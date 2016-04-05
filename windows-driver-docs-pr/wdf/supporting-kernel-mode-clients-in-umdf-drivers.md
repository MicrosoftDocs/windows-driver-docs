---
title: Supporting Kernel-Mode Clients in UMDF Drivers
description: This topic describes how a User-Mode Driver Framework (UMDF) driver supports kernel-mode clients, starting in UMDF version 2.
ms.assetid: 5C0180BF-F0C7-4225-8388-C3315C282516
---

# Supporting Kernel-Mode Clients in UMDF Drivers


This topic describes how a User-Mode Driver Framework (UMDF) driver supports *kernel-mode clients*, starting in UMDF version 2.

A *kernel-mode client* is a kernel-mode driver that sends I/O requests to your UMDF driver. The kernel-mode driver might be above the UMDF driver, in the same device stack, or it might be in a different device stack.

The kernel-mode driver can forward I/O requests that it has received from a user-mode application, or can create new I/O requests and send them to the user-mode driver.

### <a href="" id="how-to-support-kernel-mode-clients-in-a-umdf-based-driver"></a>How to support kernel-mode clients in a UMDF driver

To enable a UMDF driver's support for kernel-mode clients, the INF file of the UMDF driver must include a [UmdfKernelModeClientPolicy](specifying-wdf-directives-in-inf-files.md) directive in its INF *DDInstall*.**WDF** section.

The framework provides two methods that are useful to drivers that support kernel-mode clients. A driver can call the [**WdfRequestGetRequestorMode**](https://msdn.microsoft.com/library/windows/hardware/ff549971) method to determine whether an I/O request came from kernel mode or user mode. If the I/O request came from user mode, the driver can call [**WdfRequestIsFromUserModeDriver**](https://msdn.microsoft.com/library/windows/hardware/dn265620) to determine whether the request came from an application or another user-mode driver.

### Restrictions on kernel-mode drivers

A UMDF driver can process I/O requests from a kernel-mode driver only if the kernel-mode driver meets the following requirements:

-   The kernel-mode driver must be running at IRQL = PASSIVE\_LEVEL when it sends the I/O request.

-   Unless the driver has set the **UmdfFileObjectPolicy** INF directive to **AllowNullAndUnknownFileObjects**, each I/O request that a kernel-mode driver sends to a user-mode driver must have an associated file object. The framework must have previously been notified that the I/O manager created the file object. (Such notification causes the framework to call the user-mode driver's [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function, but that callback function is optional.)

-   The I/O request cannot contain an [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) function code.

-   The I/O request's buffers must not contain pointers to additional information, because the user-mode driver cannot dereference the pointers.

-   If the I/O request contains an [I/O control code](https://msdn.microsoft.com/library/windows/hardware/ff565406) that specifies the "neither" buffer access method, the kernel-mode driver must send the I/O request in the process context of the application that created the I/O request. For more information about how to support the "neither" method in a UMDF driver, see [Managing Buffer Access Methods in UMDF Drivers](managing-buffer-access-methods-in-umdf-drivers.md).

-   The UMDF driver might modify an I/O request's output data, in user mode. Therefore, the kernel-mode driver must validate any output data that it receives from the user-mode driver.

-   The kernel-mode client should typically validate the *Information* value that a UMDF driver passes to [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948). If the client is a KMDF driver, it can call [**WdfRequestGetCompletionParams**](https://msdn.microsoft.com/library/windows/hardware/ff549961) to obtain this information in an IO\_STATUS\_BLOCK structure.

    Typically, the framework does not validate the information value that a UMDF driver passes to [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948). (This parameter usually specifies the number of transferred bytes.) The framework validates the information value only for output buffers, and only for the [buffered I/O](https://msdn.microsoft.com/library/windows/hardware/ff540701#direct) data access method. (For example, the framework verifies that the number of transferred bytes does not exceed the output buffer size of a read operation, if the access method is buffered I/O.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20Kernel-Mode%20Clients%20in%20UMDF%20Drivers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




