---
title: INF DDInstall.Events Section
author: andylsn
description: Each per-Models DDInstall.Events section contains one or more INF AddEventProvider directives that reference additional INF-writer-defined sections in an INF file.
ms.assetid: 
keywords:
- INF DDInstall.Events Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.Events Section
api_type:
- NA
ms.date: 06/04/2018
ms.localizationpriority: medium
---

# INF DDInstall.Events Section

Each per-Models <em>DDInstall</em>**.Events** section contains one or more [**INF AddEventProvider directives**](inf-addeventprovider-directive.md) that reference additional INF-writer-defined sections in an INF file. This section is supported for Windows 10 version 1809 and later.

```cpp
[install-section-name.Events] |
[install-section-name.nt.Events] |
[install-section-name.ntx86.Events] |
[install-section-name.ntia64.Events] |
[install-section-name.ntamd64.Events] |
[install-section-name.ntarm.Events] |
[install-section-name.ntarm64.Events] |

AddEventProvider={ProviderGUID},event-provider-install-section
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...] 
```

You can provide a <em>DDInstall</em>**.Events** section with at least one **AddEventProvider** directive to register [Event Tracing for Windows](https://msdn.microsoft.com/library/windows/desktop/aa363668) (ETW) providers.

## Entries

<a href="" id="addeventprovider--providerguid--event-provider-install-section"></a>**AddEventProvider=**{*ProviderGUID*},*event-provider-install-section*  
This directive references an INF-writer-defined *event-provider-install-section* elsewhere in the INF file for the drivers of the devices covered by this *DDInstall* section. For more information, see [**INF AddEventProvider Directive**](inf-addeventprovider-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=**<em>filename</em>**.inf**\[**,**<em>filename2</em>**.inf**\]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, a **Needs** entry is also usually required.

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=**<em>inf-section-name</em>\[**,**<em>inf-section-name</em>\]...  
This optional entry specifies the section that must be processed during the installation of this device. Typically, the section is a <em>DDInstall</em>**.Events** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within a <em>DDInstall</em>**.Events** section.

**Needs** entries cannot be nested. For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

Remarks
-------

<em>DDInstall</em>**.Events** sections should have the same platform and operating system decorations as their related [***DDInstall***](inf-ddinstall-section.md) sections. For example, an <em>install-section-name</em>**.ntx86** section would have a corresponding <em>install-section-name</em>**.ntx86.Events** section.

The specified *DDInstall* section must be referenced in a device/models-specific entry under the per-manufacturer *Models* section of the INF file. The case-insensitive extensions to the *install-section-name* shown in the formal syntax statement can be inserted into such a <em>DDInstall</em>**.Events** section name in cross-platform INF files.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Examples
--------

This example shows the <em>install-section-name</em>**.Events** section and its event-provider-install-sections in the INF file.

```cpp
[Device_Inst.NT.Events]
AddEventProvider={071acb53-ccfb-42e0-9a68-5336b7301507},foo_Event_Provider_Inst
AddEventProvider={6d3fd9ef-bcbb-42d7-9fbd-1bf2d926b394},bar_Event_Provider_Inst

; entries in the following xxx_Inst sections omitted here for brevity,
; but fully specified as the example for the AddEventProvider directive
;
[foo_Event_Provider_Inst]
; ...

[bar_Event_Provider_Inst]
; ...
```

## See also


[**AddEventProvider**](inf-addeventprovider-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

 

 





