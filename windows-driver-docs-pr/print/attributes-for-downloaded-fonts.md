---
title: Attributes for Downloaded Fonts
description: Attributes for Downloaded Fonts
ms.assetid: 335413d0-cf0a-4dd9-b1a4-345945c63395
keywords:
- downloaded font attributes WDK Unidrv
- font attributes WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attributes for Downloaded Fonts





The following table lists attributes describing the printer's support for downloaded fonts.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute Name</th>
<th>Attribute Parameter</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong><em>DLSymbolSet</strong></p></td>
<td><p>Constant that represents the symbol set to be used when downloading TrueType fonts. Can be either PC-8 or ROMAN-8.</p></td>
<td><p>Optional. If not specified, the glyph range is assumed to be contiguous within limits specified by *<strong>MinGlyphID</strong> and *<strong>MaxGlyphID</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>FontFormat</strong></p></td>
<td><p></p>
Constant value indicating the type of downloading supported. Must be one of the following:
HPPCL
HPPCL_RES
HPPCL_OUTLINE
OEM_CALLBACK</td>
<td><p>Required if the printer can download fonts. If OEM_CALLBACK is specified, font callback functions must be provided. For more information about these callbacks, see <a href="customizing-microsoft-s-printer-drivers.md" data-raw-source="[Customizing Microsoft&#39;s Printer Drivers](customizing-microsoft-s-printer-drivers.md)">Customizing Microsoft&#39;s Printer Drivers</a>.</p></td>
</tr>
<tr class="odd">
<td><p><strong><em>MaxFontID</strong></p></td>
<td><p>Numeric value representing the maximum identifier for soft fonts.</p></td>
<td><p>Optional. If not specified, the default value is 65535.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>MaxGlyphID</strong></p></td>
<td><p>Numeric value representing the maximum identifier for downloaded font glyphs.</p></td>
<td><p>Optional. If not specified and <em><strong>DLSymbolSet</strong> is not specified, the default value is 255. Ignored if *<strong>DLSymbolSet</strong> is specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong></em>MaxNumDownFonts</strong></p></td>
<td><p>Numeric value representing the maximum number of soft fonts that can be stored in printer memory at one time.</p></td>
<td><p>Optional. If not specified, Unidrv assumes an unlimited number of soft fonts can be stored.</p></td>
</tr>
<tr class="even">
<td><p><strong><em>MinFontID</strong></p></td>
<td><p>Numeric value representing the minimum identifier for soft fonts.</p></td>
<td><p>Optional. If not specified, the default value is one.</p></td>
</tr>
<tr class="odd">
<td><p><strong></em>MinGlyphID</strong></p></td>
<td><p>Numeric value representing the minimum identifier for downloaded font glyphs.</p></td>
<td><p>Optional. If not specified and <em><strong>DLSymbolSet</strong> is not specified, the default value is 32. Ignored if *<strong>DLSymbolSet</strong> is specified.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>TextHalftoneThreshold</strong></p></td>
<td><p>Numeric value that determines whether Unidrv performs text halftoning for TrueType fonts. If the driver&#39;s resolution is greater than or equal to the value specified in this attribute, Unidrv halftones text.</p></td>
<td><p>Optional. The default value is 600.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




