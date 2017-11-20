---
title: Orientation
description: Orientation
MS-HAID:
- 'autocfg\_d984ee6a-7ec2-452b-837c-53133c00b94f.xml'
- 'print.orientation2'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a3bd9d67-200f-4739-ad0e-ff7fd2eb20a3
---

# Orientation


Schema Path:\\Printer.Layout.Orientation

Node Type:Property

Description:The property associated with page orientation. The value entries that are children of this property are the current page orientation and a list of page orientations supported by the device.

The Orientation property contains two child values: **CurrentValue** and **Supported**.

### <span id="currentvalue"></span><span id="CURRENTVALUE"></span> CurrentValue

Schema Path:\\Printer.Layout.Orientation:CurrentValue

Node Type:Value

Data Type:BIDI\_STRING

Description:The current (default) orientation in which pages will be printed.

Must be one of the following values.

Portrait

Landscape

ReversePortrait

ReverseLandscape

### <span id="supported"></span><span id="SUPPORTED"></span> Supported

Schema Path:\\Printer.Layout.Orientation:Supported

Node Type:Value

Data Type:BIDI\_STRING

Description:A comma-separated list of all values supported for Orientation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Orientation%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




