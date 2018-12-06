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

<a href="" id="evtioread"></a>[*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776)  
The framework calls an I/O queue's [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776) callback function when a read request is available in the queue.

<a href="" id="evtiowrite"></a>[*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813)  
The framework calls an I/O queue's [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813) callback function when a write request is available in the queue.

<a href="" id="evtiodevicecontrol"></a>[*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758)  
The framework calls an I/O queue's [*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758) callback function when a device I/O control request is available in the queue.

<a href="" id="evtiointernaldevicecontrol"></a>[*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768)  
The framework calls an I/O queue's [*EvtIoInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback function when an internal device I/O control request is available in the queue.

<a href="" id="evtiodefault"></a>[*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757)  
The framework calls an I/O queue's [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) callback function when any request is available, if the driver has not supplied the associated request-type-specific callback function.

The driver registers callback functions when it calls [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) to create an I/O queue for a device.

Each of these callback functions receives two input arguments: a handle to the I/O request that the framework is delivering to the driver and a handle to the I/O queue that held the request. A callback function can determine the target device by calling [**WdfIoQueueGetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff547421).

The framework calls your driver's request handlers in an arbitrary thread context. A driver should not wait for an extended period of time while executing in an arbitrary thread context. In some cases, your driver might use kernel dispatcher objects as synchronization mechanisms. For information about when your driver can wait for dispatcher objects, and what to do when it can't, see [Introduction to Kernel Dispatcher Objects](https://msdn.microsoft.com/library/windows/hardware/ff548068).

 

 





