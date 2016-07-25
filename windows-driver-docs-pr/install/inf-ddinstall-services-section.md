---
title: INF DDInstall.Services Section
description: Each per-Models DDInstall.Services section contains one or more INF AddService directives that reference additional INF-writer-defined sections in an INF file.
ms.assetid: 30efb094-cc18-4c01-8851-4bc5dba1ae1d
keywords: ["INF DDInstall.Services Section Device and Driver Installation"]
topic_type:
- apiref
api_name:
- INF DDInstall.Services Section
api_type:
- NA
---

# INF DDInstall.Services Section


Each per-Models *DDInstall***.Services** section contains one or more [**INF AddService directives**](inf-addservice-directive.md) that reference additional INF-writer-defined sections in an INF file.

``` syntax
[install-section-name.Services] |
[install-section-name.nt.Services] |
[install-section-name.ntx86.Services] |
[install-section-name.ntia64.Services] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64.Services]  (Windows XP and later versions of Windows)
 
AddService=ServiceName,[flags],service-install-section
                     [,event-log-install-section[,[EventLogType][,EventName]]]...]
[DelService=ServiceName[,[flags][,[EventLogType][,EventName]]]]...
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...] 
```

You can provide a *DDInstall***.Services** section with at least one **AddService** directive to control how and when the services of a particular driver are loaded, dependencies on other services or drivers, and so forth. Optionally, you can also specify event-logging services.

## Entries


<a href="" id="addservice-servicename--flags--service-install-section"></a>**AddService=***ServiceName*,\[*flags*\]**,***service-install-section*  

<a href="" id="------------------------------------------------event-log-install-section---eventlogtype---eventname-------"></a>                                       \[,*event-log-install-section*\[**,**\[*EventLogType*\]\[**,***EventName*\]\]\]...\]  
This directive references an INF-writer-defined *service-install-section* and, possibly, an *event-log-install-section* elsewhere in the INF file for the drivers of the devices covered by this *DDInstall* section. For more information, see [**INF AddService Directive**](inf-addservice-directive.md).

<a href="" id="delservice-servicename---flags----eventlogtype---eventname------"></a>**DelService=***ServiceName*\[**,**\[*flags*\]\[**,**\[*EventLogType*\]\[**,***EventName*\]\]\]...  
This directive removes a previously installed service from the target computer. This directive is very rarely used. For more information, see [**INF DelService Directive**](inf-delservice-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=***filename***.inf**\[**,***filename2***.inf**\]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, usually so is a **Needs** entry.

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=***inf-section-name*\[**,***inf-section-name*\]...  
This optional entry specifies the section that must be processed during the installation of this device. Typically, the section is a *DDInstall***.Services** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within a *DDInstall***.Services** section.

**Needs** entries cannot be nested. For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

Remarks
-------

*DDInstall***.Services** sections should have the same platform and operating system decorations as their related [***DDInstall***](inf-ddinstall-section.md) sections. For example, an *install-section-name***.ntx86** section would have a corresponding *install-section-name***.ntx86.Services** section.

The specified *DDInstall* section must be referenced in a device/models-specific entry under the per-manufacturer *Models* section of the INF file. The case-insensitive extensions to the *install-section-name* shown in the formal syntax statement can be inserted into such a *DDInstall***.Services** section name in cross-platform INF files.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Examples
--------

This example shows the *DDInstall***.Services** section for the **Ser\_Inst** section shown as an example for the [**INF *DDInstall* section**](inf-ddinstall-section.md).

```
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

This example shows the *install-section-name***.NT.Services** section and its service-install-sections in the INF file for the system-supplied WDM audio device/driver shown as an example for the [**INF *DDInstall* section**](inf-ddinstall-section.md).

```
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

See [**INF DDInstall.HW Section**](inf-ddinstall-hw-section.md) for more examples of *DDInstall***.Services** sections with some *service-install*-sections referenced by the [**AddService**](inf-addservice-directive.md) directive. This includes one for a PnP filter driver.

## See also


[**AddService**](inf-addservice-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[**DelService**](inf-delservice-directive.md)

[***Models***](inf-models-section.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20DDInstall.Services%20Section%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





