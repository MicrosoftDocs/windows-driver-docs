---
title: Transmit and receive queues
description: Transmit and receive queues
keywords:
- NetAdapterCx transmit and receive queues, NetCx transmit and receive queues
ms.date: 01/24/2019
ms.localizationpriority: medium
ms.custom: 19H1
---

# Transmit and receive queues

## Overview

*Packet queues*, or *datapath queues* are objects introduced in NetAdapterCx to enable client drivers to model their hardware features, such as hardware transmit and receive queues, more explicitly in software drivers. This topic explains how to work with transmit and receive queues in NetAdapterCx. 

When your client driver calls [**NET_ADAPTER_DATAPATH_CALLBACKS_INIT**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-net_adapter_datapath_callbacks_init), typically from its [*EVT_WDF_DRIVER_DEVICE_ADD*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) event callback function, it provides two queue creation callbacks: [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](/windows-hardware/drivers/ddi/netadapter/nc-netadapter-evt_net_adapter_create_txqueue) and [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](/windows-hardware/drivers/ddi/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue). The client creates transmit and receive queues in these callbacks respectively.

The framework empties queues before transitioning to a low power state and deletes them before deleting the adapter.

## Creating packet queues

When creating a packet queue, either a transmit queue or a receive queue, the client must provide pointers to the following three callback functions:

- [*EVT_PACKET_QUEUE_ADVANCE*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance)
- [*EVT_PACKET_QUEUE_SET_NOTIFICATION_ENABLED*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_set_notification_enabled)
- [*EVT_PACKET_QUEUE_CANCEL*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_cancel)

In addition, the client can provide these optional callback functions after initializing the queue configuration structure:

- [*EVT_PACKET_QUEUE_START*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_start)
- [*EVT_PACKET_QUEUE_STOP*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_stop)

### Creating a transmit queue

NetAdapterCx calls [*EVT_NET_ADAPTER_CREATE_TXQUEUE*](/windows-hardware/drivers/ddi/netadapter/nc-netadapter-evt_net_adapter_create_txqueue) at the very end of the [power-up sequence](power-up-sequence-for-a-netadaptercx-client-driver.md). During this callback, client drivers typically do the following:

- Optionally register start and stop callbacks for the queue.
- Call [**NetTxQueueInitGetQueueId**](/windows-hardware/drivers/ddi/nettxqueue/nf-nettxqueue-nettxqueueinitgetqueueid) to retrieve the identifier of the transmit queue to set up.
- Call [**NetTxQueueCreate**](/windows-hardware/drivers/ddi/nettxqueue/nf-nettxqueue-nettxqueuecreate) to allocate a queue. 
    - If [**NetTxQueueCreate**](/windows-hardware/drivers/ddi/nettxqueue/nf-nettxqueue-nettxqueuecreate) fails, the *EvtNetAdapterCreateTxQueue* callback function should return an error code.
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
    NET_EXTENSION_QUERY extension;
    NET_EXTENSION_QUERY_INIT(
        &extension,
        NET_PACKET_EXTENSION_CHECKSUM_NAME,
        NET_PACKET_EXTENSION_CHECKSUM_VERSION_1);

    NetTxQueueGetExtension(txQueue, &extension, &queueContext->ChecksumExtension);

    // Query Large Send Offload packet extension offset and store it in the context
    NET_EXTENSION_QUERY_INIT(
        &extension,
        NET_PACKET_EXTENSION_LSO_NAME,
        NET_PACKET_EXTENSION_LSO_VERSION_1);
    
    NetTxQueueGetExtension(txQueue, &extension, &queueContext->LsoExtension);

    return status;
}
```

### Creating a receive queue

To create a receive queue from [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](/windows-hardware/drivers/ddi/netadapter/nc-netadapter-evt_net_adapter_create_rxqueue), use the same pattern as a transmit queue and call [**NetRxQueueCreate**](/windows-hardware/drivers/ddi/netrxqueue/nf-netrxqueue-netrxqueuecreate). 

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
    NET_EXTENSION_QUERY extension;
    NET_EXTENSION_QUERY_INIT(
        &extension,
        NET_PACKET_EXTENSION_CHECKSUM_NAME,
        NET_PACKET_EXTENSION_CHECKSUM_VERSION_1); 
          
    NetRxQueueGetExtension(rxQueue, &extension, &queueContext->ChecksumExtension);

    return status;
}
```

