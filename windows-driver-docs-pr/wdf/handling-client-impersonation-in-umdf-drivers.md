---
title: Handling Client Impersonation in UMDF Drivers
description: This topic describes how a User-Mode Driver Framework (UMDF) driver accesses protected resources, starting in UMDF version 2.
ms.assetid: 02EA93CE-3C4D-4F6F-8E58-DD78EBDB19DE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Client Impersonation in UMDF Drivers


This topic describes how a User-Mode Driver Framework (UMDF) driver accesses protected resources, starting in UMDF version 2.

UMDF drivers typically run under the LocalService account and cannot access files or resources that require user credentials, such as protected files or other protected resources. A UMDF driver typically operates on commands and data that flow between a client application and a device. Therefore, most UMDF drivers do not access protected resources.

However, some drivers might require access to a protected resource. For example, a UMDF driver might load firmware into a device from a file that a client application provides. The file might have an access control list (ACL) that prevents unauthorized users from modifying the file and taking control of the device. Unfortunately, this ACL also prevents the UMDF driver from accessing the file.

The framework provides an impersonation capability that allows drivers to impersonate the driver's client and obtain the client's access rights to protected resources.

### Enabling Impersonation

Both the UMDF driver's installation package and the client application must enable the framework's impersonation capability, as follows:

-   The INF file of the UMDF driver's installation package must include the **UmdfImpersonationLevel** directive and set the maximum allowable impersonation level. Impersonation is enabled only if the INF file includes the **UmdfImpersonationLevel** directive. For more information about setting the impersonation level, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

-   The client application must set the allowed impersonation level for each file handle. The application uses the quality of service (QoS) settings in the Microsoft Win32 **CreateFile** function to set the allowed impersonation level. For more information about these settings, see the *dwFlagsAndAttributes* parameter of **CreateFile** in the Windows SDK documentation.

### Handling Impersonation for an I/O Request

The UMDF driver and framework handle impersonation for an I/O request in the following sequence:

1.  The driver calls the [**WdfRequestImpersonate**](https://msdn.microsoft.com/library/windows/hardware/dn265619) method to specify the required impersonation level and an [*EvtRequestImpersonate*](https://msdn.microsoft.com/library/windows/hardware/dn265581) callback function.

2.  The framework checks the requested impersonation level. If the requested level is greater than the level that the UMDF driver's installation package and the client application allow, the impersonation request fails. Otherwise, the framework impersonates the client and immediately calls the [*EvtRequestImpersonate*](https://msdn.microsoft.com/library/windows/hardware/dn265581) callback function.

The [*EvtRequestImpersonate*](https://msdn.microsoft.com/library/windows/hardware/dn265581) callback function must perform only the operations that require the requested impersonation level, such as opening a protected file.

The framework does not allow a driver's [*EvtRequestImpersonate*](https://msdn.microsoft.com/library/windows/hardware/dn265581) callback function to call any of the framework's object methods. This ensures that the driver does not expose the impersonation level to other driver callback functions or other drivers.

As a best practice, your driver should not [enable cancellation](canceling-i-o-requests.md) of an I/O request before calling [**WdfRequestImpersonate**](https://msdn.microsoft.com/library/windows/hardware/dn265619) for that request.

The [**WdfRequestImpersonate**](https://msdn.microsoft.com/library/windows/hardware/dn265619) method grants only the impersonation level that the driver requests.

### Passing Credentials down the Driver Stack

When your driver receives a [**WdfRequestTypeCreate**](https://msdn.microsoft.com/library/windows/hardware/ff552503)-typed I/O request, the driver might forward the I/O request down the driver stack to a kernel-mode driver. Kernel-mode drivers do not have the impersonation capability that [**WdfRequestImpersonate**](https://msdn.microsoft.com/library/windows/hardware/dn265619) provides to UMDF drivers.

Therefore, if you want a kernel-mode driver to receive the client's user credentials (rather the credentials of the [driver host process](umdf-driver-host-process.md)), the driver must set the [**WDF\_REQUEST\_SEND\_OPTION\_IMPERSONATE\_CLIENT**](https://msdn.microsoft.com/library/windows/hardware/ff552493) flag when it calls [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the create request to the I/O target. The **Send** method returns an error code if the impersonation attempt fails, unless the driver also sets the **WDF\_REQUEST\_SEND\_OPTION\_IMPERSONATION\_IGNORE\_FAILURE** flag.

The following example shows how a UMDF driver might use the **WDF\_REQUEST\_SEND\_OPTION\_IMPERSONATE\_CLIENT** flag to send a file creation request to an I/O target. The driver's INF file must also include the **UmdfImpersonationLevel** directive as described above.

```cpp
WDFIOTARGET iotarget;
WDF_REQUEST_SEND_OPTIONS options;
NTSTATUS status;
WDF_REQUEST_PARAMETERS params;
ULONG sendFlags;  
 
WDF_REQUEST_PARAMETERS_INIT(&params);
WdfRequestGetParameters(Request, &params);
   
sendFlags = WDF_REQUEST_SEND_OPTION_SYNCHRONOUS;
if (params.Type == WdfRequestTypeCreate) {
    sendFlags |= WDF_REQUEST_SEND_OPTION_IMPERSONATE_CLIENT;
}
   
WDF_REQUEST_SEND_OPTIONS_INIT(&options, sendFlags);
if (WdfRequestSend(Request,
                   iotarget,
                   &options
                   ) == FALSE) {
    status = WdfRequestGetStatus(Request);
}
```

The driver does not have to call [**WdfRequestImpersonate**](https://msdn.microsoft.com/library/windows/hardware/dn265619) before it sends the request to the I/O target.

If lower-level drivers also forward the request, the client's impersonation level travels down the driver stack.

### Reducing Security Threats

To reduce the chance of an "elevation of privilege" attack, you should:

-   Try to avoid using impersonation.

    For example, to avoid using impersonation to open a file that the driver must use, the client application can open the file and use I/O operations to send file contents to the driver.

-   Use the lowest impersonation level that your driver requires.

    Set the impersonation level in your driver's INF file as low as possible. If your driver does not require any impersonation, do not include the **UmdfImpersonationLevel** directive in the INF file.

-   Minimize the opportunities for an attacker to exploit your driver.

    Your [*EvtRequestImpersonate*](https://msdn.microsoft.com/library/windows/hardware/dn265581) callback function should contain a small section of code that performs only the operation that requires impersonation. For example, if your driver accesses a protected file, it requires impersonation only when it opens the file handle. It does not require impersonation to read from or write to the file.

 

 





