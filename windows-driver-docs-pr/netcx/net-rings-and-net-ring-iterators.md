---
title: Introduction to net rings and net ring iterators
description: This topic describes net rings and net ring iterators.
ms.assetid: 8A56AA21-264C-4C1A-887E-92C9071E8AB8
keywords:
- NetAdapterCx Introduction to net rings and net ring iterators, NetCx Introduction to net rings and net ring iterators, NetAdapterCx PCI devices net ring, NetAdapterCx asynchronous I/O
ms.date: 07/01/2019
ms.localizationpriority: medium
ms.custom: 19H1
---

# Introduction to net rings and net ring iterators

## NET_RING overview

A **NET_RING** is a circular buffer of network data that is shared between NetAdapterCx and a client driver. Every packet queue in a client driver has two rings: a *packet ring* for core packet descriptors, and a *fragment ring* for each packet's fragment descriptors.

For more information about packet descriptors, see [Packet descriptors and extensions](packet-descriptors-and-extensions.md).

Every core descriptor in the packet ring has indices into the fragment ring for locating that packet's fragment descriptors. Another data structure, the **NET_RING_COLLECTION**, groups the packet ring and fragment ring together for a given packet queue as shown in the following diagram.

![multi-ring layout](images/multi-ring.png) 

Every packet queue has its own **NET_RING_COLLECTION** structure, and, consequently, its own packet ring, fragment ring, and descriptors in those rings. Therefore, the network data transfer operation of each packet queue is completely independent. To learn more about packet queues, see [Transmit and receive queues](transmit-and-receive-queues.md).

## NET_RING element ownership

Each element in a **NET_RING** is owned by either the client driver or NetAdapterCx. Ownership is controlled by three indices, which mark sections of the **NET_RING**. These indices are described in the following table. The act of moving these indices, which client drivers do by calling into the [Net Ring Iterator Interface](#net-ring-iterator-interface-overview), is described by *post* and *drain* semantics. 

| **NET_RING** index name | Description | Required for transferring network data | Modified by |
| --- | --- | --- | --- |
| BeginIndex | The beginning of the range of elements in the **NET_RING** that the NIC client driver owns. **BeginIndex** is also the beginning of the *drain* section of the **NET_RING**. When **BeginIndex** is incremented, the driver *drains* the elements from the ring and transfers ownership of them to the OS. | Yes | NIC client driver, through Net Ring Iterator Interface API calls |
| NextIndex | The beginning of the *post* section of the **NET_RING**. **NextIndex** divides the section of the ring that the client driver owns into the post and drain subsections. When **NextIndex** is incremented, the driver *posts* the buffers to hardware and transfers the buffers to the drain section of the ring. | No | NIC client driver, through Net Ring Iterator Interface API calls |
| EndIndex | The end of the range of elements in the **NET_RING** that the NIC client driver owns. Client drivers own elements up to **EndIndex - 1** inclusive. | Yes | NetAdapterCx |

Manipulating these indices with net ring iterators during a packet queue's [*EvtPacketQueueAdvance*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) callback is how client drivers transfer network data between the system and the network interface card (NIC) hardware.

Client drivers own every element from **BeginIndex** to **EndIndex - 1** inclusive. For example, if **BeginIndex** is 2 and **EndIndex** is 5, the client driver owns three elements: the elements with index values 2, 3, and 4.

If **BeginIndex** is equal to **EndIndex**, the client driver does not own any elements.

NetAdapterCx posts elements to the ring buffer by incrementing **EndIndex**. A client driver drains the buffers and returns ownership of the elements by advancing the ring's drain iterator, which increments **BeginIndex**.

**NextIndex** is optional for client drivers to use, and is provided for convenience in separating the post and drain subsections of the client driver's section of the ring.

Elements with index values between **NextIndex** and **EndIndex - 1** inclusive are owned by the client but have not yet been posted to hardware. If **NextIndex** is equal to **BeginIndex**, the client driver does not have any completed buffers to transfer to the OS. If **NextIndex** is equal to **EndIndex**, the client driver does not have any buffers to post to hardware.

Because the net ring is circular, eventually the index values wrap around the end of the buffer and come back to the beginning. NetAdapterCx automatically handles wrapping the index values around the ring when the client driver calls the appropriate method, as described in the following section.

For specific information about managing the elements in net rings, see [Net ring element management](net-ring-element-management.md).

## Net Ring Iterator Interface overview

NIC client drivers perform post and drain operations on net rings by calling into the *Net Ring Iterator Interface*. A [**NET_RING_ITERATOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/ns-netringiterator-_net-ring-iterator) is a small structure that contains references to the post and drain indices of a **NET_RING** to which it belongs. 

Each **NET_RING** can have multiple iterators. For example, the packet ring might have an iterator that covers the drain section of the ring (a *drain iterator*), an iterator that covers the post section of the ring (a *post iterator*), and an iterator that covers both the post and drain sections. Likewise, the fragment ring can have the same iterators.

To make it easy for client drivers to control each iterator for each ring, the Net Ring Iterator Interface separates iterators into two categories: [**NET_RING_PACKET_ITERATOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/ns-netringiterator-_net-ring-packet-iterator) and [**NET_RING_FRAGMENT_ITERATOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/ns-netringiterator-_net-ring-fragment-iterator). These are wrapper structures around the **NET_RING_ITERATOR** and are used in all Net Ring Iterator Interface API calls. Client drivers should not use a **NET_RING_ITERATOR** directly. Instead, they should use the appropriate type of iterator for a given net ring (either packet or fragment).

By getting, advancing, and setting net ring iterators, client drivers send and receive network data in their packet queues. Client drivers also call methods on net ring iterators to access the ring's elements.

For a complete list of net ring iterator data structures and methods, see [Netringiterator.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/netringiterator/).

## Sending and receiving network data with net rings and net ring iterators

See the following topics for more information and code samples about sending and receving network data in net rings.

[Sending network data with net rings](sending-network-data-with-net-rings.md)

[Receiving network data with net rings](receiving-network-data-with-net-rings.md)
