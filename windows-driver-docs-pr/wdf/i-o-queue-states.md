---
title: I/O Queue States
description: I/O Queue States
keywords:
- I/O queues WDK KMDF , states
- states WDK I/O queue
- current I/O queue state WDK KMDF
- idle I/O queue state WDK KMDF
- ready I/O queue state WDK KMDF
- stopped I/O queue state WDK KMDF
- drained I/O queue state WDK KMDF
- purged I/O queue state WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# I/O Queue States


The framework defines the following states for I/O queues:

<a href="" id="idle"></a>*Idle*  
The I/O queue contains no I/O requests, and the driver is not processing any requests that it received from the I/O queue.

<a href="" id="ready"></a>*Ready*  
The I/O queue can receive I/O requests from the framework, and it can deliver I/O requests to the driver.

<a href="" id="stopped"></a>*Stopped*  
The I/O queue can receive I/O requests from the framework, but it cannot deliver I/O requests to the driver, and the driver is not processing any requests that it received from the I/O queue.

<a href="" id="drained"></a>*Drained*  
The I/O queue is empty, it cannot receive new I/O requests from the framework, and all I/O requests that were in the I/O queue have been delivered to the driver.

<a href="" id="purged"></a>*Purged*  
The I/O queue is empty, it cannot receive new I/O requests from the framework, and all I/O requests that were in the I/O queue have been canceled.

The framework can set a new I/O queue to the ready state after your driver calls [**WdfIoQueueCreate**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuecreate). However, [power-managed I/O queues](using-power-managed-i-o-queues.md) enter the ready state only if the device is in its working (D0) state.

Your driver can change an I/O queue's state by:

-   Calling [**WdfIoQueueStop**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestop) or [**WdfIoQueueStopSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopsynchronously) to place the queue in its stopped state.

-   Calling [**WdfIoQueueDrain**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrain) or [**WdfIoQueueDrainSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrainsynchronously) to place the queue in its drained state.

-   Calling [**WdfIoQueuePurge**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurge) or [**WdfIoQueuePurgeSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurgesynchronously) to place the queue in its purged state.

-   Calling [**WdfIoQueueStart**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestart) to return the queue to its ready state.

To obtain an I/O queue's current state, your driver can call [**WdfIoQueueGetState**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuegetstate).

 

