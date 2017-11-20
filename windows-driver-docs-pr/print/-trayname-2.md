---
title: \ TrayName\
description: \ TrayName\
MS-HAID:
- 'autocfg\_da4a9717-e050-47a4-96d8-ca86d6e65af0.xml'
- 'print.\_trayname\_2'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: efdb5ecb-3abc-4dfd-8087-7f4f3a938cf2
---

# \[TrayName\]


Schema Path:\\Printer.Finishing.OutputBins.\[TrayName\]

Node Type:Property

Description:An IHV-mapped property name for an output tray. An IHV can map an IHV-specific tray name for an output bin with a name from the following list:

OutputBin1

OutputBin2

OutputBin*xx* (*xx* is a positive integer)

TopBin

MiddleBin

BottomBin

LargeCapacityBin

FaceUpBin

FaceDownBin

MailboxBin

The \[TrayName\] property contains three child values: Installed, Capacity, and Level.

### <span id="installed"></span><span id="INSTALLED"></span> Installed

Schema Path:\\Printer.Finishing.OutputBins.\[TrayName\]:Installed

Node Type:Value

Data Type:BIDI\_BOOL

Description:Determines whether the bin referenced by \[TrayName\] is installed on the device. If **TRUE**, that bin is installed on the device; if **FALSE**, that bin is not installed on the device.

### <span id="capacity"></span><span id="CAPACITY"></span> Capacity

Schema Path:\\Printer.Finishing.OutputBins.\[TrayName\]:Capacity

Node Type:Value

Data Type:BIDI\_INT

Description:The capacity, in sheets, of the currently referenced output bin.

### <span id="level"></span><span id="LEVEL"></span> Level

Schema Path:\\Printer.Finishing.OutputBins.\[TrayName\]:Level

Node Type:Value

Data Type:BIDI\_INT

Description:The amount of capacity remaining in the currently referenced output bin, expressed as a percentage. A full tray has a value of 100, while an empty tray has a value of 0. If the level is not measurable, a value of -1 (indicating an unknown level) should be returned.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20%5BTrayName%5D%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




