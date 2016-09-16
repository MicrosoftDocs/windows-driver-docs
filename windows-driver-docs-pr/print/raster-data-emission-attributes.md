---
title: Raster Data Emission Attributes
author: windows-driver-content
description: Raster Data Emission Attributes
MS-HAID:
- 'nt5gpd\_27aa6f7d-cea8-408e-8e7c-262167fc2e42.xml'
- 'print.raster\_data\_emission\_attributes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 98366b64-f96b-4275-ba25-8483abf705aa
keywords: ["data emission raster printing attributes WDK Unidrv", "emission raster printing attributes WDK Unidrv"]
---

# Raster Data Emission Attributes


## <a href="" id="ddk-raster-data-emission-attributes-gg"></a>


The following table lists attributes describing the printer's support for raster data emission.

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
<td><p>*<strong>CursorXAfterSendBlockData</strong></p></td>
<td><p>Constant value indicating the cursor's x-position after a block of raster data has been sent. Can be one of:</p>
AT_GRXDATA_END
AT_GRXDATA_ORIGIN
AT_CURSOR_X_ORIGIN
meaning the pixel at the start of the graphics block, the pixel after the last one in the block, or the cursor origin.</td>
<td><p>Optional. If not specified, the default value is AT_GRXDATA_END.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>CursorYAfterSendBlockData</strong></p></td>
<td><p>Constant value indicating the cursor's y-position after a block of raster data has been sent. Can be one of:</p>
NO_MOVE
AUTO_INCREMENT</td>
<td><p>Optional. If not specified, the default value is NO_MOVE, meaning the cursor's y-position is unchanged.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>MaxMultipleRowBytes</strong></p></td>
<td><p>Numeric value indicating the maximum-size raster block to use when downloading raster data on devices that set *SendMultipleRows? to <strong>TRUE</strong>.</p></td>
<td><p>The default value is 32 KB. The largest allowed value is 256 KB.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>MirrorRasterByte</strong>?</p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether Unidrv should mirror (reverse) each byte of image data.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>MirrorRasterPage?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether output is to be mirrored. When <strong>TRUE</strong>, this attribute causes everything on the page to be printed as raster, and then mirrored in the opposite direction from banding. This means that portrait pages are mirrored left to right; landscape pages are mirrored top to bottom.</p>
<p>This attribute is most useful for printing on transparencies or back-print film.</p></td>
<td><p>Optional. The default value is <strong>FALSE</strong>.</p>
<p>This attribute is a relocatable global attribute. It may appear as a root-level attribute (see [Root-Level-Only Attributes](root-level-only-attributes.md)) when there are no configuration dependencies, or it may appear with *Option or *Case constructs on a per-media type basis.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>MoveToX0BeforeSetColor?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the cursor's x-coordinate must be set to zero before an explicit color selection command can be sent.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. Can be <strong>TRUE</strong> only if *<strong>UseExpColorSelectCmd?</strong> is also <strong>TRUE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>OptimizeLeftBound?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether Unidrv should remove blanks at the left bound of each band.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>OutputDataFormat</strong></p></td>
<td><p>H_BYTE or V_BYTE, indicating whether the bits in a data byte are mapped to horizontal pixels or vertical pixels.</p></td>
<td><p>Optional. If not specified, the default value is H_BYTE.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>PreAnalysisOptions</strong></p></td>
<td><p>Numeric value, one of 0, 1, 2, 4, or 8.</p>
<p>For information about the meaning of each attribute parameter, see [Preanalysis Infrastructure](preanalysis-infrastructure.md).</p></td>
<td><p>Optional. If not specified, the default value is 1.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>RasterSendAllData?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether Unidrv should send all raster data, including blank scan lines and blanks within scan lines.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>SendMultipleRows?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the command specified by CmdSendBlockData can send multiple blocks at one time.</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>*<strong>StripBlanks</strong></p></td>
<td><p>LIST indicating which blanks in a raster data block should be stripped. Can be one or more of:</p>
LEADING
ENCLOSED
TRAILING</td>
<td><p>Optional. If not specified, Unidrv does not strip any blanks. Also see *<strong>MinStripBlankPixels</strong> in [Option Attributes for the Resolution Feature](option-attributes-for-the-resolution-feature.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>UseExpColorSelectCmd?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the printer requires explicit color selection commands, separate from color raster data.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. Dot-matrix printers require a value of <strong>TRUE</strong>.</p></td>
</tr>
</tbody>
</table>

 

For information about commands associated with raster data emission, see [Raster Data Emission Commands](raster-data-emission-commands.md).

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Raster%20Data%20Emission%20Attributes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


