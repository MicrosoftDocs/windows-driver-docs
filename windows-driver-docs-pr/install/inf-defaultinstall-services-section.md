---
title: INF DefaultInstall.Services Section
description: A DefaultInstall.Services section contains one or more AddService directives referencing additional INF-writer-defined sections in an INF file.
ms.assetid: 2b066cf9-b6b7-42d0-b147-9b1849ff04db
keywords: ["INF DefaultInstall.Services Section Device and Driver Installation"]
topic_type:
- apiref
api_name:
- INF DefaultInstall.Services Section
api_type:
- NA
---

# INF DefaultInstall.Services Section


**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).

 

A **DefaultInstall.Services** section contains one or more [**AddService**](inf-addservice-directive.md) directives referencing additional INF-writer-defined sections in an INF file. This section is equivalent to the [**INF *DDInstall*.Services**](inf-ddinstall-services-section.md) section, and is used in association with an [**INF DefaultInstall**](inf-defaultinstall-section.md) section.

``` syntax
[DefaultInstall.Services] |
[DefaultInstall.nt.Services] |
[DefaultInstall.ntx86.Services] |
[DefaultInstall.ntia64.Services] | (Windows XP and later versions of Windows)
[DefaultInstall.ntamd64.Services]  (Windows XP and later versions of Windows)
 
AddService=ServiceName,[flags],service-install-section
                             [,event-log-install-section[,[EventLogType][,EventName]]]...]
[DelService=ServiceName[,[flags][,[EventLogType][,EventName]]]...]
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
```

## Entries


<a href="" id="addservice-servicename--flags--service-install-section"></a>**AddService=***ServiceName***,**\[*flags*\]**,***service-install-section*  

<a href="" id="-----------------------------------------------------------------------------------------event-log-install-section---eventlogtype---eventname------"></a>                                                   \[**,***event-log-install-section*\[**,**\[*EventLogType*\]\[**,**EventName\]\]\]...  
This directive references an INF-writer-defined *service-install-section* and, possibly, an *event-log-install-section* elsewhere in the INF file for the drivers of the devices covered by this [**DefaultInstall**](inf-defaultinstall-section.md) section.

For more information, see [**INF AddService Directive**](inf-addservice-directive.md).

<a href="" id="delservice-servicename---flags----eventlogtype---eventname------"></a>**DelService=***ServiceName*\[**,**\[*flags*\]\[**,**\[*EventLogType*\]\[**,***EventName*\]\]\]...  
This directive removes a previously installed service from the target computer. This directive is very rarely used.

For more information, see [**INF DelService Directive**](inf-delservice-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=***filename***.inf**\[**,***filename2***.inf**\]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, usually so is a **Needs** entry.

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=***inf-section-name*\[**,***inf-section-name*\]...  
This optional entry specifies the particular named section that must be processed during the installation of this device. Typically, such a named section is a *DDInstall***.Services** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within such a *DDInstall***.Services** section.

**Needs** entries cannot be nested. For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

Remarks
-------

The [**AddService**](inf-addservice-directive.md) directive controls how and when the services of a particular driver are loaded, any dependencies on other services or on underlying (legacy) drivers it might have, and so forth. Optionally, it can set up event-logging services for the driver as well.

**Note**  INF files use the **DefaultInstall.Services** section only if they also use an [**INF DefaultInstall**](inf-defaultinstall-section.md) section. Otherwise, they use [**INF *DDInstall*.Services**](inf-ddinstall-services-section.md) sections together with [**INF *DDInstall***](inf-ddinstall-section.md) sections.

 

**DefaultInstall.Services** sections should have the same platform and operating system decorations as their related **DefaultInstall** sections. For example, a **DefaultInstall.ntx86** section would have a corresponding **DefaultInstall.ntx86.Services** section. For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Examples
--------

See the examples provided for the [**INF *DDInstall*.Services**](inf-ddinstall-services-section.md) section.

## See also


[***DDInstall***](inf-ddinstall-section.md)

[**DefaultInstall**](inf-defaultinstall-section.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20DefaultInstall.Services%20Section%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





