---
title: TrueGray
author: windows-driver-content
description: TrueGray
ms.assetid: d6fef790-79d9-4ea7-8e1d-bca8837108de
keywords:
- minidrivers WDK Pscript , TrueGray feature
- TrueGray feature
- RGB colors WDK printer
- gray color space WDK Pscript
- ADTrueGray
- color checking WDK Pscript
- checking RGB colors
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TrueGray


## <a href="" id="ddk-truegray-gg"></a>


The TrueGray feature checks RGB colors in text and vector graphics, but not in bitmaps. For colors that are gray (that is, colors whose red, green, and blue values are equal), the TrueGray feature translates the colors from the RGB color space to the color printer's gray color space before printing them. This feature is not available for monochrome printers.

The TrueGray feature uses a private [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-) keyword, \***ADTrueGray**, to allow PScript minidriver writers to enable or disable this feature.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyword and Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>*<strong>ADTrueGray</strong>: True</p></td>
<td><p>The TrueGray feature is enabled by default for this printer.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>ADTrueGray</strong>: False</p></td>
<td><p>The TrueGray feature is disabled by default for this printer.</p></td>
</tr>
</tbody>
</table>

 

When the user interface indicates that the TrueGray feature is enabled, the driver detects RGB colors for which R = G = B, and one of the following conditions is true:

-   When ICM processing is off

-   When ICM processing is carried out on the host and the destination color profile is RGB data and the converted color is R' = G' = B' (that is, different from the original color)

-   When ICM processing would normally be done using CIE-based color spaces and the original color is R = G = B

No attempt is made to detect gray in CMYK colors. This is the color space normally used when ICM color processing is carried out on the host.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20TrueGray%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


