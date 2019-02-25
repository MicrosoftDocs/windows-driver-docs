---
title: Event\ \ \
description: Event\ \ \
ms.assetid: a3b0b3f1-03d6-4309-9efe-d2588c7240cb
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Event\#\#\#


Schema Path:\\Printer.Status.Detailed.Event\#\#\#

Node Type:Property

Description:A generated event name based on event IDs in the device. Each number suffix should be unique for a given event. If a device reuses a particular number suffix, it should allow enough time for applications to determine whether the event previously associated with the number suffix has expired. This property contains all of the value entries that describe the event in question.

The Event\#\#\# property contains two child values, Name and Severity, and is the parent of the [Component](component2.md) property.

### <span id="name"></span><span id="NAME"></span> Name

Schema Path:\\Printer.Status.Detailed.Event\#\#\#:Name

Node Type:Value

Data Type:BIDI\_STRING

Description:A brief description of the current error condition. There are different event names for each component.

The typical values for Name are as follows:

CoverOpen

Jam

DoorOpen

InputTrayMissing

InputTrayMediaSizeChange

InputTrayMediaTypeChange

InputTraySupplyLow

InputTraySupplyEmpty

OutputTrayMissing

OutputTrayAlmostFull

OutputTrayFull

FuserUnderTemperature

FuserOverTemperature

ConsumableLow

ConsumableEmpty

WasteReceptacleAlmostFull

WasteReceptacleFull

### <span id="severity"></span><span id="SEVERITY"></span> Severity

Schema Path:\\Printer.Status.Summary:Detailed.Event\#\#\#:Severity

Node Type:Value

Data Type:BIDI\_STRING

Description:The severity level of the current event. The printer determines the severity level assigned to an error condition.

The following values are allowed:

Informational

Warning

Critical

 

 




