---
title: Pattern
description: Pattern
ms.assetid: 4c9067dc-03b2-4bee-ad30-df395de357d9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Pattern


Schema Path:\\Printer.Finishing.HolePunch.Pattern

Node Type:Property

Description:This property contains all the value entries that pertain to the patterns in which holes can be punched in output pages.

The Pattern property contains two child values: **CurrentValue** and **Supported**.

### <span id="currentvalue"></span><span id="CURRENTVALUE"></span>CurrentValue

Schema Path:\\Printer.Finishing.HolePunch.Pattern:CurrentValue

Node Type:Value

Data Type:BIDI\_STRING

Description:The current (default) hole punch pattern to be applied to output pages.

The following values are allowed:

TwoHoleUSTop

ThreeHoleUS

TwoHoleDIN

FourHoleDIN

TwentyTwoHoleUS

NineteenHoleUS

TwoHoleMetric

Swedish4Hole

TwoHoleUSSide

FiveHoleUS

SevenHoleUS

Mixed7H4S

Norweg6Hole

Metric26Hole

Metric30Hole

unknown

### <span id="supported"></span><span id="SUPPORTED"></span>Supported

Schema Path:\\Printer.Finishing.HolePunch.Pattern:Supported

Node Type:Value

Data Type:BIDI\_STRING

Description:A comma-separated list of all values supported for hole punch Pattern.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Pattern%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




