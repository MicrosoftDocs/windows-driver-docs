---
title: Request Handlers
author: windows-driver-content
description: Request Handlers
ms.assetid: bfc543bf-18a8-4e2c-ba7a-d0a21cefb038
keywords: ["I/O queues WDK KMDF , creating", "I/O queues WDK KMDF , request handlers", "request handlers WDK KMDF"]
---

# Request Handlers


## <a href="" id="ddk-i-o-queue-event-callbacks-df"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Request%20Handlers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




