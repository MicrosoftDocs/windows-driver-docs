---
title: Transferring network data
description: Transferring network data
ms.assetid: D2AC8269-F2D5-4FDC-A59E-6A35DBB18FF0
keywords:
- NetAdapterCx transferring network data, NetCx transferring network data
ms.author: windowsdriverdev
ms.date: 06/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Transferring network data

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

To watch a video that introduces the data path model in NetAdapterCx, see the [Network Adapter Class Extension: Data Path](https://aka.ms/netadapter/video3) video on Channel 9.

In the NetAdapterCx model, network data requests are stored in WDF queues. Each queue is associated with a ring buffer, which contains a group of packets and pointers to indicate where in the ring to read and write next.

## Creating transmit and receive queues

When your client driver calls [**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md), typically from its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) event callback function, it provides two queue creation callbacks: [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md) and [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md). The client creates transmit and receive queues in these callbacks.

For example, the client creates a transmit queue by calling [**NetTxQueueCreate**](nettxqueuecreate.md) as follows:

```cpp
NTSTATUS
EvtAdapterCreateTxQueue(NETADAPTER Adapter, PNETTXQUEUE_INIT NetTxQueueInit)
{
    NETTXQUEUE txQueue;

    NET_TXQUEUE_CONFIG txQueueConfig;
    NET_TXQUEUE_CONFIG_INIT(&txQueueConfig, 
                            EvtTxQueueAdvance,
                            EvtTxQueueSetNotificationEnabled,
                            EvtTxQueueCancel);

    // Assign fixed size data type as per packet context

    NET_TXQUEUE_CONFIG_SET_DEFAULT_PACKET_CONTEXT_TYPE(&txConfig, MY_CONTEXT);

    NTSTATUS status = NetTxQueueCreate(
        NetTxQueueInit,
        WDF_NO_OBJECT_ATTRIBUTES,
        &txQueueConfig,
        &txQueue);

    return status;
}
```

To create a receive queue from [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md), use the same pattern to call [**NetRxQueueCreate**](netrxqueuecreate.md).  For an example, see [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md).

The framework empties queues before transitioning to a low power state and deletes them before deleting the adapter.

## Implementing queue callbacks

When creating a transmit (Tx) queue, the client must provide pointers to all three of the following callback functions:

* [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md)
* [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md)
* [*EVT_TXQUEUE_CANCEL*](evt-txqueue-cancel.md)

Similarly, when creating a receive (Rx) queue, the client must provide pointers to all three of the receive queue callbacks:

* [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md)
* [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md)
* [*EVT_RXQUEUE_CANCEL*](evt-rxqueue-cancel.md)

See the above pages for details on what the client needs to do in each event callback function.

## Using the ring buffer

A [**NET_RING_BUFFER**](net-ring-buffer.md) is a circular buffer of one or more [**NET_PACKET**](net-packet.md) structures that is shared between NetAdapterCx and a client. In NetAdapterCx 1.2 and later, each datapath queue has two ring buffers: one **NET_PACKET** ring buffer and one [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) ring buffer. Both ring buffers are described by a [NET_DATAPATH_DESCRIPTOR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/ns-netdatapathdescriptor-_net_datapath_descriptor) structure.

> [!IMPORTANT]
> Each packet in the packet ring buffer references the start of its fragments in the fragment ring buffer. Therefore, the fragment ring buffer makes it easy to query a packet for how many fragments it has, retrieve a single fragment, or loop over all fragments in a packet, but it is not accessed directly. This topic explains how client drivers work with the packet ring buffer.

Each element in a packet [**NET_RING_BUFFER**](net-ring-buffer.md) is owned by either the client driver or NetAdapterCx.  The values of the index members control ownership.  Specifically, the client driver owns every element from **BeginIndex** to **EndIndex - 1** inclusive.
For example, if **BeginIndex** is 2 and **EndIndex** is 5, the client driver owns three elements: the elements with index values 2, 3, and 4.
If **BeginIndex** is equal to **EndIndex**, the client driver does not own any elements.

NetAdapterCx adds elements to the ring buffer by incrementing **EndIndex**.
A client driver returns ownership of the elements by incrementing **BeginIndex**.

The client driver may optionally set **NextIndex** to the index of the next packet that it will submit to the hardware.

![Using the ring buffer](images/using-the-ring-buffer.gif "Using the ring buffer")

