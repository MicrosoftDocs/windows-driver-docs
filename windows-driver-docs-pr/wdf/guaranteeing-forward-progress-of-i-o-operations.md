---
title: Guaranteeing Forward Progress of I/O Operations
description: Guaranteeing Forward Progress of I/O Operations
ms.assetid: e230eb3b-54ac-43b1-ac2b-8fa137cee43e
keywords:
- guaranteed forward progress WDK KMDF
- forward progress, guaranteed WDK KMDF
- low-memory situations WDK KMDF
- I/O queues WDK KMDF , guaranteed forward progress
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Guaranteeing Forward Progress of I/O Operations


Some drivers, such as storage drivers for the system's paging device, must perform at least some of their supported I/O operations without failure, to avoid losing critical system data. One potential cause of a driver failure is a low-memory situation. If the framework or the driver cannot allocate enough memory to handle an I/O request, one or the other might have to fail the I/O request by [completing](completing-i-o-requests.md) it with an error status value.

In versions of KMDF prior to version 1.9, the framework always fails an I/O request if it cannot allocate a framework request object for an I/O request packet (IRP) that the I/O manager has sent to the driver. To provide drivers the ability to process I/O requests during low-memory situations, versions 1.9 and later of the framework provide a *guaranteed forward progress* capability for I/O queues.

This capability enables the framework and the driver to pre-allocate memory for sets of request objects and request-related driver context buffers, respectively. The framework and driver use this pre-allocated memory only when the amount of system memory is low.

### Features of Guaranteed Forward Progress

By using the framework's guaranteed forward progress for I/O queues, a driver can:

-   Ask the framework to pre-allocate a set of request objects to use with a specific I/O queue during low-memory situations.

-   Provide a callback function that pre-allocates request-specific resources that the driver can use when it receives pre-allocated request objects from the framework during low-memory situations.

-   Provide another callback function that allocates driver-specific resources for an I/O request when a low-memory situation has *not* been detected. If this callback function's allocation fails because of a low-memory situation, it can indicate whether the framework should use one of its pre-allocated request objects.

-   Specify which I/O requests require the use of pre-allocated request objects. Options include using pre-allocated objects for all IRPs, using them only if a paging I/O operation is in progress, or having an additional driver callback function examine each IRP to determine whether to use a pre-allocated object.

If your driver implements guaranteed forward progress for one or more of its I/O queues, the driver will be better able to successfully [process I/O requests](processing-i-o-requests.md) during low-memory situations. You can implement guaranteed forward progress for a device's default I/O queue, and for any I/O queue that your driver configures by calling [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920).

The framework's guaranteed forward progress capability works for your driver only if both your driver and the driver's [I/O targets](using-i-o-targets.md) implement guaranteed forward progress. In other words, if a driver implements guaranteed forward progress for a device, all lower-level drivers in the device's driver stack must also implement guaranteed forward progress.

### Enabling Guaranteed Forward Progress for an I/O Queue

