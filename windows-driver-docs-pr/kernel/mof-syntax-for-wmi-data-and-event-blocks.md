---
title: MOF Syntax for WMI Data and Event Blocks
description: MOF Syntax for WMI Data and Event Blocks
ms.assetid: 247037b7-d62e-4f74-8fa4-57e74f6c412f
keywords: ["WMI WDK kernel , event blocks", "event blocks WDK WMI", "data blocks WDK WMI", "WMI WDK kernel , data blocks", "blocks WDK WMI", "MOF files WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# MOF Syntax for WMI Data and Event Blocks





A driver's WMI schema describes its data blocks, which define the information that a driver can provide and the methods it can execute in response to WMI requests. A driver's schema also describes its event blocks, which are data blocks that the driver sends to WMI when a driver-determined event occurs for which a WMI client user has requested notification.

A driver writer defines a driver's schema in Managed Object Format (MOF). MOF is a compiled language created by the Desktop Management Task force (DMTF) and based on Interface Definition language (IDL). A driver's MOF file contains a MOF class definition for each data block and event block the driver exposes to WMI.

A MOF class definition for a WMI data block follows this syntax:

**\[**<em>Required and optional class qualifiers</em>**\]**

**class***ClassName* : *OptionalBaseClass*
**{**
**\[key, read\]**
**string InstanceName;**
**\[read\]**
**boolean Active;**
**\[** *Required and optional property qualifiers* **\]**
<em>datatype itemname1</em>**;**
**\[** *Required and optional property qualifiers* **\]**
<em>datatype itemnameN</em>**;**
**};**
The following topics describe the syntax elements shown above:

[WMI Class Qualifiers](wmi-class-qualifiers.md)

[WMI Class Names and Base Classes](wmi-class-names-and-base-classes.md)

[Required Items in WMI Classes](required-items-in-wmi-classes.md)

[WMI Property Qualifiers](wmi-property-qualifiers.md)

[Driver-Defined WMI Data Items](driver-defined-wmi-data-items.md)

[WMI Class Examples](wmi-class-examples.md)

For a general discussion of MOF syntax as it pertains to WMI clients and other kinds of applications, see the Microsoft Windows SDK.

 

 




