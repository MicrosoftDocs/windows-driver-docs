---
title: INF DDInstall.HW Section
description: DDInstall.HW sections are typically used for installing multifunction devices, for installing PnP filter drivers, and for setting up any user-accessible device-specific but driver-independent information in the registry, whether with explicit AddReg directives or with Include and Needs entries.
keywords:
- INF DDInstall.HW Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF DDInstall.HW Section
api_type:
- NA
ms.date: 06/02/2022
---

# INF DDInstall.HW section

_DDInstall_.**HW** sections are typically used for installing multifunction devices, for installing PnP filter drivers, and for setting up any user-accessible device-specific but driver-independent information in the registry, whether with explicit [**AddReg**](inf-addreg-directive.md) directives or with **Include** and **Needs** entries.

```inf
[install-section-name.HW] |
[install-section-name.nt.HW] |
[install-section-name.ntx86.HW] |
[install-section-name.ntia64.HW] | (Windows XP and later versions of Windows)
[install-section-name.ntamd64.HW] | (Windows XP and later versions of Windows)
[install-section-name.ntarm.HW] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.HW] (Windows 10 version 1709 and later versions of Windows)
 
[AddReg=add-registry-section[,add-registry-section]...] ...
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
[DelReg=del-registry-section[,del-registry-section]...] ...
[BitReg=bit-registry-section[,bit-registry-section] ...] 
```

## Entries

Not all valid entries are supported in a [Universal INF](using-a-universal-inf-file.md).  The following lists which directives are valid in a universal INF and which are not.

### Supported in a Universal INF

**AddReg=**_add-registry-section_[,_add-registry-section_]...  
References one or more INF-writer-defined _add-registry-sections_ elsewhere in the INF file for the devices covered by this _DDInstall_.**HW** section. The _add-registry-section_ typically installs filters and/or stores per-device information in the registry. An **HKR** specification in such an _add-registry-section_ specifies the device's _hardware key_, a device-specific registry subkey that contains information about the device. A hardware key is also called a device key. For more info, see [Registry Trees and Keys for Devices and Drivers](./registry-trees-and-keys.md). A driver package can add settings via an INF by using an **HKR** specification in an add-registry-section referenced by a **DDInstall.HW section**.

For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

**Include=**_filename_.**inf**[,_filename2_.**inf**]...  
Specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, usually so is a **Needs** entry.

**Needs=**_inf-section-name_[,_inf-section-name_]...  
Specifies the named sections that must be processed during the installation of this device. Typically, such a named section is a _DDInstall_.**HW** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within such a _DDInstall_.**HW** section of the included INF.

### Not supported in a Universal INF

**DelReg=**_del-registry-section_[,_del-registry-section_]...  
References one or more INF-writer-defined *delete-registry-section*s elsewhere in the INF file for the drivers of the devices covered by this _DDInstall_ section. Such a delete-registry section removes stale registry information for a previously installed device/driver from the target computer. An **HKR** specification in such a delete-registry section designates the same subkey as for **AddReg**.

This directive is rarely used, except in an INF file that upgrades a previous installation of the same devices/models listed in the per-manufacturer per-_Models_ section that defined the name of this _DDInstall_ section. For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

**BitReg=**_bit-registry-section_[,_bit-registry-section_] ...  
Is valid in this section, but almost never used. An **HKR** specification in a referenced bit-registry section designates the same subkey as for **AddReg**. For more information, see [**INF BitReg Directive**](inf-bitreg-directive.md).

## Remarks

The case-insensitive extensions to the _install-section-name_ shown in the formal syntax statement can be inserted into such a _DDInstall_.**HW** section name in cross-platform INF files. For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Any _DDInstall_.**HW** section must have one of the following:

- An **AddReg** directive.
- An **Include** entry that specifies another INF file. In this case, the _DDInstall_.**HW** section must also contain a corresponding **Needs** entry that specifies a section in the other INF file. This section is used to set up the necessary registry information.

Each directive in a _DDInstall_.**HW** section can reference more than one INF-writer-defined section. However, each additional named section must be separated from the next with a comma (,).

Each such section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

For more information about how to install multifunction devices, see [Supporting Multifunction Devices](../multifunction/index.md).

## Examples

This example shows how a driver package can use the _DDInstall_.**HW** sections and _DDInstall_.**Services** sections to add both a function driver and a PnP upper filter driver.

```inf
[Example_DDInstall]
CopyFiles=example_copyfiles

[Example_DDInstall.HW]
AddReg=filter_addreg

[filter_addreg]
HKR,,"UpperFilters",0x00010000,"ExampleUpperFilter" ; [REG_MULTI_SZ](https://learn.microsoft.com/windows/desktop/SysInfo/registry-value-types) value 

[Example_DDInstall.Services]
AddService=ExampleFunctionDriver,0x00000002,function_ServiceInstallSection
AddService=ExampleUpperFilter,,filter_ServiceInstallSection

[function_ServiceInstallSection]
DisplayName    = %function_ServiceDesc%
ServiceType    = 1
StartType      = 3
ErrorControl   = 1
ServiceBinary  = %13%\ExampleFunctionDriver.sys

[filter_ServiceInstallSection]
DisplayName    = %filter_ServiceDesc%
ServiceType    = 1
StartType      = 3
ErrorControl   = 1
ServiceBinary  = %13%\ExampleUpperFilter.sys
```

## See also

[**AddReg**](inf-addreg-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**_DDInstall_**](inf-ddinstall-section.md)

[**_DDInstall.Services_**](inf-ddinstall-services-section.md)

[**DelReg**](inf-delreg-directive.md)
