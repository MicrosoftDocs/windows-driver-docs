---
title: TrayName (InputBins)
description: An IHV-mapped property name for an input tray.
ms.date: 08/31/2021
ms.localizationpriority: medium
---

# TrayName (InputBins)

Schema Path: \\Printer.Layout.InputBins.\[TrayName\]

Node Type: Property

Description: An IHV-mapped property name for an input tray. An IHV can map an IHV-specific tray name for an input bin with a name from the following list.

- Tray1

- Tray2

- Trayxx (xx an arbitrary positive integer)

- TopBin

- MiddleBin

- BottomBin

- LargeCapacityBin

- ManualBin

- EnvelopeBin

- EnvelopeManual

- MultiPurposeBin

The \[TrayName\] property contains the following child values:

- Installed

- MediaSize

- MediaColor

- Capacity

- Level

## Installed

Schema Path: \\Printer.Layout.InputBins.\[TrayName\]:Installed

Node Type: Value

Data Type: BIDI_BOOL

Description: Indicates whether the bin referenced by \[TrayName\] is installed on the device. If **TRUE**, the bin is installed on the device; if **FALSE**, the bin is not installed on the device.

## MediaSize

Schema Path: \\Printer.Layout.InputBins.\[TrayName\]:MediaSize

Node Type: Value

Data Type: BIDI_STRING

Description: The size of the media available in the currently referenced input bin. The values should conform to the IEEE-ISTO PWG Standard 5101.1-2001 - Media Standardized Names.

The following values are allowed:

- na_legal_8.5x14in

- na_letter_8.5x11in

- iso_a4_210x297mm

- iso_c5_162x229mm

- iso_dl_110x220mm

- jis_b4_257x364mm

## MediaType

Schema Path: \\Printer.Layout.InputBins.\[TrayName\]:MediaType

Node Type: Value

Data Type: BIDI_STRING

Description: The type of media available in the currently referenced input bin. The values should conform to the IEEE-ISTO PWG Standard 5101.1-2001 - Media Standardized Names.

The following values are allowed:

- cardstock

- envelope

- labels

- photographic

- stationery

- stationery-inkjet

- transparency

- other

## MediaColor

Schema Path: \\Printer.Layout.InputBins.\[TrayName\]:MediaColor

Node Type: Value

Data Type: BIDI_STRING

Description: The color of the media available in the currently referenced input bin. The values should conform to the IEEE-ISTO PWG Standard 5101.1-2001 - Media Standardized Names.

The following values are allowed:

- white

- pink

- yellow

- buff

- goldenrod

- blue

- green

- red

- gray

- ivory

- orange

- no-color

- unknown

## FeedDirection

Schema Path: \\Printer.Layout.InputBins.\[TrayName\]:FeedDirection

Node Type: Value

Data Type: BIDI_STRING

Description: Indicates which edge of the paper enters the media path first in the currently referenced input bin and must be one of the following values:

- LongEdgeFirst

- ShortEdgeFirst

## Capacity

Schema Path: \\Printer.Layout.InputBins.\[TrayName\]:Capacity

Node Type: Value

Data Type: BIDI_INT

Description: The capacity, in sheets, of the currently referenced input bin.

## Level

Schema Path: \\Printer.Layout.InputBins.\[TrayName\]:Level

Node Type: Value

Data Type: BIDI_INT

Description: The amount of capacity remaining in the currently referenced input bin, expressed as a percentage. A full tray would have a value of 100, while an empty tray a value of 0. If the level is not measurable, a value of -1 (indicating an unknown Level) should be returned.
