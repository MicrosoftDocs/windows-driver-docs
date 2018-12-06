---
title: Option Attributes for the Resolution Feature
description: Option Attributes for the Resolution Feature
ms.assetid: f04cd119-38c7-465c-b4fd-d657aa5bfacd
keywords:
- Resolution Feature
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Option Attributes for the Resolution Feature





The following table lists the attributes associated with the Resolution feature. For more information about the Resolution feature, see [Standard Features](standard-features.md).

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
<td><p><em><strong>DPI</strong></p></td>
<td><p>PAIR of numeric values representing the x and y values for the printer&#39;s resolution, in dots per inch.</p></td>
<td><p>Required. The x and y values must equal *<strong>TextDPI</strong> x and y values, or they must be equal to *<strong>TextDPI</strong> x and y values divided by a power of two. For example, if *<strong>TextDPI</strong> is PAIR(300, 300), then *<strong>DPI</strong> values might be PAIR(300, 300), PAIR(150, 150), or PAIR(75, 75), but not PAIR(100, 100).</p></td>
</tr>
<tr class="even">
<td><p></em><strong>MinStripBlankPixels</strong></p></td>
<td><p>Numeric value representing the minimum number of blank bytes that Unidrv should encounter within a scan line before stripping enclosing blank bytes.</p></td>
<td><p>Optional. If not specified, the default value is zero. This attribute is relevant only if a <em><strong>StripBlanks</strong> entry specifies ENCLOSED. See <a href="raster-data-emission-attributes.md" data-raw-source="[Raster Data Emission Attributes](raster-data-emission-attributes.md)">Raster Data Emission Attributes</a>.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>PinsPerLogPass</strong></p></td>
<td><p>Numeric value presenting the number of scan lines printed by one logical pass of the print head. Must be a multiple of <em><strong>PinsPerPhysPass</strong>, since each logical pass consists of one or more physical passes.</p></td>
<td><p>Optional. If not specified, the default value is 1. Required if a printer performs interlacing, requiring multiple passes of the print head across a set of scan lines, to print all the scan lines.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>PinsPerPhysPass</strong></p></td>
<td><p>Numeric value representing the number of scan lines printed as the print head moves across the page. Must be one, or a multiple of eight.</p></td>
<td><p>Optional. If not specified, the default value is 1.</p>
<p>The horizontal and vertical resolutions should be multiples of <em><strong>PinsPerPhysPass</strong>, or the output might be unpredictable.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>RequireUniDir?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the specified resolution requires unidirectional printing to be enabled.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td><p><em><strong>SpotDiameter</strong></p></td>
<td><p>Numeric value representing the spot diameter size, as a percentage of the pixel size, for the resolution specified by *<strong>DPI</strong>.</p></td>
<td><p>Required.</p>
<p>Examples:</p>
100 means the spot diameter equals the pixel size.
200 means the spot diameter is twice the pixel size.
50 means the spot diameter is half the pixel size.</td>
</tr>
<tr class="odd">
<td><p></em><strong>TextDPI</strong></p></td>
<td><p>PAIR or numeric values representing the x and y values for the printer&#39;s text resolution, in dots per inch.</p></td>
<td><p>Required. See *<strong>DPI</strong> comments. This resolution is used for drawing fonts and vector graphics.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

For information about additional option attributes, see [Option Attributes for All Features](option-attributes-for-all-features.md).

Also see [Controlling Image Quality](controlling-image-quality.md).

 

 




