---
title: Handling I/O Requests
---

# Handling I/O Requests

In the NetAdapterCx model, network data requests are stored in WDF queues.  Each queue is associated with a ring buffer, which contains a group of packets and pointers to indicate where in the ring to read and write next.

## Creating transmit and receive queues

When your client driver calls [**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md), typically from its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) event callback function, it provides two queue creation callbacks: [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](evt-net-adapter-create-txqueue.md) and [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md).  The client creates transmit and receive queues in these callbacks.

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

Because the NETRXQUEUE and NETTXQUEUE objects are parented to the NETADAPTER, WDF automatically deletes the queues when the adapter is deleted.

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

The [**NET_RING_BUFFER**](net-ring-buffer.md) is a circular buffer of one or more [**NET_PACKET**](net-packet.md) structures that is shared between NetAdapterCx and a client.

Each element in a [**NET_RING_BUFFER**](net-ring-buffer.md) is owned by either the client driver or NetAdapterCx.  The values of the index members control ownership.  Specifically, the client driver owns every element from **BeginIndex** to **EndIndex - 1** inclusive.
For example, if **BeginIndex** is 2 and **EndIndex** is 5, the client driver owns three elements: the elements with index values 2, 3, and 4.
If **BeginIndex** is equal to **EndIndex**, the client driver does not own any elements.

NetAdapterCx adds elements to the ring buffer by incrementing **EndIndex**.
A client driver returns ownership of the elements by incrementing **BeginIndex**.

The client driver may optionally set **NextIndex** to the index of the next packet that it will submit to the hardware.

In this model, the client has submitted packets with index values between **BeginIndex** and **NextIndex - 1** inclusive to hardware.  Packets with index values between **NextIndex** and **EndIndex - 1** are owned by the client but have not yet been sent to hardware.  If the value of **BeginIndex** is equal to the value of **NextIndex**, the client has not programmed any packets to hardware.

After the hardware transmits or receives data, the client calls [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md) to return ownership of the completed packets to the class extension, which advances the **BeginIndex** accordingly.  Because the ring buffer is circular, eventually the index values wrap around the end of the buffer and come back to the beginning.

To retrieve and return packets stored in the ring buffer, use the following routines:

Although a client driver can manipulate the **NET_RING_BUFFER** directly, a client driver typically uses higher level helper routines like

* [NetRingBufferAdvanceNextPacket method](netringbufferadvancenextpacket.md)
* [NetRingBufferGetNextPacket method](netringbuffergetnextpacket.md)
* [NetRingBufferGetPacketAtIndex method](netringbuffergetpacketatindex.md)
* [NetRingBufferReturnCompletedPackets method](netringbufferreturncompletedpackets.md)
* [NetRingBufferReturnCompletedPacketsThroughIndex method](netringbufferreturncompletedpacketsthroughindex.md)

For code examples, see [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md) and [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md).
