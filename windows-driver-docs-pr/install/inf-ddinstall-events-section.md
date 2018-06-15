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
ms.author: windowsdriverdev
ms.date: 06/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF DDInstall.Events Section

This section is supported in Windows 10 version 1803 and later.

Each per-Models *DDInstall***.Events** section contains one or more [**INF AddEventProvider directives**](inf-addeventprovider-directive.md) that reference additional INF-writer-defined sections in an INF file.

```
[install-section-name.Events] |
[install-section-name.nt.Events] |
[install-section-name.ntx86.Events] |
[install-section-name.ntia64.Events] |
[install-section-name.ntamd64.Events]
 
AddEventProvider={ProviderGUID},event-provider-install-section
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...] 
```

You can provide a *DDInstall***.Events** section with at least one **AddEventProvider** directive to register [Event Tracing for Windows](https://msdn.microsoft.com/library/windows/desktop/aa363668) (ETW) providers.

## Entries

<a href="" id="addeventprovider--providerguid--event-provider-install-section"></a>**AddEventProvider=**{*ProviderGUID*},*event-provider-install-section*  
This directive references an INF-writer-defined *event-provider-install-section* elsewhere in the INF file for the drivers of the devices covered by this *DDInstall* section. For more information, see [**INF AddEventProvider Directive**](inf-addeventprovider-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=***filename***.inf**\[**,***filename2***.inf**\]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, a **Needs** entry is also usually required.

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=***inf-section-name*\[**,***inf-section-name*\]...  
This optional entry specifies the section that must be processed during the installation of this device. Typically, the section is a *DDInstall***.Events** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within a *DDInstall***.Events** section.

**Needs** entries cannot be nested. For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

Remarks
-------

*DDInstall***.Events** sections should have the same platform and operating system decorations as their related [***DDInstall***](inf-ddinstall-section.md) sections. For example, an *install-section-name***.ntx86** section would have a corresponding *install-section-name***.ntx86.Events** section.

The specified *DDInstall* section must be referenced in a device/models-specific entry under the per-manufacturer *Models* section of the INF file. The case-insensitive extensions to the *install-section-name* shown in the formal syntax statement can be inserted into such a *DDInstall***.Events** section name in cross-platform INF files.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Examples
--------

This example shows the *install-section-name***.Events** section and its event-provider-install-sections in the INF file.

```
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

 

 





