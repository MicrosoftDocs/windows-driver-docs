---
title: Controlling Device Access
author: windows-driver-content
description: Controlling Device Access
ms.assetid: E4FF73B3-87D0-458E-A042-E5A8F3DB1677
---

# Controlling Device Access


The UMDF driver host process runs in the context of the local service account. Your driver may need to access other devices or components that do not permit generalized access to the local service account.

Starting in Windows 8, the operating system includes a security identifier (SID) that identifies UMDF drivers. By including this SID in their device security requirements, devices or components can permit access to UMDF drivers while preventing access from other requests from the local service account.

The SID for UMDF drivers is SDDL\_USER\_MODE\_DRIVERS, and the definition is in sddl.h. The full representation of this SID is:

``` syntax
S-1-5-84-0-0-0-0-0
```

The abbreviation for this SID is UD. This abbreviation is available starting in Windows 8.

A driver external to your UMDF driver can specify the SID either in its INF file or in the driver, before it creates the device object.

## Specifying device security in an INF file


In the INF file, you can use either the abbreviated form or the fully specified form of the SID.

The abbreviated form is available starting in Windows 8:

``` syntax
HKR,,Security,,"D:P(A;;GA;;;BA)(A;;GA;;;SY)(A;;GA;;;UD)"   
```

On operating systems earlier than Windows 8, you must use the fully specified form:

``` syntax
HKR,,Security,,"D:P(A;;GA;;;BA)(A;;GA;;;SY)(A;;GA;;;S-1-5-84-0-0-0-0-0)"       
```

## Specifying device security in a KMDF driver


To specify security requirements in the driver, you must use the abbreviated form, which is only available starting in Windows 8. For example, a KMDF driver could enable access to its device from UMDF drivers by using the following:

```
RtlInitUnicodeString(&amp;sddlString, L"D:P(A;;GA;;;BA)(A;;GA;;;SY)(A;;GA;;;UD)");
status = WdfDeviceInitAssignSDDLString(DeviceInit, &amp;sddlString);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Controlling%20Device%20Access%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




