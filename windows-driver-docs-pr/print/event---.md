---
title: Event\ \ \
description: Event\ \ \
ms.assetid: a3b0b3f1-03d6-4309-9efe-d2588c7240cb
---

# Event\#\#\#


Schema Path:\\Printer.Status.Detailed.Event\#\#\#

Node Type:Property

Description:A generated event name based on event IDs in the device. Each number suffix should be unique for a given event. If a device reuses a particular number suffix, it should allow enough time for applications to determine whether the event previously associated with the number suffix has expired. This property contains all of the value entries that describe the event in question.

The Event\#\#\# property contains two child values, Name and Severity, and is the parent of the [Component](component2.md) property.

### <a href="" id="name"></a> Name

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

### <a href="" id="severity"></a> Severity

Schema Path:\\Printer.Status.Summary:Detailed.Event\#\#\#:Severity

Node Type:Value

Data Type:BIDI\_STRING

Description:The severity level of the current event. The printer determines the severity level assigned to an error condition.

The following values are allowed:

Informational

Warning

Critical

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Event#%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