To enable guaranteed forward progress for an I/O queue, your driver initializes a [**WDF\_IO\_QUEUE\_FORWARD\_PROGRESS\_POLICY**](https://msdn.microsoft.com/library/windows/hardware/ff552364) structure and then calls the [**WdfIoQueueAssignForwardProgressPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547395) method. If the driver calls [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920) to configure an I/O queue, it must do so before it calls **WdfIoQueueAssignForwardProgressPolicy**.

When the driver calls [**WdfIoQueueAssignForwardProgressPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547395), it can specify the following three event callback functions, all of which are optional:

<a href="" id="evtioallocateresourcesforreservedrequest"></a>[*EvtIoAllocateResourcesForReservedRequest*](https://msdn.microsoft.com/library/windows/hardware/ff541751)  
A driver's [*EvtIoAllocateResourcesForReservedRequest*](https://msdn.microsoft.com/library/windows/hardware/ff541751) callback function allocates and stores request-specific resources for request objects that the framework is reserving for low-memory situations.

The framework calls this callback function each time that it creates a reserved request object. The driver should allocate request-specific resources for one I/O request, typically by using the reserved request object's [context space](framework-object-context-space.md).

<a href="" id="evtioallocaterequestresources"></a>[*EvtIoAllocateRequestResources*](https://msdn.microsoft.com/library/windows/hardware/ff541747)  
A driver's [*EvtIoAllocateRequestResources*](https://msdn.microsoft.com/library/windows/hardware/ff541747) callback function allocates request-specific resources for immediate use. It is called immediately after the framework has received an IRP and created a request object for the IRP.

If the callback function's attempt to allocate resources fails, the callback function returns an error status value. The framework then deletes the newly created request object and uses one of its reserved request objects. In turn, the driver's [request handler](request-handlers.md) uses request-specific resources that its [*EvtIoAllocateRequestResources*](https://msdn.microsoft.com/library/windows/hardware/ff541747) callback function previously allocated.

<a href="" id="evtiowdmirpforforwardprogress"></a>[*EvtIoWdmIrpForForwardProgress*](https://msdn.microsoft.com/library/windows/hardware/ff541808)  
A driver's [*EvtIoWdmIrpForForwardProgress*](https://msdn.microsoft.com/library/windows/hardware/ff541808) callback function examines an IRP and tells framework whether to use a reserved request object for the IRP or to fail the I/O request by completing it with an error status value.

The framework calls this callback function only if the framework is unable to create a new request object and you have indicated (by setting a flag in the driver's [**WDF\_IO\_QUEUE\_FORWARD\_PROGRESS\_POLICY**](https://msdn.microsoft.com/library/windows/hardware/ff552364) structure) that you want the driver to examine IRPs during low-memory situations. In other words, your driver can assess each IRP and decide if it is one that must be processed even during low-memory situations.

When your driver calls [**WdfIoQueueAssignForwardProgressPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547395), it also specifies the number of reserved request objects that you want the framework to pre-allocate for low-memory situations. You can choose the number of request objects that are appropriate for your device and driver. To prevent reduced performance, your driver should typically specify a number that approximates the number of I/O requests that the driver and device can handle in parallel.

However, if your driver's call to [**WdfIoQueueAssignForwardProgressPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547395) and its [*EvtIoAllocateResourcesForReservedRequest*](https://msdn.microsoft.com/library/windows/hardware/ff541751) callback function pre-allocate too many reserved request objects or too much request-specific resource memory, your driver can actually contribute to the low-memory situations that you are attempting to handle. You should test the performance of your driver and device, and include low-memory simulations, to determine the best numbers to choose.

Before [**WdfIoQueueAssignForwardProgressPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547395) returns, the framework creates and reserves the number of request objects that the driver has specified. Each time that it reserves a request object, the framework immediately calls the driver's [*EvtIoAllocateResourcesForReservedRequest*](https://msdn.microsoft.com/library/windows/hardware/ff541751) callback function so that the driver can allocate and save request-specific resources, in case the framework actually uses the reserved request objects.

When one of the driver's [request handlers](request-handlers.md) receives an I/O request from the I/O queue, it can call the [**WdfRequestIsReserved**](https://msdn.microsoft.com/library/windows/hardware/ff549980) method to determine whether the request object is one that the framework pre-allocated for low-memory situations. If this method returns **TRUE**, the driver should use resources that its [*EvtIoAllocateResourcesForReservedRequest*](https://msdn.microsoft.com/library/windows/hardware/ff541751) callback function reserved.

If the framework uses one of its reserved request objects, it returns the object to its set of reserved objects after the driver completes the request. The framework saves the request object, and any context space that the driver created by calling [**WdfDeviceInitSetRequestAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff546786) or [**WdfObjectAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff548723), for reuse if another low-memory situation occurs.

### How the Framework and Driver Support Guaranteed Forward Progress

Following are the steps that the driver and framework perform to support guaranteed forward progress for an I/O queue:

1.  The driver calls [**WdfIoQueueAssignForwardProgressPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547395).

    In response, the framework allocates and stores the number of request objects that the driver specifies. If the driver previously called [**WdfDeviceInitSetRequestAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff546786), each allocation includes context space that **WdfDeviceInitSetRequestAttributes** specified.

    In addition, if the driver has provided an [*EvtIoAllocateResourcesForReservedRequest*](https://msdn.microsoft.com/library/windows/hardware/ff541751) callback function, the framework calls the callback function each time that it allocates and stores a request object.

2.  The framework receives an I/O request packet (IRP) that the I/O manager is sending to the driver.

    The framework attempts to allocate a request object for the IRP. If the I/O queue that the driver created for the request type supports guaranteed forward progress, the next step depends on whether the allocation succeeds or fails:

    -   The request object allocation succeeds.

        If the driver provided an [*EvtIoAllocateRequestResources*](https://msdn.microsoft.com/library/windows/hardware/ff541747) callback function, the framework calls it. If the callback function returns STATUS\_SUCCESS, the framework adds the request to the I/O queue. If the callback function returns an error status value, the framework deletes the request object that it just created and uses one of its pre-allocated request objects. When the driver's request handler receives the request object, it determines whether the request object was pre-allocated and therefore whether it should use the driver's pre-allocated resources.

        If the driver did *not* provide an [*EvtIoAllocateRequestResources*](https://msdn.microsoft.com/library/windows/hardware/ff541747) callback function, the framework adds the request to the I/O queue, just as if the driver had not enabled guaranteed forward progress.

    -   The request object allocation fails.

        What the framework does next depends on the value that the driver provided for the **ForwardProgressReservedPolicy** member of the [**WDF\_IO\_QUEUE\_FORWARD\_PROGRESS\_POLICY**](https://msdn.microsoft.com/library/windows/hardware/ff552364) structure. This member informs the framework when to use a reserved request: always, only if the I/O request is a paging I/O operation, or only if the [*EvtIoWdmIrpForForwardProgress*](https://msdn.microsoft.com/library/windows/hardware/ff541808) callback function indicates that a reserved request should be used.

    In all cases, the driver's request handlers can call [**WdfRequestIsReserved**](https://msdn.microsoft.com/library/windows/hardware/ff549980) to determine whether the framework has used a reserved request object. If so, the driver should use the request resources that its [*EvtIoAllocateResourcesForReservedRequest*](https://msdn.microsoft.com/library/windows/hardware/ff541751) callback function allocated.

### Guaranteed Forward Progress Scenario

You are writing a driver for a storage device that might contain the system's paging file. It is important that read operations from and write operations to the paging file succeed.

You decide to create separate I/O queues for read and write operations, and to enable guaranteed forward progress for both of these I/O queues. You decide to create a third I/O queue for all other request types without enabling guaranteed forward progress.

Your driver stack and device are capable of processing four write operations in parallel, so you set the **TotalForwardProgressRequests** member of the [**WDF\_IO\_QUEUE\_FORWARD\_PROGRESS\_POLICY**](https://msdn.microsoft.com/library/windows/hardware/ff552364) structure to 4 before calling [**WdfIoQueueAssignForwardProgressPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff547395).

You decide that guaranteeing forward progress is only important if your driver's device is the paging device, so your driver sets the **ForwardProgressReservedPolicy** member of the WDF\_IO\_QUEUE\_FORWARD\_PROGRESS\_POLICY structure to [**WdfIoForwardProgressReservedPolicyPagingIO**](https://msdn.microsoft.com/library/windows/hardware/ff552357).

Because your driver requires a framework memory object for each read request and each write request, you decide that your driver should pre-allocate some memory objects to use for its calls to [**WdfIoTargetFormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff548612) and [**WdfIoTargetFormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff548620) in low-memory situations.

Therefore, the driver provides an [*EvtIoAllocateResourcesForReservedRequest*](https://msdn.microsoft.com/library/windows/hardware/ff541751) callback function for the read queue and another one for the write queue. Each time that the framework calls one of these callback functions, the callback function calls [**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706) and saves the returned object handle for low-memory situations. Because the callback function receives a handle to a pre-allocated request object, it can parent the memory object to the request object. (A driver for a DMA device might also pre-allocate [framework DMA objects](framework-dma-objects.md).)

The [request handlers](request-handlers.md) for the read and write queues must determine whether each received request object is one that the framework reserved for low-memory situations. A request handler can call [**WdfRequestIsReserved**](https://msdn.microsoft.com/library/windows/hardware/ff549980), or it can compare the request object handle with the ones that the [*EvtIoAllocateResourcesForReservedRequest*](https://msdn.microsoft.com/library/windows/hardware/ff541751) callback function received previously.

The driver also provides an [*EvtIoAllocateRequestResources*](https://msdn.microsoft.com/library/windows/hardware/ff541747) callback function for the read queue and another one for the write queue. The framework calls one of these callback functions when it receives a read or write request from the I/O manager and successfully creates a request object. Each of these callback functions calls [**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706) to allocate a memory object for a request. If the allocation fails, the callback function returns an error status value to notify the framework that a low-memory situation has just occurred. The framework, detecting the error return value, deletes the request object that it just created and uses one of its pre-allocated objects.

This driver does not provide an [*EvtIoWdmIrpForForwardProgress*](https://msdn.microsoft.com/library/windows/hardware/ff541808) callback function, because it does not need to examine individual read or write IRPs before the framework adds them to an I/O queue.

Remember that when a driver implements guaranteed forward progress for a device, all lower-level drivers in the device's driver stack must also implement guaranteed forward progress.

 

 





