---
title: Accessing Data Buffers in WDF Drivers (KMDF or UMDF)
description: When a Windows Driver Frameworks (WDF) driver receives a read, write, or device I/O control request, the request object contains either an input buffer, an output buffer, or both.
ms.assetid: ceba2279-b0fb-4261-b439-723d5dad967b
keywords:
- request processing WDK KMDF , data buffers
- data buffers WDK KMDF
- input buffers WDK KMDF
- output buffers WDK KMDF
- buffers WDK KMDF
- buffered I/O WDK KMDF
- direct I/O WDK KMDF
- neither buffered nor direct I/O WDK KMDF
- I/O requests WDK KMDF , data buffers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Data Buffers in WDF Drivers (KMDF or UMDF)


When a Windows Driver Frameworks (WDF) driver receives a read, write, or device I/O control request, the request object contains either an input buffer, an output buffer, or both.

Input buffers contain information that the driver needs. For write requests, this information is typically data that a function driver must send to a device. For device I/O control requests, an input buffer might contain information that indicates the type of operation that the driver must perform.

Output buffers receive information from the driver. For read requests, this information is typically data that a function driver receives from a device. For device I/O control requests, an output buffer might receive status or other information that was specified by the request's I/O control code.

The technique that your driver uses to access a request's data buffers depends on the driver's method for accessing data buffers for a device. There are three access methods:

