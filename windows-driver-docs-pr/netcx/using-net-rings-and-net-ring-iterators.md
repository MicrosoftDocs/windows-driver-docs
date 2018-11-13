---
title: Using net rings and net ring iterators
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators.
ms.assetid: 8A56AA21-264C-4C1A-887E-92C9071E8AB8
keywords:
- NetAdapterCx Net rings and net ring iterators, NetCx Net rings and net ring iterators, NetAdapterCx PCI devices net ring, NetAdapterCx asynchronous I/O
ms.date: 10/30/2018
ms.localizationpriority: medium
---

# Using net rings and net ring iterators

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

## NET_RING overview

A **NET_RING** is a circular buffer of network data that is shared between NetAdapterCx and a client driver. Every packet queue in a client driver has two rings: a *packet ring* for core packet descriptors, and a *fragment ring* for each packet's fragment descriptors.

For more information about packet descriptors, see [Packet descriptors and extensions](packet-descriptors-and-extensions.md).

Every core descriptor in the packet ring has indices into the fragment ring for locating that packet's fragment descriptors. Another data structure, the **NET_RING_COLLECTION**, groups the packet ring and fragment ring together for a given packet queue.

![multi-ring layout](images/multi-ring.png) 

Every packet queue has its own **NET_RING_COLLECTION** structure, and, consequently, its own packet ring, fragment ring, and descriptors in those rings. Therefore, the network data transfer operation of each packet queue is completely independent. To learn more about packet queues, see [Transmit and receive queues](transmit-and-receive-queues.md).

## NET_RING post and drain operations

Each element in a **NET_RING** is owned by either the client driver or NetAdapterCx. The **NET_RING** contains three indices that control ownership and mark sections of the **NET_RING**, as described in the following table.

