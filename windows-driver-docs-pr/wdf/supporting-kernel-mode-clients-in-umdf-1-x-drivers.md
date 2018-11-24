---
title: Supporting Kernel-Mode Clients in UMDF 1.x Drivers
description: Supporting Kernel-Mode Clients in UMDF 1.x Drivers
ms.assetid: 933dc761-2616-4bee-8357-dbb6644596c2
keywords:
- kernel-mode clients WDK UMDF
- UMDF drivers WDK UMDF , kernel-mode clients
- user-mode drivers WDK UMDF , kernel-mode clients
- UMDF WDK , kernel-mode clients
- User-Mode Driver Framework WDK , kernel-mode clients
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Kernel-Mode Clients in UMDF 1.x Drivers

[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

>[!WARNING]
>Also see [Supporting Kernel-Mode Clients in UMDF 2.x](supporting-kernel-mode-clients-in-umdf-drivers.md).

UMDF versions 1.9 and later allow UMDF drivers to support *kernel-mode clients*. A kernel-mode client can be either of the following:

-   A kernel-mode driver that exists above a UMDF driver in a device's driver stack.

-   A kernel-mode driver for one device stack, which supports one device, opens a handle to another device, and the latter device's driver stack contains a UMDF driver.

In other words, a UMDF driver that supports kernel-mode clients can receive I/O requests from a kernel-mode driver. The kernel-mode driver can forward I/O requests that it has received from a user-mode application, or can create new I/O requests and send them to the user-mode driver.

To determine if your UMDF driver must support kernel-mode clients, you must understand the driver stack to which your driver will be added, and where in that stack your driver will reside. You must also determine whether a driver from another stack might send I/O requests to your driver's device.

Your driver must support kernel-mode clients if:

-   A kernel-mode driver can be located directly above your UMDF driver in a driver stack. For example, a kernel-mode filter driver might reside directly above a UMDF-based function driver.

-   A kernel-mode driver from another stack can send I/O requests to your driver's device. For example, your driver might create a symbolic link that a kernel-mode driver in another stack can use to open a handle to your driver's device. The kernel-mode driver can then send I/O requests to the device.

### <a href="" id="how-to-support-kernel-mode-clients-in-a-umdf-based-driver"></a>How to support kernel-mode clients in a UMDF driver

A UMDF driver can receive I/O requests from a kernel-mode driver only if the UMDF driver has enabled support for kernel-mode clients. Furthermore, if a device installation attempts to load kernel-mode drivers above a UMDF driver in the device's driver stack, the framework allows the drivers to load only if the UMDF driver has enabled support for kernel-mode clients.

To enable a UMDF driver's support for kernel-mode clients, the INF file of the UMDF driver must include a [UmdfKernelModeClientPolicy](specifying-wdf-directives-in-inf-files.md) directive in its INF *DDInstall*.**WDF** section. If the INF file of the UMDF driver does not include this directive, UMDF does not allow a kernel-mode driver that is installed above the UMDF driver to run.

The framework provides two methods that are useful to drivers that support kernel-mode clients. A driver can call the [**IWDFIoRequest2::GetRequestorMode**](https://msdn.microsoft.com/library/windows/hardware/ff559002) method to determine whether an I/O request came from kernel mode or user mode. If the I/O request came from user mode, the driver can call [**IWDFIoRequest2::IsFromUserModeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559021) to determine whether the request came from an application or another user-mode driver.

### Restrictions on kernel-mode drivers

A UMDF driver can process I/O requests from a kernel-mode driver only if the kernel-mode driver meets the following requirements:

-   The kernel-mode driver must be running at IRQL = PASSIVE\_LEVEL when it sends the I/O request.

-   Unless the driver has set the **UmdfFileObjectPolicy** INF directive to **AllowNullAndUnknownFileObjects**, each I/O request that a kernel-mode driver sends to a user-mode driver must have an associated file object. The framework must have previously been notified that the I/O manager created the file object. (Such notification causes the framework to call the user-mode driver's [**IQueueCallbackCreate::OnCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff556841) callback function, but that callback function is optional.)

-   The I/O request cannot contain an [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) function code.

-   The I/O request's buffers must not contain pointers to additional information, because the user-mode driver cannot dereference the pointers.

-   If the I/O request contains an [I/O control code](https://msdn.microsoft.com/library/windows/hardware/ff565406) that specifies the "neither" buffer access method, the kernel-mode driver must send the I/O request in the process context of the application that created the I/O request. For more information about how to support the "neither" method in a UMDF-base driver, see [Using Neither Buffered I/O nor Direct I/O in UMDF Drivers](https://msdn.microsoft.com/library/windows/hardware/ff554413#using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers).

-   The UMDF driver might modify an I/O request's output data, in user mode. Therefore, the kernel-mode driver must validate any output data that it receives from the user-mode driver.

-   The kernel-mode client should typically validate the *Information* value that a UMDF driver passes to [**IWDFIoRequest::CompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559074). If the client is a KMDF driver, it can call [**WdfRequestGetCompletionParams**](https://msdn.microsoft.com/library/windows/hardware/ff549961) to obtain this information in an IO\_STATUS\_BLOCK structure.

    Typically, the framework does not validate the information value that a UMDF driver passes to [**IWDFIoRequest::CompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559074). (This parameter usually specifies the number of transferred bytes.) The framework validates the information value only for output buffers, and only for the [buffered I/O](https://msdn.microsoft.com/library/windows/hardware/ff554413#using-buffered-i-o-in-umdf-drivers) data access method. (For example, the framework verifies that the number of transferred bytes does not exceed the output buffer size of a read operation, if the access method is buffered I/O.)

### <a href="" id="handling-return-status-values"></a>Handling return status values in a UMDF 1.x driver

Passing return status values from user-mode to kernel-mode requires special attention, as follows:

-   UMDF version 1 drivers typically receive HRESULT-typed return values, while KMDF and WDM-based kernel-mode drivers typically receive NTSTATUS-typed values. If a UMDF 1.*x* driver completes an I/O request, and if the driver has a kernel-mode client, the driver's call to [**IWDFIoRequest::Complete**](https://msdn.microsoft.com/library/windows/hardware/ff559070) or [**IWDFIoRequest::CompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559074) should specify an HRESULT value that the driver generates from an NTSTATUS value. In general, UMDF 1.*x* drivers should use the HRESULT\_FROM\_NT macro (defined in *Winerror.h*) to return status to a kernel-mode client. The following example shows how to use this macro when completing a request.

    ```cpp
    hr = HRESULT_FROM_NT(STATUS_BUFFER_OVERFLOW)
    request->Complete(HRESULT_FROM_NT(STATUS_BUFFER_OVERFLOW);
    return hr;
    ```

    To return a specific HRESULT value to a kernel-mode client, the following callbacks must use the HRESULT\_FROM\_NT macro:

    -   [**IPnpCallback::OnQueryRemove**](https://msdn.microsoft.com/library/windows/hardware/ff556808)
    -   [**IPnpCallback::OnQueryStop**](https://msdn.microsoft.com/library/windows/hardware/ff556811)
    -   [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766)
    -   [**IPnpCallbackHardware::OnReleaseHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556768)

    To use the NTSTATUS values that are defined in *ntstatus.h*, a UMDF 1.*x* driver must include these two lines before including any additional headers.

    ```cpp
    #define UMDF_USING_NTSTATUS
    #include <ntstatus.h>
    ```

    Do not use the HRESULT\_FROM\_NT macro to convert STATUS\_SUCCESS from an NTSTATUS value to an HRESULT value. Just return S\_OK, as shown in the following example.

    ```cpp
    request->Complete(S_OK);
    ```

-   The framework completes some I/O requests on behalf of UMDF drivers. Sometimes the framework does not convert HRESULT-typed return values into equivalent NTSTATUS values, so the framework might pass an HRESULT-typed completion status to a kernel-mode client.

    Because of this situation, kernel-mode clients should not use the NT\_ERROR macro when testing an I/O request's completion status, because the NT\_ERROR macro does not return **TRUE** for HRESULT error values. Kernel-mode drivers should use the NT\_SUCCESS macro when testing an I/O request's completion status.

### <a href="" id="kernel-mode-client-support-in-earlier-umdf-versions"></a> Kernel-mode client support in earlier UMDF versions

For UMDF versions earlier than version 1.9, a driver's INF file can include an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) to create a REG\_DWORD-sized **UpperDriverOk** registry value under the **WUDF** subkey of the device's [hardware key](https://msdn.microsoft.com/library/windows/hardware/ff561381).

If the **UpperDriverOk** registry value is set to a nonzero number, the framework allows kernel-mode drivers to load above the user-mode driver. The kernel-mode drivers can forward I/O requests from user-mode applications to the UMDF driver, but kernel-mode drivers cannot send I/O requests that are created in kernel mode to the UMDF driver.

For UMDF versions 1.9 and later, the **UpperDriverOk** registry value is obsolete and supported only for existing drivers. New drivers should use the [UmdfKernelModeClientPolicy](specifying-wdf-directives-in-inf-files.md) directive.

 

 





