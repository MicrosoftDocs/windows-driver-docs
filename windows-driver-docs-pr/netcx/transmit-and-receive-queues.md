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
ms.localizationpriority: medium
---

# Transmit and receive queues

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

*Packet queues*, or *datapath queues* are objects introduced in NetAdapterCx to enable client drivers to model their hardware features, such as hardware transmit and receive queues, more explicitly in software drivers. This topic explains how to work with transmit and receive queues in NetAdapterCx. 

## Creating transmit and receive queues

When your client driver calls [**NET_ADAPTER_DATAPATH_CALLBACKS_INIT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_datapath_callbacks_init), typically from its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) event callback function, it provides two queue creation callbacks: [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_txqueue) and [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue). The client creates transmit and receive queues in these callbacks respectively.

For example, the client creates a transmit queue by calling [**NetTxQueueCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueuecreate) as follows:

```C++
NTSTATUS
MyEvtAdapterCreateTxQueue(
    NETADAPTER Adapter, 
    PNETTXQUEUE_INIT NetTxQueueInit
)
{
    NETPACKETQUEUE txQueue;

    // Allocate and initialize the tx queue configuration structure
    NET_PACKET_QUEUE_CONFIG txQueueConfig;
    NET_PACKET_QUEUE_CONFIG_INIT(&txQueueConfig, 
                                 EvtTxQueueAdvance,
                                 EvtTxQueueSetNotificationEnabled,
                                 EvtTxQueueCancel);

    // Optional: set the tx queue's start and stop callbacks
    txQueueConfig.EvtStart = EvtTxQueueStart;
    txQueueConfig.EvtStop = EvtTxQueueStop;

    // Assign fixed size data type as per packet context
    NET_TXQUEUE_CONFIG_SET_DEFAULT_PACKET_CONTEXT_TYPE(&txConfig, MY_CONTEXT);

    // Create the queue
    NTSTATUS status = NetTxQueueCreate(NetTxQueueInit,
                                       WDF_NO_OBJECT_ATTRIBUTES,
                                       &txQueueConfig,
                                       &txQueue);

    return status;
}
```

To create a receive queue from [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue), use the same pattern to call [**NetRxQueueCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueuecreate). For an example, see [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue).

The framework empties queues before transitioning to a low power state and deletes them before deleting the adapter.

## Implementing queue callbacks

When creating a packet queue, either a transmit queue or a receive queue, the client must provide pointers to the following three callback functions:

- [*EVT_PACKET_QUEUE_ADVANCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance)
- [*EVT_PACKET_QUEUE_SET_NOTIFICATION_ENABLED*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_set_notification_enabled)
- [*EVT_PACKET_QUEUE_CANCEL*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_cancel)

In addition, the client can provide these optional callback functions after initializing the queue configuration structure:

- [*EVT_PACKET_QUEUE_START*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_start)
- [*EVT_PACKET_QUEUE_STOP*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_stop)

See each of these pages for details on what the client needs to do in each event callback function.

## Polling model

The NetAdapter data path is a polling model, and the polling operation on one packet queue is completely independent of other queues. The polling model is implemented by calling the client driver's queue advance callbacks, as shown in the following figure:

![Polling Flow](images/polling.png)

For code examples, see [*EVT_PACKET_QUEUE_ADVANCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance).

The sequence of a polling operation is as follows:

1. The OS gives buffers to the client driver for either transmitting or receiving.
2. The client driver programs the packets to hardware.
3. The client driver returns the completed packets to the OS.
