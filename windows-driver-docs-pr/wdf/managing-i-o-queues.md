---
title: Managing I/O Queues
description: Managing I/O Queues
keywords:
- I/O queues WDK KMDF , starting
- I/O queues WDK KMDF , stopping
- I/O queues WDK KMDF , restarting
- I/O queues WDK KMDF , adding requests
- I/O queues WDK KMDF , obtaining requests
- I/O queues WDK KMDF , searching requests
- I/O queues WDK KMDF , purging
- I/O queues WDK KMDF , draining
- I/O queues WDK KMDF , moving requests
- I/O queues WDK KMDF , intercepting requests
- I/O queues WDK KMDF , properties
- intercepting I/O requests WDK KMDF
- moving I/O requests WDK KMDF
- relocating I/O requests WDK KMDF
- searching I/O requests WDK KMDF
- requeuing I/O requests WDK KMDF
- stopping I/O queues WDK KMDF
- restarting I/O queues WDK KMDF
- starting I/O queues WDK KMDF
- dispatching methods WDK KMDF
ms.date: 04/20/2017
---

# Managing I/O Queues


## <a href="" id="starting-an-i-o-queue"></a> Starting an I/O Queue


When a driver calls [**WdfIoQueueCreate**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuecreate) to create an I/O queue, the framework automatically enables the queue to receive I/O requests and to deliver them to a driver.

