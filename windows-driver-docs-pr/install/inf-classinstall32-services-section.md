---
title: INF ClassInstall32.Services Section
description: A ClassInstall32 section installs a new device setup class (and possibly a class installer) for devices in the new class.
ms.assetid: 602cf407-f3c0-4342-9e59-87481a0f41ef
keywords:
- INF ClassInstall32.Services Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF ClassInstall32.Services Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF ClassInstall32.Services Section


**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A **ClassInstall32** section installs a new [device setup class](device-setup-classes.md) (and possibly a class installer) for devices in the new class.

```cpp
[ClassInstall32.Services] | 
[ClassInstall32.nt.Services] | 
[ClassInstall32.ntx86.Services] | 
[ClassInstall32.ntarm.Services] | (Windows 8 and later versions of Windows)
[ClassInstall32.ntarm64.Services] | (Windows 10 version 1709 and later versions of Windows)
[ClassInstall32.ntia64.Services] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64.Services]  (Windows XP and later versions of Windows)

AddService=ServiceName,[flags],service-install-section
                             [,event-log-install-section[,[EventLogType][,EventName]]]...
[DelService=ServiceName[,[flags][,[EventLogType][,EventName]]]...]
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
```

Each **ClassInstall32.Services** section contains one or more [**INF AddService directives**](inf-addservice-directive.md) that reference additional INF-writer-defined sections in an INF file.

INF files typically use the **ClassInstall32.Services** section with at least one **AddService** directive to control how and when the services of a particular device class are loaded, any dependencies it might have on other services, and so forth. Optionally, they can also set up event-logging services for the device class.

## Entries


<a href="" id="addservice-servicename--flags--service-install-section"></a>**AddService=**<em>ServiceName</em>,\[*flags*\]**,**<em>service-install-section</em>  

<a href="" id="----------------------------------------event-log-install-section---eventlogtype---eventname------"></a>                                      \[**,**<em>event-log-install-section</em>\[**,**\[*EventLogType*\]\[**,**<em>EventName</em>\]\]\]...  
This directive references an INF-writer-defined service-install-section and, possibly, an event-log-install-section elsewhere in the INF file for the drivers of the device class covered by the [**ClassInstall32**](inf-classinstall32-section.md) section. For more information, see [**INF AddService Directive**](inf-addservice-directive.md).

<a href="" id="delservice-servicename---flags----eventlogtype---eventname------"></a>**DelService=**<em>ServiceName</em>\[**,**\[*flags*\]\[**,**\[*EventLogType*\]\[**,**<em>EventName</em>\]\]\]...  
This directive removes a previously installed service from the target computer. This directive is very rarely used. For more information, see [**INF DelService Directive**](inf-delservice-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=**<em>filename</em>**.inf**\[**,**<em>filename2</em>**.inf**\]...  
This optional entry specifies one or more additional system-supplied named INF files that contain sections needed to install this device class. If this entry is specified, usually so is a **Needs** entry.

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=**<em>inf-section-name</em>\[**,**<em>inf-section-name</em>\]...  
This optional entry specifies the particular named section that must be processed during the installation of this device class. Typically, such a named section is an **ClassInstall32.Services** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within such a **ClassInstall32.Services** section.

**Needs** entries cannot be nested. (For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md)).

Remarks
-------

**ClassInstall32.Services** sections should have the same platform and operating system decorations as their related [**ClassInstall32 sections**](inf-classinstall32-section.md). For example, a **ClassInstall32.ntx86** section would have a corresponding **ClassInstall32.ntx86.Services** section.

The case-insensitive **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions can be inserted into a **ClassInstall32.Services** section name in cross-platform INF files, as shown in the formal syntax statement. For more information, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## See also


[**ClassInstall32**](inf-classinstall32-section.md)

[**AddService**](inf-addservice-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[**DelService**](inf-delservice-directive.md)

[***Models***](inf-models-section.md)

 

 






