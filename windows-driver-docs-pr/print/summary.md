---
title: Summary property
description: A brief description of the current state of the device.
ms.date: 09/08/2021
ms.localizationpriority: medium
---

# Summary property

Schema Path: \\Printer.Status.Summary

Node Type: Property

Description: A brief description of the current state of the device. This provides a high-level view of the device status. Only the most important conditions are displayed.

The Summary property contains two child values: **State** and **StateReason**.

## State

Schema Path: \\Printer.Status.Summary:State

Node Type: Value

Data Type: BIDI_STRING

Description: The processing state of the device.

The following values are allowed:

- Idle

- Processing

- Stopped

## StateReason

Schema Path: \\Printer.Status.Summary:StateReason

Node Type: Value

Data Type: BIDI_STRING

Description: The most important reasons for the current printer state. This value can be a list of space-delimited state reasons.

The following values are allowed:

- AttentionRequired

- DoorOpen

- MarkerSupplyEmpty

- MarkerSupplyLow

- MediaEmpty

- MediaJam

- MediaLow

- MediaNeeded

- None

- Paused

- OutputAreaAlmostFull

- OutputAreaFull
