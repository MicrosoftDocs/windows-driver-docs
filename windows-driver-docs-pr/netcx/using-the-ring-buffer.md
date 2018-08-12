---
title: Using the ring buffer
description: Using the ring buffer
ms.assetid: 8A56AA21-264C-4C1A-887E-92C9071E8AB8
keywords:
- NetAdapterCx using the ring buffer, NetCx using the ring buffer, NetAdapterCx PCI devices ring buffer, NetAdapterCx asynchronous I/O
ms.author: windowsdriverdev
ms.date: 03/18/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Using the ring buffer

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

A [**NET_RING_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringbuffer/ns-netringbuffer-_net_ring_buffer) is a circular buffer of one or more [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet) structures that is shared between NetAdapterCx and a client. To access a queue's packet ring buffer, first call **NetRx(Tx)QueueGetDatapathDescriptor** to get the queue's datapath descriptor structure, then call the [NET_DATAPATH_DESCRIPTOR_GET_PACKET_RING_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_datapath_descriptor_get_packet_ring_buffer) macro to get the ring buffer.

Each element in the packet ring buffer is owned by either the client driver or NetAdapterCx. The values of the index members control ownership. Specifically, the client driver owns every element from **BeginIndex** to **EndIndex - 1** inclusive.

For example, if **BeginIndex** is 2 and **EndIndex** is 5, the client driver owns three elements: the elements with index values 2, 3, and 4.
If **BeginIndex** is equal to **EndIndex**, the client driver does not own any elements.

NetAdapterCx adds elements to the ring buffer by incrementing **EndIndex**. A client driver returns ownership of the elements by incrementing **BeginIndex**.

The client driver may optionally set **NextIndex** to the index of the next packet that it will submit to the hardware.

![Using the ring buffer](images/using-the-ring-buffer.gif "Using the ring buffer")

In this model, the client has submitted packets with index values between **BeginIndex** and **NextIndex - 1** inclusive to hardware. Packets with index values between **NextIndex** and **EndIndex - 1** are owned by the client but have not yet been sent to hardware. If the value of **BeginIndex** is equal to the value of **NextIndex**, the client has not programmed any packets to hardware.

After the hardware transmits or receives data, the client advances **BeginIndex** to transfer ownership of the packets to NetAdapterCx. If the client tracks packet completion using the **Completed** flag on **NET_PACKET_FRAGMENT**, the client can call [**NetRingBufferReturnCompletedPackets**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferreturncompletedpackets) to advance **BeginIndex** automatically through each completed packet.

Because the ring buffer is circular, eventually the index values wrap around the end of the buffer and come back to the beginning. To handle wrap around when incrementing ring buffer indices, call [**NetRingBufferIncrementIndex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netringbuffer/nf-netringbuffer-netringbufferincrementindex).

## PCI Device Drivers

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

## Device Drivers with Asynchronous I/O

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
