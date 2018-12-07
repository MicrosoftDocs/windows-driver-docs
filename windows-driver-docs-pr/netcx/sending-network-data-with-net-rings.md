---
title: Sending network data using net rings
description: This topic describes how NetAdapterCx client drivers use net rings and net ring iterators to send network data.
ms.assetid: 2F3DA1A5-D0C1-4928-80B2-AF41F949FF14
keywords:
- NetAdapterCx Net rings and net ring iterators, NetCx Net rings and net ring iterators, NetAdapterCx PCI devices net ring, NetAdapterCx asynchronous I/O
ms.date: 12/06/2018
ms.localizationpriority: medium
---

# Sending network data with net rings

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

## Transmit (Tx) post and drain operation overview

The following animation illustrates how a client driver for a simple PCI network interface card (NIC) performs post and drain operations for a transmit (Tx) queue.  

![Net ring post and drain operations for transmit (Tx)](images/net_ring_post_and_drain_operations_tx.gif "Net ring post and drain operations for transmit (Tx)")

In this animation, the packets owned by the client driver are highlighted in light blue and dark blue, and fragments owned by the client driver are highlighted in yellow and orange. The lighter colors represent the *drain* subsection of the elements the driver owns, while the darker colors represent the *post* subsection of the elements the driver owns.

## Sending data in order

Here is a typical post and drain sequence for a driver whose device transmits data in order, such as a simple PCI NIC.

1. Call **NetTxQueueGetRingCollection** to retrieve the transmit queue's ring collection structure. You can store this in the queue's context space to reduce calls out of the driver. 
2. Post data to hardware:    
    1. Use the ring collection to retrieve the post iterator for the transmit queue's packet ring by calling [**NetRingGetTxPostPacketIterator**](netringgettxpostpacketiterator.md).
    2. Do the following in a loop:
        1. Get a packet by calling [**NetRingIteratorGetPacket**](netringiteratorgetpacket.md) with the packet iterator.
        2. Check if this packet should be ignored. If it should be ignored, skip to step 5 of this loop. If not, continue.
        3. Get the post iterator for this packet's fragments by calling [**NetRingGetTxPostPacketFragmentIterator**](netringgettxpostpacketfragmentiterator.md).
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

These steps might look like this in code. Note the use of the [**NetRingIteratorAny**](netringiteratorany.md) method as a `while` loop testing condition. This method determines whether the iterator has reached its **End** or not. If it has not reached its **End**, the iterator has a valid element to process.

```cpp
void
MyEvtTxQueueAdvance(
    NETPACKETQUEUE TxQueue
)
{
    // Get the transmit queue's context to retrieve the net ring collection
    PMY_TX_QUEUE_CONTEXT txQueueContext = MyGetTxQueueContext(TxQueue);
    NET_RING_COLLECTION const * Rings = txQueueContext->Rings;

    //
    // Post data to hardware
    //
    NET_RING_PACKET_ITERATOR packetIterator = NetRingGetTxPostPacketIterator(Rings);
    while(NetRingIteratorAny(packetIterator))
    {
        NET_PACKET* packet = NetRingIteratorGetPacket(&packetIterator);
        if(!packet->Ignore)
        {
            NET_FRAGMENT_ITERATOR fragmentIterator = NetRingGetTxPostPacketFragmentIterator(&packetIterator);
            for(txQueueContext->numTxDescriptors = 0; 
                NetRingIteratorAny(fragmentIterator); 
                txQueueContext->numTxDescriptors++)
            {
                // Translate fragment descriptor to hardware
                ...
                //

                NetRingAdvanceFragmentIterator(&fragmentIterator);
            }
            NetRingSetTxPostFragmentIterator(&fragmentIterator);
        }
        NetRingAdvancePacketIterator(&packetIterator);
    }
    NetRingSetTxPostPacketIterator(&packetIterator);

    //
    // Drain packets if completed
    //
    packetIterator = NetRingGetTxDrainPacketIterator(Rings);
    while(NetRingIteratorAny(packetIterator))
    {        
        NET_PACKET* packet = NetRingIteratorGetPacket(&packetIterator);
        
        // Test packet for transmit completion by checking hardware ownership flags in the packet's last fragment
        ..
        //
        
        NetRingAdvancePacketIterator(&packetIterator);
    }
    NetRingSetTxDrainPacketIterator(&packetIterator);
}
```

## Sending data out of order

For drivers whose devices might complete transmissions out of order, the primary difference from in-order devices lies in who allocates the transmit buffers and how the driver handles the test for transmission completion. For in-order transmissions with a PCI NIC that is DMA-capable, the OS typically allocates, attaches, and ultimately owns the fragment buffers. Then, in order, the client driver can test each fragment's corresponding hardware ownership flag during *EvtPacketQueueAdvance*.

In contrast to this model, consider a typical USB-based NIC. In this situation, the USB stack owns the memory buffers for transmission and those buffers might be located elsewhere in system memory. The USB stack indicates completions to the client driver out of order, so the client driver needs to record a packet's completion status separately during its completion callback routine. To do so, the client driver can either use the packet's **Scratch** field, or it can use some other method like storing information in its queue context space. Then, in the call to [*EvtPacketQueueAdvance*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance), the client driver checks this information for packet completion testing. 