---
title: TrueGray
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TrueGray





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
<td><p><em><strong>ADTrueGray</strong>: True</p></td>
<td><p>The TrueGray feature is enabled by default for this printer.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>ADTrueGray</strong>: False</p></td>
<td><p>The TrueGray feature is disabled by default for this printer.</p></td>
</tr>
</tbody>
</table>

 

When the user interface indicates that the TrueGray feature is enabled, the driver detects RGB colors for which R = G = B, and one of the following conditions is true:

-   When ICM processing is off

-   When ICM processing is carried out on the host and the destination color profile is RGB data and the converted color is R' = G' = B' (that is, different from the original color)

-   When ICM processing would normally be done using CIE-based color spaces and the original color is R = G = B

No attempt is made to detect gray in CMYK colors. This is the color space normally used when ICM color processing is carried out on the host.

 

 




