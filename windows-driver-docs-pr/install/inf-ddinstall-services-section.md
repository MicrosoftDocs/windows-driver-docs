---
title: INF DDInstall.Services Section
description: Each per-Models DDInstall.Services section contains one or more INF AddService directives that reference additional INF-writer-defined sections in an INF file.
ms.assetid: 30efb094-cc18-4c01-8851-4bc5dba1ae1d
keywords:
- INF DDInstall.Services Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.Services Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DDInstall.Services Section


Each per-Models <em>DDInstall</em>**.Services** section contains one or more [**INF AddService directives**](inf-addservice-directive.md) that reference additional INF-writer-defined sections in an INF file.

```cpp
[install-section-name.Services] |
[install-section-name.nt.Services] |
[install-section-name.ntx86.Services] |
[install-section-name.ntarm.Services] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.Services] | (Windows 10 version 1709 and later versions of Windows)
[install-section-name.ntia64.Services] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64.Services]  (Windows XP and later versions of Windows)
 
AddService=ServiceName,[flags],service-install-section
                     [,event-log-install-section[,[EventLogType][,EventName]]]...]
[DelService=ServiceName[,[flags][,[EventLogType][,EventName]]]]...
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...] 
```

You can provide a <em>DDInstall</em>**.Services** section with at least one **AddService** directive to control how and when the services of a particular driver are loaded, dependencies on other services or drivers, and so forth. Optionally, you can also specify event-logging services.

## Entries

<a href="" id="addservice-servicename--flags--service-install-section"></a>
<a href="" id="------------------------------------------------event-log-install-section---eventlogtype---eventname-------"></a>
**AddService=**<em>ServiceName</em>,\[*flags*\]**,**<em>service-install-section</em>\[,*event-log-install-section*\[**,**\[*EventLogType*\]\[**,**<em>EventName</em>\]\]\]...\]  
This directive references an INF-writer-defined *service-install-section* and, possibly, an *event-log-install-section* elsewhere in the INF file for the drivers of the devices covered by this *DDInstall* section. For more information, see [**INF AddService Directive**](inf-addservice-directive.md).

<a href="" id="delservice-servicename---flags----eventlogtype---eventname------"></a>**DelService=**<em>ServiceName</em>\[**,**\[*flags*\]\[**,**\[*EventLogType*\]\[**,**<em>EventName</em>\]\]\]...  
This directive removes a previously installed service from the target computer. This directive is very rarely used. For more information, see [**INF DelService Directive**](inf-delservice-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=**<em>filename</em>**.inf**\[**,**<em>filename2</em>**.inf**\]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, usually so is a **Needs** entry.

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=**<em>inf-section-name</em>\[**,**<em>inf-section-name</em>\]...  
This optional entry specifies the section that must be processed during the installation of this device. Typically, the section is a <em>DDInstall</em>**.Services** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within a <em>DDInstall</em>**.Services** section.

**Needs** entries cannot be nested. For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

Remarks
-------

<em>DDInstall</em>**.Services** sections should have the same platform and operating system decorations as their related [***DDInstall***](inf-ddinstall-section.md) sections. For example, an <em>install-section-name</em>**.ntx86** section would have a corresponding <em>install-section-name</em>**.ntx86.Services** section.

The specified *DDInstall* section must be referenced in a device/models-specific entry under the per-manufacturer *Models* section of the INF file. The case-insensitive extensions to the *install-section-name* shown in the formal syntax statement can be inserted into such a <em>DDInstall</em>**.Services** section name in cross-platform INF files.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Examples
--------

This example shows the <em>DDInstall</em>**.Services** section for the **Ser_Inst** section shown as an example for the [**INF *DDInstall* section**](inf-ddinstall-section.md).

```cpp
[Ser_Inst.Services]
AddService=sermouse, 0x00000002, sermouse_Service_Inst,\
                sermouse_EventLog_Inst 
;
; flags value in preceding entry indicates function driver of device
; 
AddService = mouclass,, mouclass_Service_Inst, mouclass_EventLog_Inst 

; entries in the following xxx_Inst sections omitted here for brevity,
; but fully specified as the example for the AddService directive
;
[sermouse_Service_Inst]
; ...

[sermouse_EventLog_Inst]
; ...

[mouclass_Service_Inst]
; ...

[mouclass_EventLog_Inst]
; ...
```

This example shows the <em>install-section-name</em>**.NT.Services** section and its service-install-sections in the INF file for the system-supplied WDM audio device/driver shown as an example for the [**INF *DDInstall* section**](inf-ddinstall-section.md).

```cpp
[WDMPNPB003_Device.NT.Services]
AddService = wdmaud,0x00000000,wdmaud_Service_Inst
AddService = swmidi,0x00000000,swmidi_Service_Inst
AddService = sb16,  0x00000002,sndblst_Service_Inst

[wdmaud_Service_Inst]
DisplayName   = %wdmaud.SvcDesc% ; friendly name (see Strings)
ServiceType   = 1                ; SERVICE_KERNEL_DRIVER
StartType     = 1                ; SERVICE_SYSTEM_START
ErrorControl  = 1                ; SERVICE_ERROR_NORMAL
ServiceBinary = %10%\system32\drivers\wdmaud.sys

[swmidi_Service_Inst]
DisplayName   = %swmidi.SvcDesc% 
ServiceType   = 1 
StartType     = 1 
ErrorControl  = 1 
ServiceBinary = %10%\system32\drivers\swmidi.sys

[sndblst_Service_Inst]
DisplayName   = %sndblst.SvcDesc% 
ServiceType   = 1 
StartType     = 1 
ErrorControl  = 1 
ServiceBinary = %10%\system32\drivers\mssb16.sys

[Strings] ; only immediately preceding %strkey% tokens shown here
%wdmaud.SvcDesc%="Microsoft WDM Virtual Wave Driver (WDM)"
%swmidi.SvcDesc%="Microsoft Software Synthesizer (WDM)"
%sndblst.SvcDesc%="WDM Sample Driver for SB16"
```

See [**INF DDInstall.HW Section**](inf-ddinstall-hw-section.md) for more examples of <em>DDInstall</em>**.Services** sections with some *service-install*-sections referenced by the [**AddService**](inf-addservice-directive.md) directive. This includes one for a PnP filter driver.

## See also


[**AddService**](inf-addservice-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[**DelService**](inf-delservice-directive.md)

[***Models***](inf-models-section.md)

 

 






