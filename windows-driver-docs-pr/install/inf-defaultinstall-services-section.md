---
title: INF DefaultInstall.Services Section
description: A DefaultInstall.Services section contains one or more AddService directives referencing additional INF-writer-defined sections in an INF file.
keywords:
- INF DefaultInstall.Services Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF DefaultInstall.Services Section
api_type:
- NA
ms.date: 06/03/2022
---

# INF DefaultInstall.Services section

> [!CAUTION]
> If you are building a universal or Windows Driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md) and [Getting Started with Windows Drivers](../develop/getting-started-with-windows-drivers.md).

A **DefaultInstall.Services** section contains one or more [**AddService**](inf-addservice-directive.md) directives referencing additional INF-writer-defined sections in an INF file. This section is equivalent to the [**INF *DDInstall*.Services**](inf-ddinstall-services-section.md) section, and is used in association with an [**INF DefaultInstall**](inf-defaultinstall-section.md) section.

```inf
[DefaultInstall.Services] |
[DefaultInstall.nt.Services] |
[DefaultInstall.ntx86.Services] |
[DefaultInstall.ntia64.Services] | (Windows XP and later versions of Windows)
[DefaultInstall.ntamd64.Services] | (Windows XP and later versions of Windows)
[DefaultInstall.ntarm.Services] | (Windows 8 and later versions of Windows)
[DefaultInstall.ntarm64.Services] (Windows 10 version 1709 and later versions of Windows)
 
AddService=ServiceName,[flags],service-install-section
                             [,event-log-install-section[,[EventLogType][,EventName]]]...]
[DelService=ServiceName[,[flags][,[EventLogType][,EventName]]]...]
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
```

## Entries

**AddService=**_ServiceName_,[_flags_],_service-install-section_[,_event-log-install-section_[,[_EventLogType_][,EventName]]]...  
This directive references an INF-writer-defined _service-install-section_ and, possibly, an _event-log-install-section_ elsewhere in the INF file for the drivers covered by this [**DefaultInstall**](inf-defaultinstall-section.md) section.

For more information, see [**INF AddService Directive**](inf-addservice-directive.md).

**DelService=**_ServiceName_[,[_flags_][,[_EventLogType_][,_EventName_]]]...  
This directive removes a previously installed service from the target computer. This directive is very rarely used.

For more information, see [**INF DelService Directive**](inf-delservice-directive.md).

**Include=**_filename_.**inf**[,_filename2_.**inf**]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, usually so is a **Needs** entry.

**Needs=**_inf-section-name_[,_inf-section-name_]...  
This optional entry specifies the particular named section that must be processed during the installation of this device. Typically, such a named section is a _DDInstall_**.Services** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within such a _DDInstall_**.Services** section.

## Remarks

The [**AddService**](inf-addservice-directive.md) directive controls how and when the services of a particular driver are loaded, any dependencies on other services or on underlying (legacy) drivers it might have, and so forth. Optionally, it can set up event-logging services for the driver as well.

> [!NOTE]
> INF files use the **DefaultInstall.Services** section only if they also use an [**INF DefaultInstall**](inf-defaultinstall-section.md) section. Otherwise, they use [**INF *DDInstall*.Services**](inf-ddinstall-services-section.md) sections together with [**INF *DDInstall***](inf-ddinstall-section.md) sections.

**DefaultInstall.Services** sections should have the same platform and operating system decorations as their related **DefaultInstall** sections. For example, a **DefaultInstall.ntx86** section would have a corresponding **DefaultInstall.ntx86.Services** section. For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## Examples

See the examples provided for the [**INF *DDInstall*.Services**](inf-ddinstall-services-section.md) section.

## See also

[**_DDInstall_**](inf-ddinstall-section.md)

[**DefaultInstall**](inf-defaultinstall-section.md)
