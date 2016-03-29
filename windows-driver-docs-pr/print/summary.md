---
title: Summary
description: Summary
ms.assetid: 8ed412b2-1e7c-440f-8949-a3b1fff09b16
---

# Summary


Schema Path:\\Printer.Status.Summary

Node Type:Property

Description:A brief description of the current state of the device. This provides a high-level view of the device status. Only the most important conditions are displayed.

The Summary property contains two child values: **State** and **StateReason**.

### State

Schema Path:\\Printer.Status.Summary:State

Node Type:Value

Data Type:BIDI\_STRING

Description:The processing state of the device.

The following values are allowed:

Idle

Processing

Stopped

### StateReason

Schema Path:\\Printer.Status.Summary:StateReason

Node Type:Value

Data Type:BIDI\_STRING

Description:The most important reasons for the current printer state. This value can be a list of space-delimited state reasons.

The following values are allowed:

AttentionRequired

DoorOpen

MarkerSupplyEmpty

MarkerSupplyLow

MediaEmpty

MediaJam

MediaLow

MediaNeeded

None

Paused

OutputAreaAlmostFull

OutputAreaFull

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Summary%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




