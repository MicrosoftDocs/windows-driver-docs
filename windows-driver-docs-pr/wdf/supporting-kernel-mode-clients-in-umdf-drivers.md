---
title: Supporting Kernel-Mode Clients in UMDF Drivers
description: This topic describes how a User-Mode Driver Framework (UMDF) driver supports kernel-mode clients, starting in UMDF version 2.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Kernel-Mode Clients in UMDF Drivers


This topic describes how a User-Mode Driver Framework (UMDF) driver supports *kernel-mode clients*, starting in UMDF version 2.

A *kernel-mode client* is a kernel-mode driver that sends I/O requests to your UMDF driver. The kernel-mode driver might be above the UMDF driver, in the same device stack, or it might be in a different device stack.

The kernel-mode driver can forward I/O requests that it has received from a user-mode application, or can create new I/O requests and send them to the user-mode driver.

### <a href="" id="how-to-support-kernel-mode-clients-in-a-umdf-based-driver"></a>How to support kernel-mode clients in a UMDF driver

To enable a UMDF driver's support for kernel-mode clients, the INF file of the UMDF driver must include a [UmdfKernelModeClientPolicy](specifying-wdf-directives-in-inf-files.md) directive in its INF *DDInstall*.**WDF** section.

The framework provides two methods that are useful to drivers that support kernel-mode clients. A driver can call the [**WdfRequestGetRequestorMode**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetrequestormode) method to determine whether an I/O request came from kernel mode or user mode. If the I/O request came from user mode, the driver can call [**WdfRequestIsFromUserModeDriver**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestisfromusermodedriver) to determine whether the request came from an application or another user-mode driver.

### Restrictions on kernel-mode drivers

A UMDF driver can process I/O requests from a kernel-mode driver only if the kernel-mode driver meets the following requirements:

-   The kernel-mode driver must be running at IRQL = PASSIVE\_LEVEL when it sends the I/O request.

-   Unless the driver has set the **UmdfFileObjectPolicy** INF directive to **AllowNullAndUnknownFileObjects**, each I/O request that a kernel-mode driver sends to a user-mode driver must have an associated file object. The framework must have previously been notified that the I/O manager created the file object. (Such notification causes the framework to call the user-mode driver's [*EvtDeviceFileCreate*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_file_create) callback function, but that callback function is optional.)

-   The I/O request cannot contain an [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](../kernel/irp-mj-internal-device-control.md) function code.

-   The I/O request's buffers must not contain pointers to additional information, because the user-mode driver cannot dereference the pointers.

-   If the I/O request contains an [I/O control code](../kernel/introduction-to-i-o-control-codes.md) that specifies the "neither" buffer access method, the kernel-mode driver must send the I/O request in the process context of the application that created the I/O request. For more information about how to support the "neither" method in a UMDF driver, see [Managing Buffer Access Methods in UMDF Drivers](managing-buffer-access-methods-in-umdf-drivers.md).

-   The UMDF driver might modify an I/O request's output data, in user mode. Therefore, the kernel-mode driver must validate any output data that it receives from the user-mode driver.

-   The kernel-mode client should typically validate the *Information* value that a UMDF driver passes to [**WdfRequestCompleteWithInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation). If the client is a KMDF driver, it can call [**WdfRequestGetCompletionParams**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetcompletionparams) to obtain this information in an IO\_STATUS\_BLOCK structure.

    Typically, the framework does not validate the information value that a UMDF driver passes to [**WdfRequestCompleteWithInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation). (This parameter usually specifies the number of transferred bytes.) The framework validates the information value only for output buffers, and only for the [buffered I/O](./accessing-data-buffers-in-wdf-drivers.md#direct) data access method. (For example, the framework verifies that the number of transferred bytes does not exceed the output buffer size of a read operation, if the access method is buffered I/O.)

