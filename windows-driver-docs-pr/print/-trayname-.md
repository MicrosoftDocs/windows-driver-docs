---
title: \ TrayName\
description: \ TrayName\
MS-HAID:
- 'autocfg\_96b829b0-c2f1-4456-b992-287746922573.xml'
- 'print.\_trayname\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7fa03413-5b95-443f-9b0f-75d82d0e41cf
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20%5BTrayName%5D%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




