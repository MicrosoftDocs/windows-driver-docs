---
title: Accessing Data Buffers in UMDF 1.x Drivers
description: Accessing Data Buffers in UMDF 1.x Drivers
ms.assetid: cbd67ada-696e-403e-9b35-d8ed06a844d5
keywords:
- data buffers WDK UMDF
- buffers WDK UMDF
- request processing WDK UMDF , data buffers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Data Buffers in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

When a driver receives a read, write, or device I/O control request, the request object contains either an input buffer or an output buffer, or both. (A few device I/O control requests provide two input, two output, or two input/output buffers.)

Input buffers contain information that the driver needs. For write requests, typically this information is data that a function driver must send to a device. For device I/O control requests, an input buffer might contain information that indicates the type of operation that the driver must perform.

Output buffers receive information from the driver. For read requests, typically this information is data that a function driver receives from a device. For device I/O control requests, an output buffer might receive status or other information that the I/O control code of the request specified.

The technique that your driver uses to access a request's data buffers can depend on the driver's method for accessing data buffers for a device. UMDF supports the following buffer access methods:

-   UMDF versions prior to version 1.9 support only the [buffered I/O](#using-buffered-i-o-in-umdf-drivers) access method. UMDF-based drivers that run with those versions of UMDF can use only the buffered I/O method for all read, write, and device I/O control requests. To access an I/O request's data buffers, UMDF-based drivers must use the [**IWDFIoRequest::GetInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559100) and [**IWDFIoRequest::GetOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559112) object methods.

-   Beginning with UMDF version 1.9, two access methods: [buffered I/O](#using-buffered-i-o-in-umdf-drivers) and [direct I/O](#using-direct-i-o-in-umdf-drivers), are available to UMDF-based drivers. UMDF drivers that are written for UMDF versions 1.9 and later should use the [**IWDFIoRequest2::RetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559033), [**IWDFIoRequest2::RetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559037), [**IWDFIoRequest2::RetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559041), or [**IWDFIoRequest2::RetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559046) object methods to access data buffers.

A third access method, which is called [neither buffered nor direct I/O](#using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers), is not available to UMDF-based drivers, but UMDF can convert some I/O requests from the "neither" method to a method that the UMDF version supports.

In most cases, UMDF-based drivers call the same UMDF object methods to access data buffers, whether UMDF and the driver are using buffered I/O or direct I/O. Direct I/O often provides better performance than buffer I/O provides.

The following sections of this topic explain:

-   how to specify a [preferred buffer access method](#specifying-a-preferred-buffer-access-method) and [preferred buffer retrieval mode](#specifying-a-buffer-retrieval-mode)

-   how UMDF [chooses](#how-umdf-chooses-a-buffer-access-method-for-an-i-o-request) which buffer method and retrieval mode to use

-   how your driver can [obtain](#how-a-driver-can-obtain-the-access-method-for-an-i-o-request) the buffer access method that UMDF is using

-   guidelines for using the [buffered](#using-buffered-i-o-in-umdf-drivers), [direct](#using-direct-i-o-in-umdf-drivers), and [neither buffered nor direct](#using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers) buffer access methods

### <a href="" id="specifying-a-preferred-buffer-access-method"></a> Specifying a Preferred Buffer Access Method

UMDF versions 1.9 and later support both the buffered and direct I/O access methods. Drivers can specify the access method that you prefer to use for all of a device's read, write, and device I/O control requests by calling [**IWDFDeviceInitialize2::SetIoTypePreference**](https://msdn.microsoft.com/library/windows/hardware/ff556969) before calling [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) to create a device object. For example, if a driver specifies a preference for only the buffered I/O method for read and write requests for one of its devices, the [UMDF driver host process](umdf-driver-host-process.md) uses the buffered I/O method when it delivers read and write requests to the driver for that device. If a driver specifies a preference for direct I/O, UMDF can (but might not) use direct I/O. For more information about when UMDF uses direct I/O, see [How UMDF Chooses a Buffer Access Method for an I/O Request](#how-umdf-chooses-a-buffer-access-method-for-an-i-o-request).

For each device that a driver supports, the driver can specify a preference for buffered I/O, for direct I/O, or for either buffered or direct I/O for the device. The driver can specify one type of access method for read and write requests and another type of access method for device I/O control requests. If the driver does not specify an access method preference, UMDF uses the buffered method.

For device I/O control requests, the I/O control code (IOCTL) specifies the buffer access method. (For more information about how IOCTLs specify an access method, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023).) However, the access method that UMDF uses might not match the access method that the IOCTL specifies.

-   In UMDF versions prior to version 1.9, UMDF always uses the buffered access method for all I/O control requests.

-   UMDF versions 1.9 and later use the buffered I/O access method if the IOCTL specifies buffered I/O. If the IOCTL specifies direct I/O, and if the driver calls [**IWDFDeviceInitialize2::SetIoTypePreference**](https://msdn.microsoft.com/library/windows/hardware/ff556969) to indicate that a preference for direct I/O, UMDF might use direct I/O or it might use buffered I/O, as described in [How UMDF Chooses a Buffer Access Method for an I/O Request](#how-umdf-chooses-a-buffer-access-method-for-an-i-o-request). For information about how UMDF supports IOCTLs that specify the "neither buffered I/O nor direct I/O" method, see [Using Neither Buffered I/O nor Direct I/O in UMDF Drivers](#using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers).

### <a href="" id="specifying-a-buffer-retrieval-mode"></a> Specifying a Buffer Retrieval Mode

In UMDF versions prior to version 1.9, UMDF always makes an I/O request's buffers available to the driver (by copying the buffers into the [UMDF driver host process](umdf-driver-host-process.md)) as soon as UMDF receives the I/O request. This buffer retrieval mode is called *immediate retrieval*. If a failure occurs, UMDF completes the I/O request with a failure status value and does not deliver the I/O request to the driver.

UMDF versions 1.9 and later support both immediate retrieval and *deferred retrieval* modes. The deferred retrieval mode postpones copying an I/O request's buffer into the driver host process until the driver attempts to access the buffer. If a failure occurs, the buffer access functions return an error status value to the driver.

Your driver can specify a buffer retrieval mode when it calls [**IWDFDeviceInitialize2::SetIoTypePreference**](https://msdn.microsoft.com/library/windows/hardware/ff556969) for each device. Use the following rules:

-   If your driver specifies the direct I/O access method it must also specify the deferred retrieval mode. Direct I/O only works with deferred retrieval.

-   All drivers that are written to run with UMDF versions 1.9 and later should specify the deferred retrieval mode for all I/O requests, whether the driver chooses the buffered or direct I/O access method. Deferred retrieval provides better performance because it does not access buffers that the driver does not use.

If your driver does not specify a buffer retrieval mode, UMDF uses immediate retrieval.

All UMDF-based drivers in a driver stack must use the same retrieval mode. If some drivers specify immediate retrieval and some specify deferred retrieval, UMDF uses immediate retrieval.

### <a href="" id="how-umdf-chooses-a-buffer-access-method-for-an-i-o-request"></a> How UMDF Chooses a Buffer Access Method for an I/O Request

The access method that a driver specifies when it calls [**IWDFDeviceInitialize2::SetIoTypePreference**](https://msdn.microsoft.com/library/windows/hardware/ff556969), might not be the one that UMDF uses. UMDF uses the following rules to determine which access method to use:

-   All UMDF-based drivers in a driver stack must use the same method for accessing a device's buffers. If UMDF determines that some drivers prefer either buffered I/O or direct I/O for a device while other drivers prefer only buffered I/O for the device, UMDF uses buffered I/O for all drivers. If one or more of a stack's drivers prefer only buffered I/O while others prefer only direct I/O, UMDF logs an event to the system event log and does not start the driver stack.

    Your driver can call [**IWDFDevice2::GetDeviceStackIoTypePreference**](https://msdn.microsoft.com/library/windows/hardware/ff556934) to determine the buffer access methods that UMDF has assigned to a device's read/write requests and I/O control requests.

-   In some cases, a driver specifies a preference for direct I/O when it calls **IWDFDeviceInitialize2::SetIoTypePreference**, but for best performance, UMDF uses buffered I/O for one or more of the device's requests. For example, UMDF uses buffered I/O for small buffers if it can copy the data to the driver's buffer faster than it can map the buffers for direct access.

    Optionally, you can set a REG\_DWORD-typed **DirectTransferThreshold** registry value that the framework uses to determine the smallest buffer size for which the framework will use direct I/O. Typically, you do not need to provide this registry value because the framework uses a value that provides the best performance. The **DirectTransferThreshold** value is located under the device's **Device Parameters\\WUDF** subkey, which is under the device's [hardware key](https://msdn.microsoft.com/library/windows/hardware/ff549538).

    The framework uses the following rules to determine the threshold based on the value you provide in **DirectTransferThreshold**. The numbers provided assume a **PAGE\_SIZE** of 4096, which is valid except on Itanium-based systems.

    -   If you set **DirectTransferThreshold** to any value less than or equal to 8192 (or 2 \* **PAGE\_SIZE**), the framework sets the threshold to 8192. The framework uses buffered I/O for buffers smaller than 8192 bytes, and direct I/O for buffers equal to or larger than 8192 bytes.

    -   If you set **DirectTransferThreshold** to any value greater than 8192, the framework rounds up to the next exact multiple of **PAGE\_SIZE**. Again, the framework uses buffered I/O for buffers smaller than the threshold, and direct I/O for buffers equal to or larger than the threshold.

-   UMDF uses direct I/O only for buffer space that begins and ends on a memory page boundary. If either the beginning or the end of a buffer does not lie on a page boundary, UMDF uses buffered I/O for that part of the buffer. In other words, UMDF might use both buffered I/O and direct I/O for a large data transfer that consists of several I/O requests.

-   For device I/O control requests, UMDF uses direct I/O only if the I/O control code (IOCTL) specifies direct I/O and only if all of the device's UMDF-based drivers have called **IWDFDeviceInitialize2::SetIoTypePreference** to specify the direct access method.

Drivers use the same set of request object methods to access data buffers, regardless of the buffer access method. Therefore, most drivers typically do not need to know whether UMDF is using buffered I/O or direct I/O for an I/O request.

### <a href="" id="how-a-driver-can-obtain-the-access-method-for-an-i-o-request"></a> How a Driver Can Obtain the Access Method for an I/O Request

In a few cases, you can improve the device and driver's performance if the access method is known. In such cases, your driver can call [**IWDFIoRequest2::GetEffectiveIoType**](https://msdn.microsoft.com/library/windows/hardware/ff558994) to obtain an I/O request's buffer access method.

For example, consider a high-throughput device that typically uses direct I/O. Because it is using direct I/O, the driver must copy application-specified parameters to local driver memory before it validates the parameters, to ensure that the application does not modify the parameters after validation.

Because the driver might occasionally receive a buffer that uses buffered I/O, and because buffered I/O buffers have already been copied, the application cannot modify the data and the driver does not have to copy parameters before validating them. Therefore, the driver should check each request's buffer access method to determine if it must copy parameters before validating them.

### <a href="" id="using-buffered-i-o-in-umdf-drivers"></a> Using Buffered I/O in UMDF Drivers

If your driver is using buffered I/O, UMDF behavior differs depending on the type of request. For read and write requests, the driver host process creates a single intermediate buffer that the driver can access.

For write requests, the driver host process transfers input information from the calling application's input buffer before calling the driver stack. Drivers typically read input information from the intermediate buffer and write it to the device.

For read requests, drivers typically read information from a device and store it in the intermediate buffer. The driver host process copies the output data from the intermediate buffer to the application's output buffer.

For device I/O control requests, however, the driver host process creates two separate buffers that the driver can access. Note that this differs from the behavior of WDM and KMDF drivers, for which read, write, and device I/O control requests sent using buffered I/O result in the driver accessing a single, intermediate buffer. In this case, the output buffer initially contains nothing, and the driver should not read from it. In addition, any data that the driver writes to the input buffer is discarded and not returned to the calling application.

For guidelines about when to choose buffered I/O, see [**WDF\_DEVICE\_IO\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff561404).

UMDF versions 1.9 and later can support either immediate or deferred retrieval of request buffers. For more information, see [**WDF\_DEVICE\_IO\_BUFFER\_RETRIEVAL**](https://msdn.microsoft.com/library/windows/hardware/ff561399).

A driver that uses the immediate buffer retrieval mode must use [**IWDFIoRequest::GetInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559100) and [**IWDFIoRequest::GetOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559112) to access the buffers.

A driver that uses the deferred buffer retrieval mode can access the buffers by calling [**IWDFIoRequest2::RetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559033), [**IWDFIoRequest2::RetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559037), [**IWDFIoRequest2::RetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559041), or [**IWDFIoRequest2::RetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559046).

### <a href="" id="using-direct-i-o-in-umdf-drivers"></a> Using Direct I/O in UMDF Drivers

If your driver is using direct I/O, the driver host process verifies the accessibility of the buffer space that the originator of the I/O request (typically a user-mode application) specified, locks the buffer space into physical memory, and then provides the driver with direct access to the buffer space.

For guidelines about when to choose direct I/O, see [**WDF\_DEVICE\_IO\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff561404).

Your driver can access the buffers by calling [**IWDFIoRequest2::RetrieveInputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559033), [**IWDFIoRequest2::RetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559037), [**IWDFIoRequest2::RetrieveOutputBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559041), or [**IWDFIoRequest2::RetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559046).

### <a href="" id="using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers"></a> Using Neither Buffered I/O nor Direct I/O in UMDF Drivers

The buffer access method that is known as the *neither buffered I/O nor direct I/O method* (or, the "neither" method, for short) allows drivers to directly access an application's request buffer pointers. UMDF-based drivers cannot use this access method.

However, the [definitions](https://msdn.microsoft.com/library/windows/hardware/ff543023) of some device I/O control codes (IOCTLs) specify that the requests use the "neither" method. Optionally, UMDF can convert the buffer access method of such device I/O control requests to buffered I/O or direct I/O. Use the following steps:

1.  Include the [UmdfMethodNeitherAction](specifying-wdf-directives-in-inf-files.md) directive in an [**INF DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) of your driver's INF file. You can set the directive's value to indicate that UMDF should pass device I/O control requests that use the "neither" access method to the driver. (Otherwise, UMDF completes these I/O requests with an error status value.)

2.  Access the I/O request's buffers by using the object methods that UMDF provides for [buffered I/O](#using-buffered-i-o-in-umdf-drivers) or [direct I/O](#using-direct-i-o-in-umdf-drivers).

You should enable support of IOCTL requests that use the "neither" method only if you are sure that UMDF can convert the access method to buffered I/O or direct I/O. For example, if the IOCTL specifies a customized request that does not follow the buffer specification rules that are described at [Buffer Descriptions for I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff540663), UMDF cannot convert the buffers.

 

 





