---
title: INF DDInstall.Services section
description: Each per-Models DDInstall.Services section contains one or more INF AddService directives that reference additional INF-writer-defined sections in an INF file.
keywords:
- INF DDInstall.Services Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.Services Section
api_type:
- NA
ms.date: 06/02/2022
---

# INF DDInstall.Services section

Each per-Models _DDInstall_.**Services** section contains one or more [**INF AddService directives**](inf-addservice-directive.md) that reference additional INF-writer-defined sections in an INF file.

```inf
[install-section-name.Services] |
[install-section-name.nt.Services] |
[install-section-name.ntx86.Services] |
[install-section-name.ntia64.Services] | (Windows XP and later versions of Windows)
[install-section-name.ntamd64.Services] | (Windows XP and later versions of Windows)
[install-section-name.ntarm.Services] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.Services] (Windows 10 version 1709 and later versions of Windows)
 
AddService=ServiceName,[flags],service-install-section
                     [,event-log-install-section[,[EventLogType][,EventName]]]...]
[DelService=ServiceName[,[flags][,[EventLogType][,EventName]]]]...
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...] 
```

You can provide a _DDInstall_.**Services** section with at least one **AddService** directive to control how and when the services of a particular driver are loaded, dependencies on other services or drivers, and so forth. Optionally, you can also specify event-logging services.

## Entries

**AddService=**_ServiceName_,[_flags_],_service-install-section_[,_event-log-install-section_[,[_EventLogType_][,_EventName_]]]...]  
This directive references an INF-writer-defined _service-install-section_ and, possibly, an _event-log-install-section_ elsewhere in the INF file for the drivers of the devices covered by this _DDInstall_ section. For more information, see [**INF AddService Directive**](inf-addservice-directive.md).

**DelService=**_ServiceName_[,[_flags_][,[_EventLogType_][,_EventName_]]]...  
This directive removes a previously installed service from the target computer. This directive is very rarely used. For more information, see [**INF DelService Directive**](inf-delservice-directive.md).

**Include=**_filename_.**inf**[,_filename2_.**inf*_]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, usually so is a **Needs** entry.

**Needs=**_inf-section-name_[,_inf-section-name_]...  
This optional entry specifies the section that must be processed during the installation of this device. Typically, the section is a _DDInstall_.**Services** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within a _DDInstall_.**Services** section.

## Remarks

_DDInstall_.**Services** sections should have the same platform and operating system decorations as their related [**_DDInstall_**](inf-ddinstall-section.md) sections. For example, an _install-section-name_.**ntx86** section would have a corresponding _install-section-name_.**ntx86.Services** section.

The specified _DDInstall_ section must be referenced in a device/models-specific entry under the per-manufacturer _Models_ section of the INF file. The case-insensitive extensions to the _install-section-name_ shown in the formal syntax statement can be inserted into such a _DDInstall_.**Services** section name in cross-platform INF files.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## Examples

This example shows the _install-section-name_.**NT.Services** section and its service-install-sections in the INF file for an example driver package that adds a function driver and filter driver to a device.

```inf
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

[Strings] ; only immediately preceding %strkey% tokens shown here
%function_ServiceDesc%="Example function driver service"
%filter_ServiceDesc%="Example filter driver service"
```

See [**INF DDInstall.HW Section**](inf-ddinstall-hw-section.md) for more examples of _DDInstall_.**Services** sections with some *service-install-section*s referenced by the [**AddService**](inf-addservice-directive.md) directive. This includes one for a PnP filter driver.

## See also

[**AddService**](inf-addservice-directive.md)

[**_DDInstall_**](inf-ddinstall-section.md)

[**_DDInstall_.HW**](inf-ddinstall-hw-section.md)

[**DelService**](inf-delservice-directive.md)

[**_Models_**](inf-models-section.md)