## Polling model

The NetAdapter data path is a polling model, and the polling operation on one packet queue is completely independent of other queues. The polling model is implemented by calling the client driver's queue advance callbacks, as shown in the following figure:

![Polling Flow.](images/polling.png)

## Advancing packet queues

The sequence of a polling operation on a packet queue is as follows:

1. The OS gives buffers to the client driver for either transmitting or receiving.
2. The client driver programs the packets to hardware.
3. The client driver returns the completed packets to the OS.

Polling operations occur within the client driver's [*EvtPacketQueueAdvance*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) callback function. Each packet queue in a client driver is backed by underlying data structures called *net rings*, which contain or link to the actual network data buffers in system memory. During *EvtPacketQueueAdvance*, client drivers carry out send and receive operations on the net rings by controlling indices within the rings, transferring buffer ownership between hardware and the OS as data is transmitted or received.

For more information about net rings, see [Introduction to net rings](introduction-to-net-rings.md).

For an example of implementing *EvtPacketQueueAdvance* for a transmit queue, see [Sending network data with net rings](sending-network-data-with-net-rings.md). For an example of implementing *EvtPacketQueueAdvance* for a receive queue, see [Receiving network data with net rings](receiving-network-data-with-net-rings.md).

## Enabling and disabling packet queue notification

When a client driver receives new packets in a packet queue's net rings, NetAdapterCx invokes the client driver's [*EvtPacketQueueSetNotificationEnabled*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_set_notification_enabled) callback function. This callback indicates to a client driver that polling (of *EvtPacketQueueAdvance* or *EvtPacketQueueCancel*) will stop and will not continue until the client driver calls [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](/windows-hardware/drivers/ddi/nettxqueue/nf-nettxqueue-nettxqueuenotifymorecompletedpacketsavailable) or [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](/windows-hardware/drivers/ddi/netrxqueue/nf-netrxqueue-netrxqueuenotifymorereceivedpacketsavailable). Typically, a PCI device uses this callback to enable Tx or Rx interrupts. Once an interrupt is received, interrupts can be disabled again and the client driver calls **NetTxQueueNotifyMoreCompletedPacketsAvailable** or **NetRxQueueNotifyMoreReceivedPacketsAvailable** to trigger the framework to begin polling again.

### Enabling and disabling notification for a transmit queue

For a PCI NIC, enabling transmit queue notification typically means enabling the transmit queue's hardware interrupt. When the hardware interrupt fires, the client calls [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](/windows-hardware/drivers/ddi/nettxqueue/nf-nettxqueue-nettxqueuenotifymorecompletedpacketsavailable) from its DPC.

Similarly, for a PCI NIC, disabling queue notification means disabling the interrupt associated with the queue.

For a device that has an asynchronous I/O model, the client typically uses an internal flag to track the enabled state. When an asynchronous operation completes, the completion handler checks this flag and calls [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](/windows-hardware/drivers/ddi/nettxqueue/nf-nettxqueue-nettxqueuenotifymorecompletedpacketsavailable) if it is set.

If NetAdapterCx calls *EvtPacketQueueSetNotificationEnabled* with *NotificationEnabled* set to **FALSE**, the client must not call [**NetTxQueueNotifyMoreCompletedPacketsAvailable**](/windows-hardware/drivers/ddi/nettxqueue/nf-nettxqueue-nettxqueuenotifymorecompletedpacketsavailable) until NetAdapterCx next calls this callback function with *NotificationEnabled* set to **TRUE**.

For example:

