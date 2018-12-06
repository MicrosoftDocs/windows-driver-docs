---
title: \ TrayName\
description: \ TrayName\
ms.assetid: 7fa03413-5b95-443f-9b0f-75d82d0e41cf
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# \[TrayName\]


Schema Path:\\Printer.Layout.InputBins.\[TrayName\]

Node Type:Property

Description:An IHV-mapped property name for an input tray. An IHV can map an IHV-specific tray name for an input bin with a name from the following list.

Tray1

Tray2

Trayxx (xx an arbitrary positive integer)

TopBin

MiddleBin

BottomBin

LargeCapacityBin

ManualBin

EnvelopeBin

EnvelopeManual

MultiPurposeBin

The \[TrayName\] property contains the following child values:

Installed

MediaSize

MediaColor

Capacity

Level

### <span id="installed"></span><span id="INSTALLED"></span> Installed

Schema Path:\\Printer.Layout.InputBins.\[TrayName\]:Installed

Node Type:Value

Data Type:BIDI\_BOOL

Description:Indicates whether the bin referenced by \[TrayName\] is installed on the device. If **TRUE**, the bin is installed on the device; if **FALSE**, the bin is not installed on the device.

### <span id="mediasize"></span><span id="MEDIASIZE"></span> MediaSize

Schema Path:\\Printer.Layout.InputBins.\[TrayName\]:MediaSize

Node Type:Value

Data Type:BIDI\_STRING

Description:The size of the media available in the currently referenced input bin. The values should conform to the IEEE-ISTO PWG Standard 5101.1-2001 - Media Standardized Names.
The following values are allowed:
na\_legal\_8.5x14in

na\_letter\_8.5x11in

iso\_a4\_210x297mm

iso\_c5\_162x229mm

iso\_dl\_110x220mm

jis\_b4\_257x364mm

### <span id="mediatype"></span><span id="MEDIATYPE"></span> MediaType

Schema Path:\\Printer.Layout.InputBins.\[TrayName\]:MediaType

Node Type:Value

Data Type:BIDI\_STRING

Description:The type of media available in the currently referenced input bin. The values should conform to the IEEE-ISTO PWG Standard 5101.1-2001 - Media Standardized Names.
The following values are allowed:
cardstock

envelope

labels

photographic

stationery

stationery-inkjet

transparency

other

### <span id="mediacolor"></span><span id="MEDIACOLOR"></span> MediaColor

Schema Path:\\Printer.Layout.InputBins.\[TrayName\]:MediaColor

Node Type:Value

Data Type:BIDI\_STRING

Description:The color of the media available in the currently referenced input bin. The values should conform to the IEEE-ISTO PWG Standard 5101.1-2001 - Media Standardized Names.
The following values are allowed:
white

pink

yellow

buff

goldenrod

blue

green

red

gray

ivory

orange

no-color

unknown

### <span id="feeddirection"></span><span id="FEEDDIRECTION"></span> FeedDirection

Schema Path:\\Printer.Layout.InputBins.\[TrayName\]:FeedDirection

Node Type:Value

Data Type:BIDI\_STRING

Description:Indicates which edge of the paper enters the media path first in the currently referenced input bin and must be one of the following values:

LongEdgeFirst

ShortEdgeFirst

### <span id="capacity"></span><span id="CAPACITY"></span> Capacity

Schema Path:\\Printer.Layout.InputBins.\[TrayName\]:Capacity

Node Type:Value

Data Type:BIDI\_INT

Description:The capacity, in sheets, of the currently referenced input bin.

### <span id="level"></span><span id="LEVEL"></span> Level

Schema Path:\\Printer.Layout.InputBins.\[TrayName\]:Level

Node Type:Value

Data Type:BIDI\_INT

Description:The amount of capacity remaining in the currently referenced input bin, expressed as a percentage. A full tray would have a value of 100, while an empty tray a value of 0. If the level is not measurable, a value of -1 (indicating an unknown Level) should be returned.

 

 




