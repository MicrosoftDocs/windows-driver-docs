---
title: Component
description: Contains the value entries that describe the part of the print device that is affected by the current event.
ms.date: 08/31/2021
ms.localizationpriority: medium
---

# Component

Schema Path: \\Printer.Status.Summary:Detailed.Event\#\#\#.Component

Data Type: Property

Description: This property contains the value entries that describe the part of the print device that is affected by the current event.

The Component property contains two child values: Group and Name.

## Group

Schema Path: \\Printer.Status.Summary:Detailed.Event\#\#\#.Component:Group

Node Type: Value

Data Type: BIDI_STRING

Description: The component group affected by the current event. The component group and component name (described next) are combined to determine the exact location of the problem.

The following list contains typical values for Group:

- InputBin

- MediaPath

- OutputBins

- Consumable

## Name

Schema Path: \\Printer.Status.Detailed.Event\#\#\#.Component:Name

Node Type: Value

Data Type: BIDI_STRING

Description: The name of the individual component affected by the current event. The component name and component group (above) are combined to determine the exact location of the problem.

The typical values for *Name* are as follows:

- Tray1

- TopBin

- LargeCapacityBin

- OutputBin1

- Toner.Black

- Ink.Cyan
