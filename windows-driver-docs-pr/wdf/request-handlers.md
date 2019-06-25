---
title: Request Handlers
description: Request Handlers
ms.assetid: bfc543bf-18a8-4e2c-ba7a-d0a21cefb038
keywords:
- I/O queues WDK KMDF , creating
- I/O queues WDK KMDF , request handlers
- request handlers WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Request Handlers





If your driver has specified either the sequential or the parallel [dispatching method](dispatching-methods-for-i-o-requests.md) for an I/O queue, the framework calls a driver-supplied callback function each time it is ready to deliver one of the queue's requests to the driver.

For each I/O queue, the driver can provide one or more of the following callback functions, which are called *request handlers*:

<a href="" id="evtioread"></a>[*EvtIoRead*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_read)  
The framework calls an I/O queue's [*EvtIoRead*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_read) callback function when a read request is available in the queue.

<a href="" id="evtiowrite"></a>[*EvtIoWrite*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_write)  
The framework calls an I/O queue's [*EvtIoWrite*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_write) callback function when a write request is available in the queue.

<a href="" id="evtiodevicecontrol"></a>[*EvtIoDeviceControl*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_device_control)  
The framework calls an I/O queue's [*EvtIoDeviceControl*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_device_control) callback function when a device I/O control request is available in the queue.

<a href="" id="evtiointernaldevicecontrol"></a>[*EvtIoInternalDeviceControl*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_internal_device_control)  
The framework calls an I/O queue's [*EvtIoInternalDeviceControl*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_internal_device_control) callback function when an internal device I/O control request is available in the queue.

<a href="" id="evtiodefault"></a>[*EvtIoDefault*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_default)  
The framework calls an I/O queue's [*EvtIoDefault*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nc-wdfio-evt_wdf_io_queue_io_default) callback function when any request is available, if the driver has not supplied the associated request-type-specific callback function.

The driver registers callback functions when it calls [**WdfIoQueueCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nf-wdfio-wdfioqueuecreate) to create an I/O queue for a device.

Each of these callback functions receives two input arguments: a handle to the I/O request that the framework is delivering to the driver and a handle to the I/O queue that held the request. A callback function can determine the target device by calling [**WdfIoQueueGetDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfio/nf-wdfio-wdfioqueuegetdevice).

The framework calls your driver's request handlers in an arbitrary thread context. A driver should not wait for an extended period of time while executing in an arbitrary thread context. In some cases, your driver might use kernel dispatcher objects as synchronization mechanisms. For information about when your driver can wait for dispatcher objects, and what to do when it can't, see [Introduction to Kernel Dispatcher Objects](https://docs.microsoft.com/windows-hardware/drivers/kernel/introduction-to-kernel-dispatcher-objects).

 

 





