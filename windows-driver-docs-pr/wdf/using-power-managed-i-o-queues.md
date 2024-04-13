---
title: Using Power-Managed I/O Queues
description: Using Power-Managed I/O Queues
keywords:
- I/O queues WDK KMDF , power-managed
- power-managed I/O queues WDK KMDF
- Requeue argument WDK KMDF
ms.date: 04/20/2017
---

# Using Power-Managed I/O Queues


When a driver creates an I/O queue, it can specify whether the queue is *power-managed*. When I/O requests are available in a power-managed queue, the framework delivers the requests to the driver only if the device is in its working (D0) state. The framework does not allow the device to leave its working state until all I/O requests that the framework has delivered from the power-managed queue to the driver have been completed, canceled, or postponed.

For more information about power-managed I/O queues, see [Power Management for I/O Queues](power-management-for-i-o-queues.md).

## Callback functions for Power-Managed Queues


If your driver uses power-managed I/O queues, it can provide two additional callback functions:

<a href="" id="---------evtiostop"></a>[*EvtIoStop*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop)  
The [*EvtIoStop*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop) callback function stops processing a specified I/O request. When the device leaves its working (D0) state or is removed, the framework calls an I/O queue's *EvtIoStop* callback function once for every I/O request that the driver has not [completed](completing-i-o-requests.md), including requests that the driver [owns](request-ownership.md) and those that it has [forwarded](forwarding-i-o-requests.md) to an I/O target.

<a href="" id="---------evtioresume"></a>[*EvtIoResume*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_resume)  
The [*EvtIoResume*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_resume) callback function resumes processing a previously stopped I/O request. The framework calls an I/O queue's *EvtIoResume* callback function when it resumes delivering I/O requests to the driver from the queue, after the device has returned to its working state.

Each time the framework calls a driver's [*EvtIoStop*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop) callback function, the function typically [completes](completing-i-o-requests.md) or [cancels](canceling-i-o-requests.md) the I/O request, or calls [**WdfRequestStopAcknowledge**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequeststopacknowledge) to return ownership of the request to the framework.

While doing so is optional, you should in general provide an [*EvtIoStop*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop) callback function for a power-managed queue. By providing *EvtIoStop*, your driver can help to shorten the time that elapses before your device, and possibly the system, enters a low-power state.

If you do not provide [*EvtIoStop*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop) for a power-managed queue, the framework waits until all requests delivered from the power-managed queue to the driver are complete before moving the device (or system) to a lower power state or removing the device. Potentially, this inaction can prevent a system from entering its hibernation state or another low system power state. In extreme cases, it can cause the system to crash with bugcheck code 9F.

If your driver does not forward requests to an I/O target and does not hold requests for an indeterminate time, you could safely omit [*EvtIoStop*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop) for a power-managed queue.

## Waiting for Dispatcher Objects


In general, drivers should only use dispatcher objects as synchronization mechanisms within a nonarbitrary thread context.

Because [request handlers](request-handlers.md) run in an arbitrary thread context, a request handler for a power-managed queue must not wait for kernel dispatcher objects to be set. Doing so may result in deadlock.

For more information about when a driver can wait for dispatcher objects, and what to do when it can't, see [Introduction to Kernel Dispatcher Objects](../kernel/introduction-to-kernel-dispatcher-objects.md).

 

