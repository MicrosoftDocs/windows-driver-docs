---
title: Component
description: Component
ms.assetid: 15cc741e-5919-4d71-802b-519494827722
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 