In this model, the client has submitted packets with index values between **BeginIndex** and **NextIndex - 1** inclusive to hardware.  Packets with index values between **NextIndex** and **EndIndex - 1** are owned by the client but have not yet been sent to hardware.  If the value of **BeginIndex** is equal to the value of **NextIndex**, the client has not programmed any packets to hardware.

After the hardware transmits or receives data, the client advances **BeginIndex** to transfer ownership of the packets to NetAdapterCx.  If the client tracks packet completion using the **Completed** flag on **NET_PACKET_FRAGMENT**, the client can call [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md) to advance **BeginIndex** automatically through each completed packet.

Because the ring buffer is circular, eventually the index values wrap around the end of the buffer and come back to the beginning.  To handle wrap around when incrementing ring buffer indices, call [**NetRingBufferIncrementIndex**](NetRingBufferIncrementIndex.md).

## Polling model

The NetAdapter data path is a polling model.  This polling model is implemented by calling the client driver's queue advance callbacks.  For code examples, see [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md) and [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md).

## PCI Device Drivers

Drivers for devices that use ring buffers at the hardware level (for example, typical PCI NICs) normally manipulate the [**NET_RING_BUFFER**](net-ring-buffer.md) indices directly.

Here is a typical sequence for a PCI device driver:

1. Call [**NetRxQueueGetDatapathDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueuegetdatapathdescriptor) or [**NetTxQueueGetDatapathDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueuegetdatapathdescriptor) to retrieve the queue's datapath descriptor. You can store this in the queue's context space to reduce calls out of the driver.
2. Use the datapath descriptor to retrieve the queue's packet ring buffer by calling [NET_DATAPATH_DESCRIPTOR_GET_PACKET_RING_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_datapath_descriptor_get_packet_ring_buffer).
3. Program packets to hardware by looping until the ring buffer's **NextIndex** equals **EndIndex**:
    1.  Call [**NetRingBufferGetPacketAtIndex**](NetRingBufferGetPacketAtIndex.md) on **NextIndex**.
    2.  Translate the **NET_PACKET** descriptor into the associated hardware packet descriptors.
    3.  Call [**NetRingBufferIncrementIndex**](NetRingBufferIncrementIndex.md).
4. Complete packets by looping until **BeginIndex** equals **NextIndex** or until an incomplete packet is reached:
    1.  Call [**NetRingBufferGetPacketAtIndex**](NetRingBufferGetPacketAtIndex.md) on **BeginIndex**.
    2.  Detect if the associated hardware descriptors indicate completion.  If not, terminate.
    3.  Translate the hardware descriptor to the [**NET_PACKET**](net-packet.md).
    4.  Call [**NetRingBufferIncrementIndex**](NetRingBufferIncrementIndex.md).

## Device Drivers with Asynchronous I/O

While a client driver that targets a device with an asynchronous I/O model, such as USB, can also modify the [**NET_RING_BUFFER**](net-ring-buffer.md) indices directly, we recommend instead using higher level routines to manage out-of-order-completions:

* [**NetRingBufferAdvanceNextPacket**](netringbufferadvancenextpacket.md)
* [**NetRingBufferGetNextPacket**](netringbuffergetnextpacket.md)
* [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md)

Here is a typical sequence for a device driver with asynchronous I/O:

1. [**NetRxQueueGetDatapathDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueuegetdatapathdescriptor) or [**NetTxQueueGetDatapathDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueuegetdatapathdescriptor) to retrieve the queue's datapath descriptor.
2. Use the datapath descriptor to retrieve the queue's packet ring buffer by calling [NET_DATAPATH_DESCRIPTOR_GET_PACKET_RING_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_datapath_descriptor_get_packet_ring_buffer).
3. Iterate on the packets in the ring buffer. Typically, do the following in a loop:
    1. Call [**NetRingBufferGetNextPacket**](netringbuffergetnextpacket.md).
    2. Program hardware to receive or transmit. This initiates the asynchronous I/O.
    3. Call [**NetRingBufferAdvanceNextPacket**](netringbufferadvancenextpacket.md).
4. Call [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md).

As asynchronous I/O completions come in, the client sets the **Completed** flag of the first associated [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) to **TRUE**.  This enables [**NetRingBufferReturnCompletedPackets**](NetRingBufferReturnCompletedPackets.md) to complete packets.
