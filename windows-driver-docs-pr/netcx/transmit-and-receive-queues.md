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

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

*Packet queues*, or *datapath queues* are objects introduced in NetAdapterCx to enable client drivers to model their hardware features, such as hardware transmit and receive queues, more explicitly in software drivers. This topic explains how to work with transmit and receive queues in NetAdapterCx. 

## Creating transmit and receive queues

When your client driver calls [**NET_ADAPTER_CONFIG_INIT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_config_init), typically from its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) event callback function, it provides two queue creation callbacks: [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_txqueue) and [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue). The client creates transmit and receive queues in these callbacks.

For example, the client creates a transmit queue by calling [**NetTxQueueCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueuecreate) as follows:

```C++
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

To create a receive queue from [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue), use the same pattern to call [**NetRxQueueCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueuecreate). For an example, see [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue).

The framework empties queues before transitioning to a low power state and deletes them before deleting the adapter.

## Implementing queue callbacks

When creating a transmit (Tx) queue, the client must provide pointers to all three of the following callback functions:

* [*EVT_TXQUEUE_ADVANCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nc-nettxqueue-evt_txqueue_advance)
* [*EVT_TXQUEUE_SET_NOTIFICATION_ENABLED*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nc-nettxqueue-evt_txqueue_set_notification_enabled)
* [*EVT_TXQUEUE_CANCEL*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nc-nettxqueue-evt_txqueue_cancel)

Similarly, when creating a receive (Rx) queue, the client must provide pointers to all three of the receive queue callbacks:

* [*EVT_RXQUEUE_ADVANCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nc-netrxqueue-evt_rxqueue_advance)
* [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nc-netrxqueue-evt_rxqueue_set_notification_enabled)
* [*EVT_RXQUEUE_CANCEL*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nc-netrxqueue-evt_rxqueue_cancel)

See each of these pages for details on what the client needs to do in each event callback function.

## Polling model

The NetAdapter data path is a polling model. This polling model is implemented by calling the client driver's queue advance callbacks. For code examples, see [*EVT_TXQUEUE_ADVANCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nc-nettxqueue-evt_txqueue_advance) and [*EVT_RXQUEUE_ADVANCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nc-netrxqueue-evt_rxqueue_advance).