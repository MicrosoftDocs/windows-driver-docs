---
title: Controlling Device Access
description: Controlling Device Access
ms.assetid: E4FF73B3-87D0-458E-A042-E5A8F3DB1677
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Controlling Device Access


The UMDF driver host process runs in the context of the local service account. Your driver may need to access other devices or components that do not permit generalized access to the local service account.

Starting in Windows 8, the operating system includes a security identifier (SID) that identifies UMDF drivers. By including this SID in their device security requirements, devices or components can permit access to UMDF drivers while preventing access from other requests from the local service account.

The SID for UMDF drivers is SDDL\_USER\_MODE\_DRIVERS, and the definition is in sddl.h. The full representation of this SID is:

```cpp
S-1-5-84-0-0-0-0-0
```

The abbreviation for this SID is UD. This abbreviation is available starting in Windows 8.

A driver external to your UMDF driver can specify the SID either in its INF file or in the driver, before it creates the device object.

## Specifying device security in an INF file


In the INF file, you can use either the abbreviated form or the fully specified form of the SID.

The abbreviated form is available starting in Windows 8:

```cpp
HKR,,Security,,"D:P(A;;GA;;;BA)(A;;GA;;;SY)(A;;GA;;;UD)"   
```

On operating systems earlier than Windows 8, you must use the fully specified form:

```cpp
HKR,,Security,,"D:P(A;;GA;;;BA)(A;;GA;;;SY)(A;;GA;;;S-1-5-84-0-0-0-0-0)"       
```

## Specifying device security in a KMDF driver


To specify security requirements in the driver, you must use the abbreviated form, which is only available starting in Windows 8. For example, a KMDF driver could enable access to its device from UMDF drivers by using the following:

```cpp
RtlInitUnicodeString(&sddlString, L"D:P(A;;GA;;;BA)(A;;GA;;;SY)(A;;GA;;;UD)");
status = WdfDeviceInitAssignSDDLString(DeviceInit, &sddlString);
```

 

 





