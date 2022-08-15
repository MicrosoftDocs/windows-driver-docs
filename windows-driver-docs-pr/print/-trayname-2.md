---
title: TrayName (OutputBins)
description: An IHV-mapped property name for an output tray.
ms.date: 08/31/2021
---

# TrayName (OutputBins)

Schema Path: \\Printer.Finishing.OutputBins.\[TrayName\]

Node Type: Property

Description: An IHV-mapped property name for an output tray. An IHV can map an IHV-specific tray name for an output bin with a name from the following list.

- OutputBin1

- OutputBin2

- OutputBin*xx* (*xx* is a positive integer)

- TopBin

- MiddleBin

- BottomBin

- LargeCapacityBin

- FaceUpBin

- FaceDownBin

- MailboxBin

The \[TrayName\] property contains three child values: Installed, Capacity, and Level.

## Installed

Schema Path: \\Printer.Finishing.OutputBins.\[TrayName\]:Installed

Node Type: Value

Data Type: BIDI_BOOL

Description: Determines whether the bin referenced by \[TrayName\] is installed on the device. If **TRUE**, that bin is installed on the device; if **FALSE**, that bin is not installed on the device.

## Capacity

Schema Path: \\Printer.Finishing.OutputBins.\[TrayName\]:Capacity

Node Type: Value

Data Type: BIDI_INT

Description: The capacity, in sheets, of the currently referenced output bin.

## Level

Schema Path: \\Printer.Finishing.OutputBins.\[TrayName\]:Level

Node Type: Value

Data Type: BIDI_INT

Description: The amount of capacity remaining in the currently referenced output bin, expressed as a percentage. A full tray has a value of 100, while an empty tray has a value of 0. If the level is not measurable, a value of -1 (indicating an unknown level) should be returned.
