---
title: Handling Client Impersonation in UMDF 1.x Drivers
description: Handling Client Impersonation in UMDF 1.x Drivers
ms.assetid: 25beab8c-e6b8-479b-ad60-fcc3b5b56a6d
keywords:
- User-Mode Driver Framework WDK , impersonation
- UMDF WDK , impersonation
- user-mode drivers WDK UMDF , impersonation
- impersonation WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Client Impersonation in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

UMDF drivers typically run under the LocalService account and cannot access files or resources that require user credentials, such as protected files or other protected resources. A UMDF driver typically operates on commands and data that flow between a client application and a device. Therefore, most UMDF drivers do not access protected resources.

However, some drivers might require access to a protected resource. For example, a UMDF driver might load firmware into a device from a file that a client application provides. The file might have an access control list (ACL) that prevents unauthorized users from modifying the file and taking control of the device. Unfortunately, this ACL also prevents the UMDF driver from accessing the file.

The framework provides an impersonation capability that allows drivers to impersonate the driver's client and obtain the client's access rights to protected resources.

### Enabling Impersonation

Both the UMDF driver's installation package and the client application must enable the framework's impersonation capability, as follows:

-   The INF file of the UMDF driver's installation package must include the **UmdfImpersonationLevel** directive and set the maximum allowable impersonation level. Impersonation is enabled only if the INF file includes the **UmdfImpersonationLevel** directive. For more information about setting the impersonation level, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

-   The client application must set the allowed impersonation level for each file handle. The application uses the quality of service (QoS) settings in the Microsoft Win32 **CreateFile** function to set the allowed impersonation level. For more information about these settings, see the *dwFlagsAndAttributes* parameter of **CreateFile** in the Windows SDK documentation.

### Handling Impersonation for an I/O Request

The UMDF driver and framework handle impersonation for an I/O request in the following sequence:

1.  The driver calls the [**IWDFIoRequest::Impersonate**](https://msdn.microsoft.com/library/windows/hardware/ff559136) method to specify the required impersonation level and an [**IImpersonateCallback::OnImpersonate**](https://msdn.microsoft.com/library/windows/hardware/ff554916) callback function.

2.  The framework checks the requested impersonation level. If the requested level is greater than the level that the UMDF driver's installation package and the client application allow, the impersonation request fails. Otherwise, the framework impersonates the client and immediately calls the **OnImpersonate** callback function.

The **OnImpersonate** callback function must perform only the operations that require the requested impersonation level, such as opening a protected file.

UMDF does not allow a driver's **OnImpersonate** callback function to call any of the framework's object methods. This ensures that the driver does not expose the impersonation level to other driver callback functions or other drivers.

**Note**   In versions 1.0 through 1.7 of UMDF, [**IWDFIoRequest::Impersonate**](https://msdn.microsoft.com/library/windows/hardware/ff559136) grants the highest impersonation level that the client application and INF file allow, even if the impersonation level that the driver requests is lower. In UMFD versions 1.9 and later, the **Impersonate** method grants only the impersonation level that the driver requests.

 

### Passing Credentials down the Driver Stack

When your driver receives a [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff561467)-typed I/O request, the driver might forward the I/O request down the driver stack to a kernel-mode driver. Kernel-mode drivers do not have the impersonation capability that **IWDFIoRequest::Impersonate** provides to UMDF-based drivers.

Therefore, if you want a kernel-mode driver to receive the client's user credentials (rather the credentials of the [driver host process](umdf-driver-host-process.md)), the driver must set the [**WDF\_REQUEST\_SEND\_OPTION\_IMPERSONATE\_CLIENT**](https://msdn.microsoft.com/library/windows/hardware/ff561462) flag when it calls [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) to send the create request to the I/O target. The **Send** method returns an error code if the impersonation attempt fails, unless the driver also sets the **WDF\_REQUEST\_SEND\_OPTION\_IMPERSONATION\_IGNORE\_FAILURE** flag.

The driver does not have to call **IWDFIoRequest::Impersonate** before it sends the request to the I/O target.

If lower-level drivers also forward the request, the client's impersonation level travels down the driver stack.

### Reducing Security Threats

To reduce the chance of an "elevation of privilege" attack, you should:

-   Try to avoid using impersonation.

    For example, to avoid using impersonation to open a file that the driver must use, the client application can open the file and use I/O operations to send file contents to the driver.

-   Use the lowest impersonation level that your driver requires.

    Set the impersonation level in your driver's INF file as low as possible. If your driver does not require any impersonation, do not include the **UmdfImpersonationLevel** directive in the INF file.

-   Minimize the opportunities for an attacker to exploit your driver.

    Your **OnImpersonate** callback function should contain a small section of code that performs only the operation that requires impersonation. For example, if your driver accesses a protected file, it requires impersonation only when it opens the file handle. It does not require impersonation to read from or write to the file.

 

 