> [!IMPORTANT]
> This section describes the **NET_RING** indices and what happens when they move. However, it is important to note that client drivers do not *directly* modify these indices. Instead, to perform operations on the **NET_RING**, client drivers call into the Net Ring Iterator Interface, described in the [next section](#net-ring-iterator-interface-overview).

| **NET_RING** index name | Description | Modified by |
| --- | --- | --- |
| BeginIndex | The beginning of the range of elements in the **NET_RING** that the NIC client driver owns. **BeginIndex** is also the beginning of the *drain* section of the **NET_RING**. When **BeginIndex** is incremented, the driver *drains* the elements from the ring and transfes ownership of them to the OS. | NIC client driver, through Net Ring Iterator Interface API calls |
| NextIndex | The beginning of the *post* section of the **NET_RING**. When **NextIndex** is incremented, the driver *posts* the buffers to hardware and transfers the buffers to the drain section of the ring. | NIC client driver, through Net Ring Iterator Interface API calls |
| EndIndex | The end of the range of elements in the **NET_RING** that the NIC client driver owns. Client drivers own elements up to **EndIndex - 1** inclusive. | NetAdapterCx |

Manipulating these indices with net ring iterators during a packet queue's [*EvtPacketQueueAdvance*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) callback is how client drivers transfer network data between the system and the network interface card (NIC) hardware.

Client drivers own every element from **BeginIndex** to **EndIndex - 1** inclusive. For example, if **BeginIndex** is 2 and **EndIndex** is 5, the client driver owns three elements: the elements with index values 2, 3, and 4.

If **BeginIndex** is equal to **EndIndex**, the client driver does not own any elements.

NetAdapterCx posts elements to the ring buffer by incrementing **EndIndex**. A client driver drains the buffers and returns ownership of the elements by advancing the ring's drain iterator, which increments **BeginIndex**.

Elements with index values between **NextIndex** and **EndIndex - 1** inclusive are owned by the client but have not yet been posted to hardware.

The following animations illustrate the post and drain operations that a PCI device driver performs on a **NET_RING**. The first shows posting and draining during transmit (Tx) operations, and the second shows posting and draining during receive (Rx) operations. Note that each packet has one or more fragments during transmit, but each packet has exactly one fragment during receive. Most NICs are configured this way, although some advanced NICs are capable of receiving more than one fragment per packet.

> [!NOTE]
> In these animations, the packets owned by the client driver are highlighted in light blue and dark blue, and fragments owned by the client driver are highlighted in yellow and orange. The lighter colors represent the *drain* subsection of the elements the driver owns, while the darker colors represent the *post* subsection of the elements the driver owns.

![Net ring post and drain operations for transmit (Tx)](images/net_ring_post_and_drain_operations_tx.gif "Net ring post and drain operations for transmit (Tx)")

![Net ring post and drain operations for receive (Rx)](images/net_ring_post_and_drain_operations_rx.gif "Net ring post and drain operations for receive (Rx)")

Because the net ring is circular, eventually the index values wrap around the end of the buffer and come back to the beginning. NetAdapterCx automatically handles wrapping the index values around the ring when the client driver calls the appropriate method, as described in the following section.

## Net Ring Iterator Interface overview

NIC client drivers perform operations on net rings by calling into the *Net Ring Iterator Interface*. A [**NET_RING_ITERATOR**](net-ring-iterator.md) is a small structure that contains references to the post and drain indices of a **NET_RING** to which it belongs. 

Each **NET_RING** can have multiple iterators. For example, the packet ring might have an iterator that covers the drain section of the ring (a *drain iterator*), an iterator that covers the post section of the ring (a *post iterator*), and an iterator that covers both the post and drain sections. Likewise, the fragment ring can have the same iterators.

To make it easy for client drivers to control each iterator for each ring, the Net Ring Iterator Interface separates iterators into two categories: [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) and [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md). These are wrapper structures around the **NET_RING_ITERATOR** and are used in all Net Ring Iterator Interface API calls. Client drivers should not use a **NET_RING_ITERATOR** directly. Instead, they should use the appropriate type of iterator for a given net ring (either packet or fragment).

By advancing, getting, and setting packet and fragment iterators, client drivers post and drain network data in their packet queues' net rings. Client drivers also call methods on net ring iterators to access the ring's elements.

For a complete list of net ring iterator data structures and methods, see [Netringiterator.h](netringiterator-h.md).

## Device drivers with in-order completions

Drivers for devices that use ring buffers at the hardware level (for example, typical PCI NICs) normally complete send and receive operations in order, and control their **NET_RING** post and drain iterators accordingly.

### Transmitting data in order

Here is a typical post and drain sequence for a driver that transmits data in order.

1. Call **NetTxQueueGetRingCollection** to retrieve the transmit queue's ring collection structure. You can store this in the queue's context space to reduce calls out of the driver. 
2. Post data to hardware:    
    1. Use the ring collection to retrieve the post iterator for the transmit queue's packet ring by calling [**NetRingGetTxPostPacketIterator**](netringgettxpostpacketiterator.md).
    2. Do the following in a loop:
        1. Call [**NetRingIteratorGetPacket**](netringiteratorgetpacket.md) with the packet iterator to get a packet.
        2. Check if this packet should be ignored. If it should be ignored, skip to step 5 of this loop. If not, continue.
        3. Call [**NetRingGetTxPostPacketFragmentIterator**](netringgettxpostpacketfragmentiterator.md) to get the post iterator for this packet's fragments.
        4. Do the doing the following in a loop:
            1. Call [**NetRingIteratorGetFragment**](netringiteratorgetfragment.md) with the fragment iterator to get a fragment.
            2. Translate the **NET_FRAGMENT** descriptor into the associated hardware fragment descriptor.
            3. Call [**NetRingAdvanceFragmentIterator**](netringadvancefragmentiterator.md) to move to the next fragment for this packet.
            4. Call [**NetRingSetTxPostFragmentIterator**](netringsettxpostfragmentiterator.md) to finalize posting this fragment to hardware.
        5. Call [**NetRingAdvancePacketIterator**](netringadvancepacketiterator.md) to move to the next packet.
    3. Call [**NetRingSetTxPostPacketIterator**](netringsettxpostpacketiterator.md) to finalize posting packets to hardware.
3. Drain completed transmit packets to the OS:
    1. Use the ring collection to retrieve the drain iterator for the transmit queue's packet ring by calling [**NetRingGetTxDrainPacketIterator**](netringgettxdrainpacketiterator.md).
    2. Do the following in a loop:
        1. Check if the packet has finished transmitting. If it has not, break out of the loop.
        2. Call [**NetRingAdvancePacketIterator**](netringadvancepacketiterator.md) to move to the next packet.
    3. Call [**NetRingSetTxDrainPacketIterator**](netringsettxdrainpacketiterator.md) to finalize draining packets to the OS.

These steps might look like this in code:

```cpp
void
MyEvtTxQueueAdvance(
    NETPACKETQUEUE TxQueue
)
{
    // Get the transmit queue's context to retrieve the net ring collection
    PMY_TX_QUEUE_CONTEXT txQueueContext = MyGetTxQueueContext(TxQueue);
    NET_RING_COLLECTION const * Rings = txQueueContext->Rings;

    // Post data to hardware
    NET_RING_PACKET_ITERATOR packetIterator = NetRingGetTxPostPacketIterator(Rings);
    while(NetRingIteratorAny(packetIterator))
    {
        NET_PACKET* packet = NetRingIteratorGetPacket(&packetIterator);
        if(!packet->Ignore)
        {
            NET_FRAGMENT_ITERATOR fragmentIterator = NetRingGetTxPostPacketFragmentIterator(&packetIterator);
            for(txQueueContext->numTxDescriptors = 0; NetRingIteratorAny(fragmentIterator); txQueueContext->numTxDescriptors++)
            {
                // Translate fragment descriptor to hardware
                ...

                NetRingAdvanceFragmentIterator(&fragmentIterator);
            }
            NetRingSetTxPostFragmentIterator(&fragmentIterator);
        }
        NetRingAdvancePacketIterator(&packetIterator);
    }
    NetRingSetTxPostPacketIterator(&packetIterator);

    // Drain packets if completed
    packetIterator = NetRingGetTxDrainPacketIterator(Rings);
    while(NetRingIteratorAny(packetIterator))
    {
        // Test packet for transmit completion and break if it is not finished
        ...

        NetRingAdvancePacketIterator(&packetIterator);
    }
    NetRingSetTxDrainPacketIterator(&packetIterator);
}
```

### Receiving data in order

Here is a typical sequence for a driver that receives data in order.

For example, to complete and drain a batch of packets and their fragments from a transmit queue's net rings, a client driver might do something like this:

```cpp
void
MyCompleteTxPacketBatch(
    _In_ NET_RING_COLLECTION const * Rings,
    _In_ UINT32                      BatchSize
)
{
    UINT32 packetCount = 0;

    // Retrieve the packet drain iterator
    NET_RING_PACKET_ITERATOR packetIterator = NetRingGetTxDrainPacketIterator(Rings);
    while(NetRingIteratorAny(packetIterator))
    {
        // Get the packet
        NET_PACKET* packet = NetRingIteratorGetPacket(&packetIterator);

        // Test the packet for completion. You can either use the Scratch field of the packet or some other tracking method.
        if(!myPacketCompletionTest)
        {
            break;
        }

        packetCount++;

        // Get this packet's fragments
        NET_RING_FRAGMENT_ITERATOR fragmentIterator = NetRingGetTxDrainPacketFragmentIterator(&packetIterator);

        // Drain the fragments
        NetRingAdvanceEndFragmentIterator(&fragmentIterator);

        // Move on to the next packet
        NetRingAdvancePacketIterator(&packetIterator);

        // Finish draining packets and fragments if desired batch is complete
        if(packetCount >= BatchSize)
        {
            NetRingSetTxDrainPacketIterator(&packetIterator);
            NetRingSetTxDrainFragmentIterator(&fragmentIterator);
        }
    }
}
```

To cancel and drain all fragments from the ring back to the OS, a client driver calls these three methods in order:

1. [**NetRingGetAllFragmentIterator**](netringgetallfragmentiterator.md)
2. **NetRingAdvanceEndFragmentIterator**
3. [**NetRingSetAllFragmentIterator**](netringsetallfragmentiterator.md)

```cpp

```

For example, to cancel and drain all packets from the ring back to the OS, a client driver calls these three methods in order:

1. [**NetRingGetAllPacketIterator**](netringgetallpacketiterator.md)
2. **NetRingAdvanceEndPacketIterator**
3. [**NetRingSetAllPacketIterator**](netringsetallpacketiterator.md)


Here is a typical receive sequence for a driver that performs in-order completions:

1. Step 1
2. Step 2
etc.

```cpp
```

### Device drivers with out-of-order completions

Drivers for devices that process send and receive operations out-of-order (for example, many USB NICs) perform steps similarly to in-order device drivers. Such drivers might use the **Scratch** field of each **NET_FRAGMENT** to track completion. Only when a batch of fragments has been completed can the driver advance and set the iterators for those fragments and their packets.

For example, an out-of-order transmit sequence might look like this:

1. Step 1
2. Step 2
etc.

```cpp
```

## Other Net Ring Iterator Interface operations

Besides typical NIC driver post and drain, mention things like cancelation, using the getall/setall APIs, the AdvanceEnd APIs, and NetRingIteratorAny.