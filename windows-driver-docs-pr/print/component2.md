---
title: Component
author: windows-driver-content
description: Component
ms.assetid: 15cc741e-5919-4d71-802b-519494827722
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Component


Schema Path:\\Printer.Status.Summary:Detailed.Event\#\#\#.Component

Data Type:Property

Description:This property contains the value entries that describe the part of the print device that is affected by the current event.

The Component property contains two child values: Group and Name.

### <span id="group"></span><span id="GROUP"></span> Group

Schema Path:\\Printer.Status.Summary:Detailed.Event\#\#\#.Component:Group

Node Type:Value

Data Type:BIDI\_STRING

Description:The component group affected by the current event. The component group and component name (described next) are combined to determine the exact location of the problem. The following list contains typical values for Group:

InputBin

MediaPath

OutputBins

Consumable

### <span id="name"></span><span id="NAME"></span> Name

Schema Path:\\Printer.Status.Detailed.Event\#\#\#.Component:Name

Node Type:Value

Data Type:BIDI\_STRING

Description:The name of the individual component affected by the current event. The component name and component group (above) are combined to determine the exact location of the problem.

The typical values for *Name* are as follows:

Tray1

TopBin

LargeCapacityBin

OutputBin1

Toner.Black

Ink.Cyan

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Component%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


