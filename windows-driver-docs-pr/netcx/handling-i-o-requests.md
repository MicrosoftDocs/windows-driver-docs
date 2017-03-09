---
title: Handling I/O Requests
---

# Handling I/O Requests

In the NetAdapterCx model, network data requests are stored in WDF queues.  Each queue is associated with a ring buffer, which contains a group of packets and pointers to indicate where in the ring to read and write next.

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
    NTSTATUS status = NetTxQueueCreate(
        NetTxQueueInit,
        WDF_NO_OBJECT_ATTRIBUTES,
        &txQueueConfig,
        &txQueue);

    return status;
}
```

To create a receive queue from [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md), use the same pattern to call [**NetRxQueueCreate**](netrxqueuecreate.md).

Because the NETRXQUEUE and NETTXQUEUE objects are parented to the NETADAPTER, WDF automatically deletes the queues when the adapter is deleted.

When creating transmit and receive queues, the client provides pointers to the following callbacks:

* [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md)
* [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](evt-txqueue-set-notification-enabled.md)
* [*EVT_TXQUEUE_CANCEL*](evt-txqueue-cancel.md)
* [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md)
* [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md)
* [*EVT_RXQUEUE_CANCEL*](evt-rxqueue-cancel.md)

See the above pages for details on what the client needs to do in each event callback function.

The [**NET_RING_BUFFER**](net-ring-buffer.md) is a ring buffer shared between the host and a client, a container for one or more [**NET_PACKET**](net-packet.md) structures.  To retrieve and return packets stored in the ring buffer, use the following routines:

* [NetRingBufferAdvanceNextPacket method](netringbufferadvancenextpacket.md)
* [NetRingBufferGetNextPacket method](netringbuffergetnextpacket.md)
* [NetRingBufferGetPacketAtIndex method](netringbuffergetpacketatindex.md)
* [NetRingBufferReturnCompletedPackets method](netringbufferreturncompletedpackets.md)
* [NetRingBufferReturnCompletedPacketsThroughIndex method](netringbufferreturncompletedpacketsthroughindex.md)
