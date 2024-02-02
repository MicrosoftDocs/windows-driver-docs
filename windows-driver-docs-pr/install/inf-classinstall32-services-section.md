---
title: INF ClassInstall32.Services Section
description: A ClassInstall32.Services section installs a new device setup class for devices in the new class.
keywords:
- INF ClassInstall32.Services Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF ClassInstall32.Services Section
api_type:
- NA
ms.date: 06/08/2022
---

# INF ClassInstall32.Services section

> [!CAUTION]
> If you are building a universal or Windows Driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md) and [Getting Started with Windows Drivers](../develop/getting-started-with-windows-drivers.md).

A **ClassInstall32** section installs a new [device setup class](./overview-of-device-setup-classes.md) for devices in the new class.

```inf
[ClassInstall32.Services] | 
[ClassInstall32.nt.Services] | 
[ClassInstall32.ntx86.Services] | 
[ClassInstall32.ntia64.Services] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64.Services]  (Windows XP and later versions of Windows)
[ClassInstall32.ntarm.Services] | (Windows 8 and later versions of Windows)
[ClassInstall32.ntarm64.Services] | (Windows 10 version 1709 and later versions of Windows)

AddService=ServiceName,[flags],service-install-section
                             [,event-log-install-section[,[EventLogType][,EventName]]]...
[DelService=ServiceName[,[flags][,[EventLogType][,EventName]]]...]
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
```

Each **ClassInstall32.Services** section contains one or more [**INF AddService directives**](inf-addservice-directive.md) that reference additional INF-writer-defined sections in an INF file.

INF files typically use the **ClassInstall32.Services** section with at least one **AddService** directive to control how and when the services of a particular device class are loaded, any dependencies it might have on other services, and so forth. Optionally, they can also set up event-logging services for the device class.

## Entries

**AddService=**_ServiceName_,[_flags_],_service-install-section_[,_event-log-install-section_[,[_EventLogType_][,_EventName_]]]...  
This directive references an INF-writer-defined _service-install-section_ and, possibly, an _event-log-install-section_ elsewhere in the INF file for the drivers of the device class covered by the [**ClassInstall32**](inf-classinstall32-section.md) section. For more information, see [**INF AddService Directive**](inf-addservice-directive.md).

**DelService=**_ServiceName_[,[_flags_][,[_EventLogType_][,_EventName_]]]...  
This directive removes a previously installed service from the target computer. This directive is very rarely used. For more information, see [**INF DelService Directive**](inf-delservice-directive.md).

**Include=**_filename_.**inf**[,_filename2_.**inf**]...  
This optional entry specifies one or more additional system-supplied named INF files that contain sections needed to install this device class. If this entry is specified, usually so is a **Needs** entry.

**Needs=**_inf-section-name_[,_inf-section-name_]...  
This optional entry specifies the particular named section that must be processed during the installation of this device class. Typically, such a named section is an **ClassInstall32.Services** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within such a **ClassInstall32.Services** section.

## Remarks

**ClassInstall32.Services** sections should have the same platform and operating system decorations as their related [**ClassInstall32 sections**](inf-classinstall32-section.md). For example, a **ClassInstall32.ntx86** section would have a corresponding **ClassInstall32.ntx86.Services** section.

The case-insensitive **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions can be inserted into a **ClassInstall32.Services** section name in cross-platform INF files, as shown in the formal syntax statement. For more information, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## See also

[**ClassInstall32**](inf-classinstall32-section.md)

[**AddService**](inf-addservice-directive.md)

[**_DDInstall_**](inf-ddinstall-section.md)

[**_DDInstall_.HW**](inf-ddinstall-hw-section.md)

[**DelService**](inf-delservice-directive.md)

[**_Models_**](inf-models-section.md)
