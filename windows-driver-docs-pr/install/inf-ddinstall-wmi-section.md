---
title: INF DDInstall.WMI Section
description: An INF DDInstall.WMI section contains one or more WMIInterface directives that specify characteristics for each WMI class that the driver provides.
keywords:
- INF DDInstall.WMI Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF DDInstall.WMI Section
api_type:
- NA
ms.date: 06/08/2022
---

# INF DDInstall.WMI section

An INF _DDInstall_.**WMI** section contains one or more **WMIInterface** directives that specify characteristics for each WMI class that the driver provides.

```inf
[install-section-name.WMI] |
[install-section-name.nt.WMI] | 
[install-section-name.ntx86.WMI] |
[install-section-name.ntia64.WMI] | (Windows XP and later versions of Windows)
[install-section-name.ntamd64.WMI] | (Windows XP and later versions of Windows)
[install-section-name.ntarm.WMI] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.WMI] (Windows 10 version 1709 and later versions of Windows)
 
WMIInterface={WmiClassGUID},[flags,]WMI-class-section
```

## Entries

_WmiClassGUID_  
Specifies a GUID value that identifies a WMI class.

_flags_  
Specifies one of the following bitmask flags:

0x00000001 (SCWMI_CLOBBER_SECURITY)  
If set, and if a security descriptor already exists in the registry, the existing security descriptor is replaced by the one specified in the INF file. If not set, and if a security descriptor already exists in the registry, the existing security descriptor is used instead of the one specified in the INF file.

_WMI-class-section_
Specifies an INF file section that contains directives for setting characteristics of the WMI class.

The following directives can be specified within a _WMI-class-section_:

**Security="**_security-descriptor-string_**"**  
Specifies a security descriptor that will be stored in the registry and applied to the GUID that is specified by _WmiClassGUID_. This security descriptor specifies the permissions that are required to access data blocks associated with the class. The _security-descriptor-string_ value is a string with tokens that indicate the DACL (**D:**) security component.

Only one **Security** entry can be present. If more than one **Security** entry is present, security is not set for the WMI class.

## Remarks

The INF _DDInstall_.**WMI** section is available on Microsoft Windows Server 2003 and later versions of the operating system.

A security descriptor is associated with every WMI GUID. For Windows XP and earlier operating system versions, the default security descriptor for WMI GUIDs allows full access to all users. For Windows Server 2003 and later versions, the default security descriptor allows access only to administrators.

If your driver defines WMI classes, and if you do not want to use the default descriptor, include a _DDInstall_.**WMI** section to specify a security descriptor that is stored in the registry and overrides the system's default descriptor.

For more information about how to specify security descriptors in INF files, see [Creating Secure Device Installations](creating-secure-device-installations.md).

## Examples

The following example shows a single _DDInstall_.**WMI** section that contains two **WMIInterface** directives. Each directive identifies a WMI class and specifies a _WMI-class-section_ for the class.

```inf
[InstallA.NT.WMI]
WMIInterface = {99999999-4cf9-11d2-ba4a-00a0c9062910},,WMISecurity1
WMIInterface = {99999998-4cf9-11d2-ba4a-00a0c9062910},1,WMISecurity2

[WmiSecurity1]
security = "O:BAG:BAD:(A;;0x120fff;;;BA)(A;;CC;;;WD)(A;;0x120fff;;;SY)"

[WmiSecurity2]
security = "O:BAG:BAD:(A;;0x120fff;;;BA)(A;;CC;;;WD)(A;;0x120fff;;;SY)"
```

## See also

[**_DDInstall_**](inf-ddinstall-section.md)

[**_Models_**](inf-models-section.md)
