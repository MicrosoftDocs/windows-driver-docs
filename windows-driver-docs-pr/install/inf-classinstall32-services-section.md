---
title: INF ClassInstall32.Services Section
description: A ClassInstall32 section installs a new device setup class (and possibly a class installer) for devices in the new class.
ms.assetid: 602cf407-f3c0-4342-9e59-87481a0f41ef
keywords: ["INF ClassInstall32.Services Section Device and Driver Installation"]
topic_type:
- apiref
api_name:
- INF ClassInstall32.Services Section
api_type:
- NA
---

# INF ClassInstall32.Services Section


**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).

 

A **ClassInstall32** section installs a new [device setup class](device-setup-classes.md) (and possibly a class installer) for devices in the new class.

``` syntax
[ClassInstall32.Services] | 
[ClassInstall32.nt.Services] | 
[ClassInstall32.ntx86.Services] | 
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


<a href="" id="addservice-servicename--flags--service-install-section"></a>**AddService=***ServiceName*,\[*flags*\]**,***service-install-section*  

<a href="" id="----------------------------------------event-log-install-section---eventlogtype---eventname------"></a>                                      \[**,***event-log-install-section*\[**,**\[*EventLogType*\]\[**,***EventName*\]\]\]...  
This directive references an INF-writer-defined service-install-section and, possibly, an event-log-install-section elsewhere in the INF file for the drivers of the device class covered by the [**ClassInstall32**](inf-classinstall32-section.md) section. For more information, see [**INF AddService Directive**](inf-addservice-directive.md).

<a href="" id="delservice-servicename---flags----eventlogtype---eventname------"></a>**DelService=***ServiceName*\[**,**\[*flags*\]\[**,**\[*EventLogType*\]\[**,***EventName*\]\]\]...  
This directive removes a previously installed service from the target computer. This directive is very rarely used. For more information, see [**INF DelService Directive**](inf-delservice-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=***filename***.inf**\[**,***filename2***.inf**\]...  
This optional entry specifies one or more additional system-supplied named INF files that contain sections needed to install this device class. If this entry is specified, usually so is a **Needs** entry.

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=***inf-section-name*\[**,***inf-section-name*\]...  
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20ClassInstall32.Services%20Section%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





