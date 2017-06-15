---
title: MOF Syntax for WMI Data and Event Blocks
author: windows-driver-content
description: MOF Syntax for WMI Data and Event Blocks
MS-HAID:
- 'WMI\_00580391-3953-448c-9602-0388b214fda2.xml'
- 'kernel.mof\_syntax\_for\_wmi\_data\_and\_event\_blocks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 247037b7-d62e-4f74-8fa4-57e74f6c412f
keywords: ["WMI WDK kernel , event blocks", "event blocks WDK WMI", "data blocks WDK WMI", "WMI WDK kernel , data blocks", "blocks WDK WMI", "MOF files WDK WMI"]
---

# MOF Syntax for WMI Data and Event Blocks


## <a href="" id="ddk-mof-syntax-for-wmi-data-and-event-blocks-kg"></a>


A driver's WMI schema describes its data blocks, which define the information that a driver can provide and the methods it can execute in response to WMI requests. A driver's schema also describes its event blocks, which are data blocks that the driver sends to WMI when a driver-determined event occurs for which a WMI client user has requested notification.

A driver writer defines a driver's schema in Managed Object Format (MOF). MOF is a compiled language created by the Desktop Management Task force (DMTF) and based on Interface Definition language (IDL). A driver's MOF file contains a MOF class definition for each data block and event block the driver exposes to WMI.

A MOF class definition for a WMI data block follows this syntax:

**\[***Required and optional class qualifiers***\]**

**class***ClassName* : *OptionalBaseClass*
**{**
**\[key, read\]**
**string InstanceName;**
**\[read\]**
**boolean Active;**
**\[** *Required and optional property qualifiers* **\]**
*datatype itemname1***;**
**\[** *Required and optional property qualifiers* **\]**
*datatype itemnameN***;**
**};**
The following topics describe the syntax elements shown above:

[WMI Class Qualifiers](wmi-class-qualifiers.md)

[WMI Class Names and Base Classes](wmi-class-names-and-base-classes.md)

[Required Items in WMI Classes](required-items-in-wmi-classes.md)

[WMI Property Qualifiers](wmi-property-qualifiers.md)

[Driver-Defined WMI Data Items](driver-defined-wmi-data-items.md)

[WMI Class Examples](wmi-class-examples.md)

For a general discussion of MOF syntax as it pertains to WMI clients and other kinds of applications, see the Microsoft Windows SDK.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20MOF%20Syntax%20for%20WMI%20Data%20and%20Event%20Blocks%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


