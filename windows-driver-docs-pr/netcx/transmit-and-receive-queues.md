---
title: Transmit and receive queues
description: Transmit and receive queues
ms.assetid: 4BF61CDF-4B62-47EB-936A-7DE81D62678A
keywords:
- NetAdapterCx transmit and receive queues, NetCx transmit and receive queues
ms.author: windowsdriverdev
ms.date: 03/18/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Transmit and receive queues

*Packet queues*, or *datapath queues* are objects introduced in NetAdapterCx to allow the client drivers to model their hardware features, such like hardware transmit and receive queues, more explicitly in the software drivers. This topic explains how to work with transmit and receive queues in NetAdapterCx. 

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

To create a receive queue from [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md), use the same pattern to call [**NetRxQueueCreate**](netrxqueuecreate.md). For an example, see [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md).

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

## Polling model

The NetAdapter data path is a polling model. This polling model is implemented by calling the client driver's queue advance callbacks. For code examples, see [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md) and [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md).