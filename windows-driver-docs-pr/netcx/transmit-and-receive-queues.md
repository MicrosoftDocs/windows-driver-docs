---
title: Transmit and receive queues
description: Transmit and receive queues
ms.assetid: 4BF61CDF-4B62-47EB-936A-7DE81D62678A
keywords:
- NetAdapterCx transmit and receive queues, NetCx transmit and receive queues
ms.date: 01/19/2019
ms.localizationpriority: medium
---

# Transmit and receive queues

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

*Packet queues*, or *datapath queues* are objects introduced in NetAdapterCx to enable client drivers to model their hardware features, such as hardware transmit and receive queues, more explicitly in software drivers. This topic explains how to work with transmit and receive queues in NetAdapterCx. 

When your client driver calls [**NET_ADAPTER_DATAPATH_CALLBACKS_INIT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_datapath_callbacks_init), typically from its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://msdn.microsoft.com/library/windows/hardware/ff541693) event callback function, it provides two queue creation callbacks: [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_txqueue) and [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue). The client creates transmit and receive queues in these callbacks respectively.

The framework empties queues before transitioning to a low power state and deletes them before deleting the adapter.

## Creating a transmit queue

NetAdapterCx calls [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_txqueue) at the very end of the [power-up sequence](power-up-sequence-for-a-netadaptercx-client-driver.md). During this callback, client drivers typically do the following:

- Optionally register start and stop callbacks for the queue.
- Add packet context attributes to the queue during initialization.
- Call [**NetTxQueueInitGetQueueId**](../nettxqueue/nf-nettxqueue-nettxqueueinitgetqueueid.md) to retrieve the identifier of the transmit queue to set up.
- Call [**NetTxQueueCreate**](../nettxqueue/nf-nettxqueue-nettxqueuecreate.md) to allocate a queue. 
    - If [**NetTxQueueCreate**](../nettxqueue/nf-nettxqueue-nettxqueuecreate.md) fails, the *EvtNetAdapterCreateTxQueue* callback function should return an error code.
- Query for packet extension offsets.

The following example shows how these steps might look in code. Error handling code has been left out of this example for clarity.

```C++
NTSTATUS
EvtAdapterCreateTxQueue(
    _In_    NETADAPTER          Adapter,
    _Inout_ NETTXQUEUE_INIT *   TxQueueInit
    )
{
    NTSTATUS status = STATUS_SUCCESS;

    // Prepare the configuration structure
    NET_PACKET_QUEUE_CONFIG txConfig;
    NET_PACKET_QUEUE_CONFIG_INIT(
        &txConfig,
        EvtTxQueueAdvance,
        EvtTxQueueSetNotificationEnabled,
        EvtTxQueueCancel);

    // Optional: register the queue's start and stop callbacks
    txConfig.EvtStart = EvtTxQueueStart;
    txConfig.EvtStop = EvtTxQueueStop;

    // Initialize the first default packet context
    NET_PACKET_CONTEXT_ATTRIBUTES myTxContextAttributes;
    NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE(&myTxContextAttributes, MY_DEFAULT_TX_PACKET_CONTEXT);

    // Add the first default packet context attributes to the queue
    status = NetTxQueueInitAddPacketContextAttributes(TxQueueInit, &myTxContextAttributes);

    // Get the queue ID
    const ULONG queueId = NetTxQueueInitGetQueueId(TxQueueInit);

    // Create the transmit queue
    NETPACKETQUEUE txQueue;
    status = NetTxQueueCreate(
        TxQueueInit,
        &txAttributes,
        &txConfig,
        &txQueue);

    // Get the queue context for storing the queue ID and packet extension offset info
    PMY_TX_QUEUE_CONTEXT queueContext = GetMyTxQueueContext(txQueue);

    // Store the queue ID in the context
    queueContext->QueueId = queueId;

    // Query checksum packet extension offset and store it in the context
    NET_PACKET_EXTENSION_QUERY extension;
    NET_PACKET_EXTENSION_QUERY_INIT(
        &extension,
        NET_PACKET_EXTENSION_CHECKSUM_NAME,
        NET_PACKET_EXTENSION_CHECKSUM_VERSION_1);

    queueContext->ChecksumExtensionOffset = NetTxQueueGetPacketExtensionOffset(txQueue, &extension);

    // Query Large Send Offload packet extension offset and store it in the context
    NET_PACKET_EXTENSION_QUERY_INIT(
        &extension,
        NET_PACKET_EXTENSION_LSO_NAME,
        NET_PACKET_EXTENSION_LSO_VERSION_1);
    
    queueContext->LsoExtensionOffset = NetTxQueueGetPacketExtensionOffset(txQueue, &extension);

    return status;
}
```

## Creating a receive queue

To create a receive queue from [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue), use the same pattern as a transmit queue and call [**NetRxQueueCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueuecreate). 

The following example shows how creating a receive queue might look in code. Error handling code has been left out of this example for clarity.

```c++
NTSTATUS
EvtAdapterCreateRxQueue(
    _In_ NETADAPTER NetAdapter,
    _Inout_ PNETRXQUEUE_INIT RxQueueInit
    )
{
    NTSTATUS status = STATUS_SUCCESS;

    // Prepare the configuration structure
    NET_PACKET_QUEUE_CONFIG rxConfig;
    NET_PACKET_QUEUE_CONFIG_INIT(
        &rxConfig,
        EvtRxQueueAdvance,
        EvtRxQueueSetNotificationEnabled,
        EvtRxQueueCancel);

    // Optional: register the queue's start and stop callbacks
    rxConfig.EvtStart = EvtRxQueueStart;
    rxConfig.EvtStop = EvtRxQueueStop;

    // Initialize the per-packet context
    NET_PACKET_CONTEXT_ATTRIBUTES myRxContextAttributes;
    NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE(&myRxContextAttributes, MY_RXQUEUE_PACKET_CONTEXT);

    // Add the context attributes to the queue
    status = NetRxQueueInitAddPacketContextAttributes(RxQueueInit, &myRxContextAttributes);

    // Get the queue ID
    const ULONG queueId = NetRxQueueInitGetQueueId(RxQueueInit);

    // Create the receive queue
    NETPACKETQUEUE rxQueue;
    status = NetRxQueueCreate(
        RxQueueInit,
        &rxAttributes,
        &rxConfig,
        &rxQueue);

    // Get the queue context for storing the queue ID and packet extension offset info
    PMY_RX_QUEUE_CONTEXT queueContext = GetMyRxQueueContext(rxQueue);

    // Store the queue ID in the context
    queueContext->QueueId = queueId;

    // Query the checksum packet extension offset and store it in the context
    NET_PACKET_EXTENSION_QUERY extension;
    NET_PACKET_EXTENSION_QUERY_INIT(
        &extension,
        NET_PACKET_EXTENSION_CHECKSUM_NAME,
        NET_PACKET_EXTENSION_CHECKSUM_VERSION_1); 
          
    queueContext->ChecksumExtensionOffset = NetRxQueueGetPacketExtensionOffset(rxQueue, &extension);

    return status;
```

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