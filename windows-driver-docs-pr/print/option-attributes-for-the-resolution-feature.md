---
title: Option Attributes for the Resolution Feature
author: windows-driver-content
description: Option Attributes for the Resolution Feature
MS-HAID:
- 'nt5gpd\_b424e7b3-3f8b-43fa-909e-c1738ab4c511.xml'
- 'print.option\_attributes\_for\_the\_resolution\_feature'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f04cd119-38c7-465c-b4fd-d657aa5bfacd
keywords: ["Resolution Feature"]
---

# Option Attributes for the Resolution Feature


## <a href="" id="ddk-option-attributes-for-the-resolution-feature-gg"></a>


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
<td><p>*<strong>DPI</strong></p></td>
<td><p>PAIR of numeric values representing the x and y values for the printer's resolution, in dots per inch.</p></td>
<td><p>Required. The x and y values must equal *<strong>TextDPI</strong> x and y values, or they must be equal to *<strong>TextDPI</strong> x and y values divided by a power of two. For example, if *<strong>TextDPI</strong> is PAIR(300, 300), then *<strong>DPI</strong> values might be PAIR(300, 300), PAIR(150, 150), or PAIR(75, 75), but not PAIR(100, 100).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>MinStripBlankPixels</strong></p></td>
<td><p>Numeric value representing the minimum number of blank bytes that Unidrv should encounter within a scan line before stripping enclosing blank bytes.</p></td>
<td><p>Optional. If not specified, the default value is zero. This attribute is relevant only if a *<strong>StripBlanks</strong> entry specifies ENCLOSED. See [Raster Data Emission Attributes](raster-data-emission-attributes.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>PinsPerLogPass</strong></p></td>
<td><p>Numeric value presenting the number of scan lines printed by one logical pass of the print head. Must be a multiple of *<strong>PinsPerPhysPass</strong>, since each logical pass consists of one or more physical passes.</p></td>
<td><p>Optional. If not specified, the default value is 1. Required if a printer performs interlacing, requiring multiple passes of the print head across a set of scan lines, to print all the scan lines.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>PinsPerPhysPass</strong></p></td>
<td><p>Numeric value representing the number of scan lines printed as the print head moves across the page. Must be one, or a multiple of eight.</p></td>
<td><p>Optional. If not specified, the default value is 1.</p>
<p>The horizontal and vertical resolutions should be multiples of *<strong>PinsPerPhysPass</strong>, or the output might be unpredictable.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>RequireUniDir?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the specified resolution requires unidirectional printing to be enabled.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>SpotDiameter</strong></p></td>
<td><p>Numeric value representing the spot diameter size, as a percentage of the pixel size, for the resolution specified by *<strong>DPI</strong>.</p></td>
<td><p>Required.</p>
<p>Examples:</p>
100 means the spot diameter equals the pixel size.
200 means the spot diameter is twice the pixel size.
50 means the spot diameter is half the pixel size.</td>
</tr>
<tr class="odd">
<td><p>*<strong>TextDPI</strong></p></td>
<td><p>PAIR or numeric values representing the x and y values for the printer's text resolution, in dots per inch.</p></td>
<td><p>Required. See *<strong>DPI</strong> comments. This resolution is used for drawing fonts and vector graphics.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

For information about additional option attributes, see [Option Attributes for All Features](option-attributes-for-all-features.md).

Also see [Controlling Image Quality](controlling-image-quality.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Option%20Attributes%20for%20the%20Resolution%20Feature%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


