---
title: Summary
description: Summary
ms.assetid: 8ed412b2-1e7c-440f-8949-a3b1fff09b16
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Summary


Schema Path:\\Printer.Status.Summary

Node Type:Property

Description:A brief description of the current state of the device. This provides a high-level view of the device status. Only the most important conditions are displayed.

The Summary property contains two child values: **State** and **StateReason**.

### <span id="state"></span><span id="STATE"></span>State

Schema Path:\\Printer.Status.Summary:State

Node Type:Value

Data Type:BIDI\_STRING

Description:The processing state of the device.

The following values are allowed:

Idle

Processing

Stopped

### <span id="statereason"></span><span id="STATEREASON"></span>StateReason

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

 

 




