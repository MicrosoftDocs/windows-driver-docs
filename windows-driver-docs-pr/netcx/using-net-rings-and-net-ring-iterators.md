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

Each element in a **NET_RING** is owned by either the client driver or NetAdapterCx. The **NET_RING** contains three indices that control ownership and mark sections of the **NET_RING**. Manipulating these indices during a packet queue's [*EvtPacketQueueAdvance*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) callback is how client drivers transfer network data between the system and NIC hardware.

> [!NOTE] 
> This section describes the **NET_RING** indices and their underlying post and drain concepts for transferring network data. To perform operations on a **NET_RING**, client drivers call into the Net Ring Iterator Interface, described in the [next section](#net-ring-iterator-interface-overview).

| **NET_RING** index name | Description | Modified by |
| --- | --- | --- |
| BeginIndex | The beginning of the range of elements in the **NET_RING** that the NIC client driver owns. **BeginIndex** is also the beginning of the *drain* section of the **NET_RING**. When **BeginIndex** is incremented, the driver *drains* the elements from the ring and transfes ownership of them to the OS. | NIC client driver, through Net Ring Iterator Interface API calls |
| NextIndex | The beginning of the *post* section of the **NET_RING**. When **NextIndex** is incremented, the driver *posts* the buffers to hardware and transfers the buffers to the drain section of the ring. | NIC client driver, through Net Ring Iterator Interface API calls |
| EndIndex | The end of the range of elements in the **NET_RING** that the NIC client driver owns. Client drivers own elements up to **EndIndex - 1** inclusive. | NetAdapterCx |

Client drivers own every element from **BeginIndex** to **EndIndex - 1** inclusive. For example, if **BeginIndex** is 2 and **EndIndex** is 5, the client driver owns three elements: the elements with index values 2, 3, and 4.

If **BeginIndex** is equal to **EndIndex**, the client driver does not own any elements.

NetAdapterCx posts elements to the ring buffer by incrementing **EndIndex**. A client driver drains the buffers and returns ownership of the elements by incrementing **BeginIndex**.

Elements with index values between **NextIndex** and **EndIndex - 1** inclusive are owned by the client but have not yet been posted to hardware.

After the hardware transmits or receives data, the client advances **BeginIndex**, transferring ownership of the packets and their fragments back to NetAdapterCx.

The following animation illustrates the post and drain operations for a **NET_RING** during transmit (Tx). Note that each packet has one or more fragments during transmit.

![Net ring post and drain operations for transmit (Tx)](images/net_ring_post_and_drain_operations_tx.gif "Net ring post and drain operations for transmit (Tx)")

The following animation illustrates post and drain operations for a **NET_RING** during receive (Rx). Note that, unlike in the transmit animation, each packet corresponds to one fragment. This is typical for most (but not all) NICs. 

![Net ring post and drain operations for receive (Rx)](images/net_ring_post_and_drain_operations_rx.gif "Net ring post and drain operations for receive (Rx)")

Because the net ring is circular, eventually the index values wrap around the end of the buffer and come back to the beginning. NetAdapterCx automatically handles wrapping the index values around the ring when the client driver calls the appropriate method, as described in the following section.

## Net Ring Iterator Interface overview

NIC client drivers perform operations on net rings by calling into the *Net Ring Iterator Interface*. A [**NET_RING_ITERATOR**](net-ring-iterator.md) is a small structure that contains references to the post and drain indices of a **NET_RING** to which it belongs. 

Each **NET_RING** can have multiple iterators. For example, the packet ring might have an iterator that covers the drain section of the ring (a *drain iterator*), an iterator that covers the post section of the ring (a *post iterator*), and an iterator that covers both the post and drain sections. Likewise, the fragment ring can have the same iterators.

To make it easy for client drivers to control each iterator for each ring, the Net Ring Iterator Interface separates iterators into two categories: [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) and [**NET_RING_FRAGMENT_ITERATOR**](net-ring-fragment-iterator.md). These are wrapper structures around the **NET_RING_ITERATOR** and are used in all Net Ring Iterator Interface API calls.

By advancing, getting, and setting packet and fragment iterators, client drivers post and drain network data in their packet queues' net rings. Client drivers also call methods on net ring iterators to access the ring's elements.

For a list of net ring iterator data structures and methods, see [Netringiterator.h](netringiterator-h.md).

## Using the Net Ring Iterator Interface

### PCI Device Drivers

Drivers for devices that use ring buffers at the hardware level (for example, typical PCI NICs) normally manipulate the [**NET_RING_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringbuffer/ns-netringbuffer-_net_ring_buffer) indices directly.

Here is a typical sequence for a PCI device driver:

1. Call [**NetRxQueueGetDatapathDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueuegetdatapathdescriptor) or [**NetTxQueueGetDatapathDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueuegetdatapathdescriptor) to retrieve the queue's datapath descriptor. You can store this in the queue's context space to reduce calls out of the driver.
2. Use the datapath descriptor to retrieve the queue's packet ring buffer by calling [NET_DATAPATH_DESCRIPTOR_GET_PACKET_RING_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_datapath_descriptor_get_packet_ring_buffer).
3. Program packets to hardware by looping until the ring buffer's **NextIndex** equals **EndIndex**:
    1. Call [**NetRingBufferGetPacketAtIndex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbuffergetpacketatindex) on **NextIndex**.
    2. Translate the **NET_PACKET** descriptor into the associated hardware packet descriptors.
    3. Call [**NetRingBufferIncrementIndex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringbuffer/nf-netringbuffer-netringbufferincrementindex).
4. Complete packets by looping until **BeginIndex** equals **NextIndex** or until an incomplete packet is reached:
    1. Call [**NetRingBufferGetPacketAtIndex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbuffergetpacketatindex) on **BeginIndex**.
    2. Detect if the associated hardware descriptors indicate completion. If not, terminate.
    3. Translate the hardware descriptor to the [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet).
    4. Call [**NetRingBufferIncrementIndex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringbuffer/nf-netringbuffer-netringbufferincrementindex).

```C++
```

### Device Drivers with Asynchronous I/O

While a client driver that targets a device with an asynchronous I/O model, such as USB, can also modify the [**NET_RING_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringbuffer/ns-netringbuffer-_net_ring_buffer) indices directly, we recommend instead using higher level routines to manage out-of-order-completions:

* [**NetRingBufferAdvanceNextPacket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferadvancenextpacket)
* [**NetRingBufferGetNextPacket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbuffergetnextpacket)
* [**NetRingBufferReturnCompletedPackets**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferreturncompletedpackets)

Here is a typical sequence for a device driver with asynchronous I/O:

1. Call [**NetRxQueueGetDatapathDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueuegetdatapathdescriptor) or [**NetTxQueueGetDatapathDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueuegetdatapathdescriptor) to retrieve the queue's datapath descriptor.
2. Use the datapath descriptor to retrieve the queue's packet ring buffer by calling [NET_DATAPATH_DESCRIPTOR_GET_PACKET_RING_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_datapath_descriptor_get_packet_ring_buffer).
3. Iterate on the packets in the ring buffer. Typically, do the following in a loop:
    1. Call [**NetRingBufferGetNextPacket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbuffergetnextpacket).
    2. Program hardware to receive or transmit. This initiates the asynchronous I/O.
    3. Call [**NetRingBufferAdvanceNextPacket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferadvancenextpacket).
4. Call [**NetRingBufferReturnCompletedPackets**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferreturncompletedpackets).

As asynchronous I/O completions come in, the client sets the **Completed** flag of the first associated [**NET_PACKET_FRAGMENT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_fragment) to **TRUE**. This enables [**NetRingBufferReturnCompletedPackets**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferreturncompletedpackets) to complete packets. To access the first associated **NET_PACKET_FRAGMENT** of a packet, call the [NET_PACKET_GET_FRAGMENT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_packet_get_fragment) macro with the packet, the queue's datapath descriptor, and the *0* index parameters.

```C++
```