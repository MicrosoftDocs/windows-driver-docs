---
title: Managing Buffer Access Methods in UMDF Drivers
description: If you are writing a UMDF driver, you can specify preferences for the buffer access method that the framework uses for read and write requests, as well as device I/O control requests.
ms.assetid: BDB78BCD-1964-431B-BE99-CABA6DF44D7A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Buffer Access Methods in UMDF Drivers


If you are writing a UMDF driver, you can specify *preferences* for the [buffer access method](https://msdn.microsoft.com/library/windows/hardware/ff540701) that the framework uses for read and write requests, as well as device I/O control requests. The values that a UMDF driver provides are only preferences, and are not guaranteed to be used by the framework.

-   [Specifying a Preferred Buffer Access Method](#specifying-preferred-buffer-access-method)
-   [Retrieving the Access Method for an I/O Request](#retrieving-access-method)
-   [Converting from Neither Buffered I/O nor Direct I/O](#using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers)

## <a href="" id="specifying-preferred-buffer-access-method"></a>Specifying a Preferred Buffer Access Method


Starting in UMDF version 2.0, a UMDF driver calls [**WdfDeviceInitSetIoTypeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265604) to register preferred access methods for read/write requests and for device I/O control requests.

If the driver does not call [**WdfDeviceInitSetIoTypeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265604), UMDF uses the buffered method for I/O requests to this device.

The framework uses the following rules to determine which access method to use:

-   All UMDF drivers in a driver stack must use the same method for accessing a device's buffers, and the framework gives preference to buffered I/O.

    If UMDF determines that some drivers prefer either buffered I/O or direct I/O for a device while other drivers prefer only buffered I/O for the device, UMDF uses buffered I/O for all drivers. If one or more of a stack's drivers prefer only buffered I/O while others prefer only direct I/O, UMDF logs an event to the system event log and does not start the driver stack.

    Your driver can call [**WdfDeviceGetDeviceStackIoType**](https://msdn.microsoft.com/library/windows/hardware/dn265602) to determine the buffer access methods that UMDF has assigned to a device's read/write requests and I/O control requests.

-   In some cases, UMDF assigns direct I/O to a device, but for best performance, uses buffered I/O for one or more of the device's requests. For example, UMDF uses buffered I/O for small buffers if it can copy the data to the driver's buffer faster than it can map the buffers for direct access.

    Optionally, your driver can provide a **DirectTransferThreshold** value when it calls [**WdfDeviceInitSetIoTypeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265604). The framework uses this value to determine the smallest buffer size for which the framework will use direct I/O. Typically, you do not need to provide this value because the framework uses settings that provide the best performance.

-   UMDF uses direct I/O only for buffer space that begins and ends on a memory page boundary. If either the beginning or the end of a buffer does not lie on a page boundary, UMDF uses buffered I/O for that part of the buffer. In other words, UMDF might use both buffered I/O and direct I/O for a large data transfer that consists of several I/O requests.

-   For device I/O control requests, UMDF uses direct I/O only if the I/O control code (IOCTL) specifies direct I/O and only if all of the UMDF drivers for that device have called [**WdfDeviceInitSetIoTypeEx**](https://msdn.microsoft.com/library/windows/hardware/dn265604) to specify the direct access method.

## <a href="" id="retrieving-access-method"></a>Retrieving the Access Method for an I/O Request


Drivers use the same set of request object methods to access data buffers, regardless of the buffer access method. Therefore, most drivers typically do not need to know whether UMDF is using buffered I/O or direct I/O for an I/O request.

In some cases, you can improve a driver's performance if you know the access method for an I/O request. For example, consider a high-throughput device that typically uses direct I/O. When the driver receives an I/O request, it copies data from the shared buffer space into local driver memory for validation.

However, the driver might occasionally receive a buffer that uses buffered I/O. Because the I/O manager has already copied this data into an intermediate buffer, the driver does not need to copy the parameters locally. By avoiding the copy operation, the driver improves performance.

A UMDF driver calls [**WdfRequestGetEffectiveIoType**](https://msdn.microsoft.com/library/windows/hardware/dn265616) to obtain an I/O request's buffer access method. As described above, the I/O type for a specific request may differ from the framework-assigned I/O type settings for a device.

## <a href="" id="using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers"></a> Converting from Neither Buffered I/O nor Direct I/O


A UMDF driver cannot use the "neither" method.

However, the [definitions](https://msdn.microsoft.com/library/windows/hardware/ff543023) of some device I/O control codes (IOCTLs) specify that the requests use the "neither" method. Optionally, a UMDF driver can convert the buffer access method of such device I/O control requests to buffered I/O or direct I/O. Use the following steps:

1.  Include the [UmdfMethodNeitherAction](specifying-wdf-directives-in-inf-files.md) directive in an [**INF DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) of your driver's INF file. You can set the directive's value to indicate that UMDF should pass device I/O control requests that use the "neither" access method to the driver. (Otherwise, UMDF completes these I/O requests with an error status value.)

2.  Access the I/O request's buffers by using the object methods that UMDF provides for [buffered I/O](https://msdn.microsoft.com/library/windows/hardware/ff540701#buffered) or [direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff540701#direct).

You should enable support of IOCTL requests that use the "neither" method only if you are sure that UMDF can convert the access method to buffered I/O or direct I/O. For example, if the IOCTL specifies a customized request that does not follow the buffer specification rules that are described at [Buffer Descriptions for I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff540663), UMDF cannot convert the buffers.

 

 