-   [Buffered I/O](#buffered). The I/O manager creates intermediate buffers that it shares with the driver.
-   [Direct I/O](#direct). The I/O manager locks the buffer space into physical memory, and then provides the driver with direct access to the buffer space.
-   [Neither buffered nor direct I/O](#neither). The I/O manager provides the driver with the virtual addresses of the request's buffer space. The I/O manager does not validate the request's buffer space, so the driver must verify that the buffer space is accessible and lock the buffer space into physical memory.

A Kernel-Mode Driver Framework (KMDF) driver can use any of the three access methods. A User-Mode Driver Framework (UMDF) driver can use buffered or direct I/O for read, write, and IOCTL requests, and can [convert requests that specify the **METHOD\_NEITHER** method](managing-buffer-access-methods-in-umdf-drivers.md#using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers).

## <a href="" id="ddk-preprocessing-i-o-requests-df"></a>Specifying Buffer Access Method


<a href="" id="kmdf-drivers"></a>**KMDF Drivers**  

For read and write requests, all drivers in a driver stack must use the same method for accessing a device's buffers, except for the highest-level driver, which can use the "neither" method, regardless of which method is used by lower drivers.

Starting in version 1.13, a KMDF driver specifies the access method for all of a device's read and write requests by calling [**WdfDeviceInitSetIoTypeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265604) for each device. For example, if a driver specifies the buffered I/O method for one of its devices, the I/O manager uses the buffered I/O method when delivering read and write requests to the driver for that device.

For device I/O control requests, the I/O control code (IOCTL) contains bits that specify the buffer access method. As a result, a KMDF driver does not need to take any action to select a buffering method for IOCTLs. For more information about IOCTLs, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023). Unlike read and write requests, all of a device's IOCTLs do not have to specify the same access method.

<a href="" id="umdf-drivers"></a>**UMDF Drivers**  

A UMDF driver specifies *preferences* for the access method that the framework uses for read and write requests, as well as device I/O control requests. The values that a UMDF driver provides are only preferences, and are not guaranteed to be used by the framework. For more information, see [Managing Buffer Access Methods in UMDF Drivers](managing-buffer-access-methods-in-umdf-drivers.md).

A UMDF driver specifies the access method for all of a device's read, write and IOCTL requests by calling [**WdfDeviceInitSetIoTypeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265604) for each device. For example, if a driver specifies the buffered I/O method for one of its devices, the framework uses the buffered I/O method when delivering read, write and IOCTL requests to the driver for that device.

Note the difference in buffer access technique for IOCTLs between KMDF and UMDF. KMDF drivers do not specify buffer access method for IOCTLs, whereas UMDF drivers do specify the buffer access method for IOCTLs.

If a WDF driver describes an I/O request's buffer by using a technique that is incorrect for the I/O method that an I/O target uses, the framework corrects the buffer description. For example, if a driver uses an MDL to describe a buffer that it passes to [**WdfIoTargetSendReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548669), and if the I/O target uses buffered I/O (which requires that buffers be specified using virtual addresses instead of MDLs), the framework converts the buffer description from an MDL to a virtual address and length. However, it is more efficient if your driver specifies buffers in the correct format.

For information about framework memory objects, lookaside lists, MDLs, and local buffers, see [Using Memory Buffers](using-memory-buffers.md).

For information about when memory buffers are deleted, see [Memory Buffer Life Cycle](memory-buffer-life-cycle.md).

## <a href="" id="buffered"></a> Accessing Data Buffers for Buffered I/O


If your driver is using buffered I/O, its behavior changes depending on the type of data request and whether it's using KMDF or UMDF.

<a href="" id="kmdf-drivers"></a>**KMDF Drivers**  

When a KMDF driver uses buffered I/O, the I/O manager creates one intermediate buffer that the driver can access for every type of request. Here's what happens:

-   Write requests. The I/O manager transfers input info from the calling app's input buffer before it calls the driver stack. Then, the KMDF driver reads input info from the intermediate buffer and writes it to the device.
-   Read requests. The KMDF driver reads info from the device and stores it in the intermediate buffer. Then, the I/O manager copies the output data from the intermediate buffer to the app's output buffer.
-   Device I/O control requests. The KMDF driver reads or writes data for that request to or from the intermediate buffer.

<a href="" id="umdf-drivers"></a>**UMDF Drivers**  

When a UMDF driver uses buffered I/O, the driver host process creates one or two intermediate buffers, depending on the type of request. Here's what happens:

-   Write requests. The framework creates one buffer, transfers input info from the calling app's input buffer, and then calls the driver stack. The UMDF driver reads input info from the intermediate buffer and writes it to the device.
-   Read requests. A UMDF driver reads info from a device and stores it in a buffer that the framework created. The driver host process copies the output data from the intermediate buffer to the app's output buffer.
-   Device I/O control requests. The framework creates two buffers corresponding to input and output buffers of the IOCTL that the driver can access. The framework copies the input info from the IOCTL into the new intermediate buffer and makes it available to the driver. The framework does not copy the contents of the output buffer, so the driver shouldn't attempt to read from it (otherwise it will end up reading garbage data). Any data that the driver writes to the output buffer is copied back into the original IOCTL buffer and is returned to the app upon successful completion of the I/O request. Note that any data that the driver writes to the input buffer is discarded and not returned to the calling app.

To retrieve a handle to a framework memory object that represents the buffer, both KMDF and UMDF drivers call [**WdfRequestRetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550015) or [**WdfRequestRetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550019), depending on whether this is a read or write request. The driver can then retrieve a pointer to the buffer by calling [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715). To read and write the buffer, the driver calls [**WdfMemoryCopyFromBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548701) or [**WdfMemoryCopyToBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548703).

To retrieve the virtual address and length of the buffer, the driver calls [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014) or [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018).

To allocate and build a memory descriptor list (MDL) for the buffer, a KMDF driver calls [**WdfRequestRetrieveInputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550016) or [**WdfRequestRetrieveOutputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550021).

## <a href="" id="direct"></a> Accessing Data Buffers for Direct I/O


<a href="" id="kmdf-drivers"></a>**KMDF Drivers**  

If your driver is using direct I/O, the I/O manager verifies the accessibility of the buffer space that the originator of the I/O request (typically a user-mode application) specified, locks the buffer space into physical memory, and then provides the driver with direct access to the buffer space.

<a href="" id="umdf-drivers"></a>**UMDF Drivers**  

If your driver has specified a preference for direct I/O, and all the UMDF requirements for direct I/O have been met (see [Managing Buffer Access Methods in UMDF Drivers](managing-buffer-access-methods-in-umdf-drivers.md)), the framework maps the memory buffer it receives from the I/O manager directly into the driver's host process address space, and thus provides the driver with direct access to the buffer space.

To retrieve a handle to a framework memory object that represents the buffer space, the driver calls [**WdfRequestRetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550015) or [**WdfRequestRetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550019). The driver can then retrieve a pointer to the buffer by calling [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715). To read and write the buffer, the driver calls [**WdfMemoryCopyFromBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548701) or [**WdfMemoryCopyToBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548703).

To retrieve the virtual address and length of the buffer space, the driver calls [**WdfRequestRetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550014) or [**WdfRequestRetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550018).

If a device's drivers are using direct I/O, the I/O manager describes buffers by using MDLs. To retrieve a pointer to a buffer's MDL, a KMDF driver calls [**WdfRequestRetrieveInputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550016) or [**WdfRequestRetrieveOutputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550021). A UMDF driver cannot access MDLs.

## <a href="" id="neither"></a> Accessing Data Buffers for Neither Buffered Nor Direct I/O


<a href="" id="kmdf-drivers"></a>**KMDF Drivers**  

If your driver is using the buffer access method known as the *neither buffered I/O nor direct I/O method* (or, the "neither" method, for short), the I/O manager simply provides the driver with the virtual addresses that the originator of the I/O request specified for the request's buffer space. The I/O manager does not validate the I/O request's buffer space, so the driver must verify that the buffer space is accessible and lock the buffer space into physical memory.

The virtual addresses that the I/O manager provides can be accessed only in the process context of the originator of the I/O request. Only the highest-level driver in the driver stack is guaranteed to execute in the originator's process context.

To obtain access to an I/O request's buffer space, the highest-level driver must provide an [*EvtIoInCallerContext*](https://msdn.microsoft.com/library/windows/hardware/ff541764) callback function. The framework calls this callback function each time it receives an I/O request for the driver.

If a request's buffer access method is "neither," a KMDF driver must do the following for each buffer:

1.  Call [**WdfRequestRetrieveUnsafeUserInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550022) or [**WdfRequestRetrieveUnsafeUserOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff550024) to obtain the buffer's virtual address.

2.  Call [**WdfRequestProbeAndLockUserBufferForRead**](https://msdn.microsoft.com/library/windows/hardware/ff549987) or [**WdfRequestProbeAndLockUserBufferForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff549989) to probe and lock the buffer and to obtain a handle to a framework memory object for the buffer.

3.  Save the memory object handles in the request's [context space](using-request-object-context.md).

4.  Call [**WdfDeviceEnqueueRequest**](https://msdn.microsoft.com/library/windows/hardware/ff545945), which returns the request to the framework.

The framework subsequently adds the request to one of the driver's I/O queues. If the driver has provided [request handlers](request-handlers.md), the framework will eventually call the appropriate request handler.

The request handler can retrieve the request's memory object handles from the request's context space. The driver can pass the handles to [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715) to obtain the buffer's address.

Occasionally, a highest-level driver must use the preceding steps to access a user-mode buffer, even if the driver is not using the "neither" access method. For example, suppose the driver is using buffered I/O. An I/O control code that uses the buffered access method might pass a structure that contains an embedded pointer to a user-mode buffer. In such a case, the driver must provide an [*EvtIoInCallerContext*](https://msdn.microsoft.com/library/windows/hardware/ff541764) callback function that extracts the pointers from the structure and then uses the preceding steps 2 through 4.

<a href="" id="umdf-drivers"></a>**UMDF Drivers**  

UMDF doesn't support neither buffered nor direct I/O type buffers, so a UMDF driver never needs to handle this type of buffer directly.

However, if the framework receives such buffers for read or write from the I/O manager, it makes them available to a UMDF driver as buffered I/O or direct I/O, depending on the access method selected by the driver. If the framework receives an IOCTL specifying the "neither" buffer method, it can optionally convert the buffer access method of the IOCTL request to buffered I/O or direct I/O based on the presence of an INF directive. See [Managing Buffer Access Methods in UMDF Drivers](managing-buffer-access-methods-in-umdf-drivers.md) for more info.

 

 





