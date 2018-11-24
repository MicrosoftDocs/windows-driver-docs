---
title: INF DDInstall.WMI Section
description: An INF DDInstall.WMI section contains one or more WMIInterface directives that specify characteristics for each WMI class that the driver provides.
ms.assetid: 8c4f6b2b-c2b4-4579-9dce-4436e041ebbc
keywords:
- INF DDInstall.WMI Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.WMI Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DDInstall.WMI Section


An INF *DDInstall*.**WMI** section contains one or more **WMIInterface** directives that specify characteristics for each WMI class that the driver provides.

```cpp
[install-section-name.WMI] |
[install-section-name.nt.WMI] | 
[install-section-name.ntx86.WMI] |
[install-section-name.ntarm.WMI] |  (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.WMI]  (Windows 10 version 1709 and later versions of Windows)
[install-section-name.ntia64.WMI] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64.WMI]  (Windows XP and later versions of Windows)
 
WMIInterface={WmiClassGUID},[flags,]WMI-class-section
```

## Entries


<a href="" id="wmiclassguid"></a>*WmiClassGUID*  
Specifies a GUID value that identifies a WMI class.

<a href="" id="flags"></a>*flags*  
Specifies one of the following bitmask flags:

<a href="" id="0x00000001--scwmi-clobber-security-"></a>0x00000001 (SCWMI_CLOBBER_SECURITY)  
If set, and if a security descriptor already exists in the registry, the existing security descriptor is replaced by the one specified in the INF file. If not set, and if a security descriptor already exists in the registry, the existing security descriptor is used instead of the one specified in the INF file.

<a href="" id="wmi-class-section"></a>*WMI-class-section*  
Specifies an INF file section that contains directives for setting characteristics of the WMI class.

The following directives can be specified within a *WMI-class-section*:

<a href="" id="security--security-descriptor-string-"></a>**Security="**<em>security-descriptor-string</em>**"**  
Specifies a security descriptor that will be stored in the registry and applied to the GUID that is specified by *WmiClassGUID*. This security descriptor specifies the permissions that are required to access data blocks associated with the class. The *security-descriptor-string* value is a string with tokens that indicate the DACL (**D:**) security component.

Only one **Security** entry can be present. If more than one **Security** entry is present, security is not set for the WMI class.

Remarks
-------

The INF <em>DDInstall</em>**.WMI** section is available on Microsoft Windows Server 2003 and later versions of the operating system.

A security descriptor is associated with every WMI GUID. For Windows XP and earlier operating system versions, the default security descriptor for WMI GUIDs allows full access to all users. For Windows Server 2003 and later versions, the default security descriptor allows access only to administrators.

If your driver defines WMI classes, and if you do not want to use the default descriptor, include a <em>DDInstall</em>**.WMI** section to specify a security descriptor that is stored in the registry and overrides the system's default descriptor.

For more information about how to specify security descriptors in INF files, see [Creating Secure Device Installations](creating-secure-device-installations.md).

Examples
--------

The following example shows a single <em>DDInstall</em>**.WMI** section that contains two **WMIInterface** directives. Each directive identifies a WMI class and specifies a *WMI-class-section* for the class.

```cpp
[InstallA.NT.WMI]
WMIInterface = {99999999-4cf9-11d2-ba4a-00a0c9062910},,WMISecurity1
WMIInterface = {99999998-4cf9-11d2-ba4a-00a0c9062910},1,WMISecurity2

[WmiSecurity1]
security = "O:BAG:BAD:(A;;0x120fff;;;BA)(A;;CC;;;WD)(A;;0x120fff;;;SY)"

[WmiSecurity2]
security = "O:BAG:BAD:(A;;0x120fff;;;BA)(A;;CC;;;WD)(A;;0x120fff;;;SY)"
```

## See also


[***DDInstall***](inf-ddinstall-section.md)

[***Models***](inf-models-section.md)

 

 






