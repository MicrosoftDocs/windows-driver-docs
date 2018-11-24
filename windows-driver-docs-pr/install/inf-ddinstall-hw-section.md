---
title: INF DDInstall.HW Section
description: DDInstall.HW sections are typically used for installing multifunction devices, for installing PnP filter drivers, and for setting up any user-accessible device-specific but driver-independent information in the registry, whether with explicit AddReg directives or with Include and Needs entries.
ms.assetid: 417a4ab0-9723-4b3b-aa8c-342598874d61
keywords:
- INF DDInstall.HW Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.HW Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DDInstall.HW Section


<em>DDInstall</em>**.HW** sections are typically used for installing multifunction devices, for installing PnP filter drivers, and for setting up any user-accessible device-specific but driver-independent information in the registry, whether with explicit [**AddReg**](inf-addreg-directive.md) directives or with **Include** and **Needs** entries.

```cpp
[install-section-name.HW] |
[install-section-name.nt.HW] |
[install-section-name.ntx86.HW] |
[install-section-name.ntarm.HW] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.HW] | (Windows 10 version 1709 and later versions of Windows)
[install-section-name.ntia64.HW] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64.HW]  (Windows XP and later versions of Windows)
 
[AddReg=add-registry-section[,add-registry-section]...] ...
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
[DelReg=del-registry-section[,del-registry-section]...] ...
[BitReg=bit-registry-section[,bit-registry-section] ...] 
```

## Entries


<a href="" id="addreg-add-registry-section--add-registry-section----"></a>**AddReg=**<em>add-registry-section</em>\[**,**<em>add-registry-section</em>\]...  
References one or more INF-writer-defined *add-registry-sections* elsewhere in the INF file for the devices covered by this <em>DDInstall</em>**.HW** section. The *add-registry-section* typically installs filters and/or stores per-device information in the registry. An **HKR** specification in such an *add-registry-section* specifies the device's *hardware key*, a device-specific registry subkey that contains information about the device. A hardware key is also called a device key. For more info, see [Registry Trees and Keys for Devices and Drivers](https://docs.microsoft.com/windows-hardware/drivers/install/registry-trees-and-keys). A driver package can add settings via an INF by using an **HKR** specification in an add-registry-section referenced by a **DDInstall.HW section**. 

For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=**<em>filename</em>**.inf**\[**,**<em>filename2</em>**.inf**\]...  
Specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, usually so is a **Needs** entry.

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=**<em>inf-section-name</em>\[**,**<em>inf-section-name</em>\]...  
Specifies the named sections that must be processed during the installation of this device. Typically, such a named section is a <em>DDInstall</em>**.HW** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within such a <em>DDInstall</em>**.HW** section of the included INF.

**Needs** entries cannot be nested. For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="delreg-del-registry-section--del-registry-section----"></a>**DelReg=**<em>del-registry-section</em>\[**,**<em>del-registry-section</em>\]...  
References one or more INF-writer-defined *delete-registry-section*s elsewhere in the INF file for the drivers of the devices covered by this *DDInstall* section. Such a delete-registry section removes stale registry information for a previously installed device/driver from the target computer. An **HKR** specification in such a delete-registry section designates the same subkey as for **AddReg**.

This directive is rarely used, except in an INF file that upgrades a previous installation of the same devices/models listed in the per-manufacturer per-*Models* section that defined the name of this *DDInstall* section. For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

<a href="" id="bitreg-bit-registry-section--bit-registry-section-----"></a>**BitReg=**<em>bit-registry-section</em>\[**,**<em>bit-registry-section</em>\] ...  
Is valid in this section, but almost never used. An **HKR** specification in a referenced bit-registry section designates the same subkey as for **AddReg**. For more information, see [**INF BitReg Directive**](inf-bitreg-directive.md).

Remarks
-------

The case-insensitive extensions to the *install-section-name* shown in the formal syntax statement can be inserted into such a <em>DDInstall</em>**.HW** section name in cross-platform INF files. For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Any <em>DDInstall</em>**.HW** section must have one of the following:

- An **AddReg** directive.
- An **Include** entry that specifies another INF file. In this case, the <em>DDInstall</em>**.HW** section must also contain a corresponding **Needs** entry that specifies a section in the other INF file. This section is used to set up the necessary registry information.

Each directive in a <em>DDInstall</em>**.HW** section can reference more than one INF-writer-defined section. However, each additional named section must be separated from the next with a comma (,).

Each such section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

For more information about how to install multifunction devices, see [Supporting Multifunction Devices](https://msdn.microsoft.com/library/windows/hardware/ff542743).

Examples
--------

This example shows how the CD-ROM device class installer uses <em>DDInstall</em>**.HW** sections and <em>DDInstall</em>**.Services** sections to support both CD audio and changer functionality by creating the appropriate registry sections, and setting these up as PnP upper filter drivers.

```cpp
;;
;; Installation section for cdaudio. Sets cdrom as the service 
;; and adds cdaudio as a PnP upper filter driver. 
;;
[cdaudio_install]
CopyFiles=cdaudio_copyfiles,cdrom_copyfiles

[cdaudio_install.HW]
AddReg=nosync_addreg,cdaudio_addreg
 ; cdaudio_addreg required to register this as a PnP filter driver

[cdaudio_install.Services]
AddService=cdrom,0x00000002,cdrom_ServiceInstallSection
AddService=cdaudio,,cdaudio_ServiceInstallSection

[changer_install]
CopyFiles=changer_copyfiles,cdrom_copyfiles

[changer_install.HW]
AddReg=changer_addreg

; ... changer_install.Services section similar to cdaudio&#39;s

; ... some similar cdrom_install(.HW)/addreg sections omitted 

[cdaudio_addreg] ; changer_addreg section has similar entry
HKR,,"UpperFilters",0x00010000,"cdaudio" ; [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) value 

;
; Use next section to disable synchronous transfers to this device. 
; Sync transfers will always be turned off by default in this INF 
; for any cdrom-type device.
;
[nosync_addreg]
HKR,,"DefaultRequestFlags",0x00010001,8

[autorun_addreg]
HKLM,"System\CurrentControlSet\Services\cdrom","AutoRun",0x00010003,1
;;
;; service-install sections for cdrom, cdaudio, and changer
;;
[cdrom_ServiceInstallSection]
DisplayName    = %cdrom_ServiceDesc%
ServiceType    = 1
StartType      = 1
ErrorControl   = 1
ServiceBinary  = %12%\cdrom.sys
LoadOrderGroup = SCSI CDROM Class
AddReg         = autorun_addreg

[cdaudio_ServiceInstallSection]
DisplayName    = %cdaudio_ServiceDesc%
ServiceType    = 1
StartType      = 1
ErrorControl   = 1
ServiceBinary  = %12%\cdaudio.sys

; ... changer_ServiceInstallSection similar to cdaudio&#39;s
```

## See also


[**AddReg**](inf-addreg-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.Services**](inf-ddinstall-services-section.md)

[**DelReg**](inf-delreg-directive.md)

 

 