Drivers typically call [**WdfIoQueueCreate**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuecreate) from within an [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function. The framework can begin delivering I/O requests to the driver after the driver's *EvtDriverDeviceAdd* callback function returns.

If your driver is using [power-managed](using-power-managed-i-o-queues.md) I/O queues, the framework cannot begin delivering requests to your driver until the device enters its working state and the framework has called the driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function.

## <a href="" id="stopping-and-restarting-an-i-o-queue"></a> Stopping and Restarting an I/O Queue


Your driver can call [**WdfIoQueueStop**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestop) or [**WdfIoQueueStopSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopsynchronously) to temporarily prevent the framework from delivering I/O requests from an I/O queue. To resume delivery of I/O requests, the driver calls [**WdfIoQueueStart**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestart).

If your driver uses power-managed I/O queues, the framework automatically stops a device's queues when the device leaves its working (D0) state, and the framework restarts the queues when the device state returns to D0.

## <a href="" id="adding-requests-to-an-i-o-queue"></a> Adding Requests to an I/O Queue


When the system sends a read, write, or device I/O control request to a driver, the framework places the request in an I/O queue. The driver can control the types of requests that the framework stores in each queue by calling [**WdfDeviceConfigureRequestDispatching**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceconfigurerequestdispatching).

A driver can also requeue requests that it has received from the framework, by calling [**WdfRequestForwardToIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoioqueue).

## <a href="" id="obtaining-requests-from-an-i-o-queue"></a> Obtaining Requests from an I/O Queue


If a driver specifies the sequential or the parallel [dispatching method](dispatching-methods-for-i-o-requests.md) for an I/O queue, it receives requests in [request handlers](request-handlers.md).

If a driver specifies the manual or sequential dispatching method, it can obtain requests by calling [**WdfIoQueueRetrieveNextRequest**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueueretrievenextrequest) or [**WdfIoQueueRetrieveRequestByFileObject**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueueretrieverequestbyfileobject).

## <a href="" id="searching-for-an-i-o-request"></a> Searching for an I/O Request


If a driver specifies the manual [dispatching method](dispatching-methods-for-i-o-requests.md) for an I/O queue, it can use the following steps to search for particular requests in the queue:

1.  Call [**WdfIoQueueFindRequest**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuefindrequest) to locate a request that matches driver-specified criteria.

2.  Call [**WdfIoQueueRetrieveFoundRequest**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueueretrievefoundrequest) to retrieve the request that [**WdfIoQueueFindRequest**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuefindrequest) located.

## <a href="" id="purging-or-draining-an-i-o-queue"></a> Purging or Draining an I/O Queue


*Purging* an I/O queue means stopping insertion of I/O requests into the queue and canceling any requests that are already in the queue.

*Draining* an I/O queue means stopping insertion of I/O requests into the queue, while allowing any requests that are already in the queue to be delivered to the driver.

Drivers typically purge or drain their queues only if the queues are not power-managed. For power-managed I/O queues, drivers can provide [*EvtIoStop*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop) and [*EvtIoResume*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_resume) callback functions.

If some of your driver's queues are not power-managed, you might want to purge or drain a queue if its associated device or I/O channel becomes unavailable. Typically, you will purge, instead of drain, a queue unless there is a high likelihood that each request contains very important information. For example, a driver for a network device might purge its queues, while a driver for a storage device would likely drain its queues.

If you want your driver to purge or drain an I/O queue, the driver can call one of the following queue object methods:

-   [**WdfIoQueuePurge**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurge) or [**WdfIoQueuePurgeSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurgesynchronously), to stop queuing I/O requests to an I/O queue and to cancel unprocessed requests.

-   [**WdfIoQueueDrain**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrain) or [**WdfIoQueueDrainSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrainsynchronously), to stop queuing I/O requests to an I/O queue while allowing already-queued requests to be delivered and processed.

Exercise caution when calling [**WdfIoQueueDrain**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrain) and [**WdfIoQueueDrainSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrainsynchronously). Because a drain operation waits for requests to be completed, you should only drain a queue if you are certain that the queue's pending requests will complete in a timely fashion. If you do not know how long I/O requests will take to complete and it is acceptable to cancel outstanding requests, consider purging the queue.

## <a href="" id="moving-requests-from-one-i-o-queue-to-another"></a> Moving Requests from One I/O Queue to Another


After your driver has received an I/O request, you might want the driver to requeue the request into a different I/O queue. To do this, the driver calls [**WdfRequestForwardToIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoioqueue) or [**WdfRequestForwardToParentDeviceIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoparentdeviceioqueue), which adds the request to the tail of a specified queue. Eventually, the framework will deliver the request to the driver again by using the specified queue's dispatching method. For more information about moving I/O requests from one I/O queue to another, see [Requeuing I/O Requests](requeuing-i-o-requests.md).

## <a href="" id="intercepting-an-i-o-request-before-it-is-queued"></a> Intercepting an I/O Request before it is Queued


It is possible for a driver to intercept an I/O request before the framework places the request in an I/O queue. To intercept I/O requests, the driver must call [**WdfDeviceInitSetIoInCallerContextCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetioincallercontextcallback) to register an [*EvtIoInCallerContext*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_io_in_caller_context) callback function.

The framework associates the [*EvtIoInCallerContext*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_io_in_caller_context) callback function with a device. As a result, the framework calls the *EvtIoInCallerContext* callback function every time it receives a request that the system is sending to the device.

Typically, when an [*EvtIoInCallerContext*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_io_in_caller_context) callback function receives a request, it performs some preliminary processing for the request. Next, the callback function calls [**WdfDeviceEnqueueRequest**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceenqueuerequest), which gives the request back to the framework. The framework can then place the request in the proper I/O queue, just as it would have if it had not called the *EvtIoInCallerContext* callback function.

The primary reason that a driver might provide an [*EvtIoInCallerContext*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_io_in_caller_context) callback function is that the driver has to handle I/O operations that support the I/O method called [neither buffered nor direct I/O](./accessing-data-buffers-in-wdf-drivers.md#neither). For this I/O method, the driver must access received buffers in the process context of the originator of the I/O request. For more information, see [Accessing Data Buffers in Framework-Based Drivers](./accessing-data-buffers-in-wdf-drivers.md).

## <a href="" id="obtaining-i-o-queue-properties"></a> Obtaining I/O Queue Properties


To obtain properties of a framework queue object, the driver can call the following methods:

-   [**WdfIoQueueGetDevice**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuegetdevice), to obtain a handle to the device object that the queue object belongs to.

-   [**WdfIoQueueGetState**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuegetstate), to obtain [state information](i-o-queue-states.md) about the queue.

 