```C++
VOID
MyEvtTxQueueSetNotificationEnabled(
    _In_ NETPACKETQUEUE TxQueue,
    _In_ BOOLEAN NotificationEnabled
)
{
    // Optional: retrieve queue's WDF context
    MY_TX_QUEUE_CONTEXT *txContext = GetTxQueueContext(TxQueue);

    // If NotificationEnabled is TRUE, enable transmit queue's hardware interrupt
    ...
}

VOID
MyEvtTxInterruptDpc(
    _In_ WDFINTERRUPT Interrupt,
    _In_ WDFOBJECT AssociatedObject
    )
{
    MY_INTERRUPT_CONTEXT *interruptContext = GetInterruptContext(Interrupt);

    NetTxQueueNotifyMoreCompletedPacketsAvailable(interruptContext->TxQueue);
}
```

### Enabling and disabling notification for a receive queue

For a PCI NIC, enabling receive queue notification looks very similar to a Tx queue. This typically means enabling the receive queue's hardware interrupt. When the hardware interrupt fires, the client calls [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](/windows-hardware/drivers/ddi/netrxqueue/nf-netrxqueue-netrxqueuenotifymorereceivedpacketsavailable) from its DPC.

For example:

```C++
VOID
MyEvtRxQueueSetNotificationEnabled(
    _In_ NETPACKETQUEUE RxQueue,
    _In_ BOOLEAN NotificationEnabled
)
{
    // optional: retrieve queue's WDF Context
    MY_RX_QUEUE_CONTEXT *rxContext = GetRxQueueContext(RxQueue);

    // If NotificationEnabled is TRUE, enable receive queue's hardware interrupt
    ...
}

VOID
MyEvtRxInterruptDpc(
    _In_ WDFINTERRUPT Interrupt,
    _In_ WDFOBJECT AssociatedObject
    )
{
    MY_INTERRUPT_CONTEXT *interruptContext = GetInterruptContext(Interrupt);

    NetRxQueueNotifyMoreReceivedPacketsAvailable(interruptContext->RxQueue);
}
```

For a USB device, or any other queue with a software receive completion mechanism, the client driver should track in its own Context whether the queue's notification is enabled. From the completion routine (triggered for example when a message becomes available in the USB continuous reader), call [**NetRxQueueNotifyMoreReceivedPacketsAvailable**](/windows-hardware/drivers/ddi/netrxqueue/nf-netrxqueue-netrxqueuenotifymorereceivedpacketsavailable) if the notification is enabled. The following example shows how you might do this.

```C++
VOID
UsbEvtReaderCompletionRoutine(
    _In_ WDFUSBPIPE Pipe,
    _In_ WDFMEMORY Buffer,
    _In_ size_t NumBytesTransferred,
    _In_ WDFCONTEXT Context
)
{
    UNREFERENCED_PARAMETER(Pipe);

    PUSB_RCB_POOL pRcbPool = *((PUSB_RCB_POOL*) Context);
    PUSB_RCB pRcb = (PUSB_RCB) WdfMemoryGetBuffer(Buffer, NULL);

    pRcb->DataOffsetCurrent = 0;
    pRcb->DataWdfMemory = Buffer;
    pRcb->DataValidSize = NumBytesTransferred;

    WdfObjectReference(pRcb->DataWdfMemory);

    ExInterlockedInsertTailList(&pRcbPool->ListHead,
                                &pRcb->Link,
                                &pRcbPool->ListSpinLock);

    if (InterlockedExchange(&pRcbPool->NotificationEnabled, FALSE) == TRUE)
    {
        NetRxQueueNotifyMoreReceivedPacketsAvailable(pRcbPool->RxQueue);
    }
}
```

## Canceling packet queues

When the OS stops the data path, it begins by invoking the client driver's [*EvtPacketQueueCancel*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_cancel) callback function. This callback is where client drivers perform any processing needed before the framework deletes the packet queues. Canceling for a transmit queue is optional and depends on whether the hardware supports in-flight transmit cancellation, but canceling for a receive queue is required. 

During *EvtPacketQueueCancel*, drivers return packets to the OS as needed. For code examples of transmit queue and receive queue cancellation, see [Canceling network data with net rings](canceling-network-data-with-net-rings.md).

After calling the driver's *EvtPacketQueueCancel* callback, the framework continues to poll the driver's [*EvtPacketQueueAdvance*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance) callback until all packets and buffers have been returned to the OS.
