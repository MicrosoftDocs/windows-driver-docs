---
title: Raster Data Emission Attributes
description: Raster Data Emission Attributes
ms.assetid: 98366b64-f96b-4275-ba25-8483abf705aa
keywords:
- data emission raster printing attributes WDK Unidrv
- emission raster printing attributes WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Raster Data Emission Attributes





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
<td><p><em><strong>CursorXAfterSendBlockData</strong></p></td>
<td><p>Constant value indicating the cursor&#39;s x-position after a block of raster data has been sent. Can be one of:</p>
AT_GRXDATA_END
AT_GRXDATA_ORIGIN
AT_CURSOR_X_ORIGIN
meaning the pixel at the start of the graphics block, the pixel after the last one in the block, or the cursor origin.</td>
<td><p>Optional. If not specified, the default value is AT_GRXDATA_END.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>CursorYAfterSendBlockData</strong></p></td>
<td><p>Constant value indicating the cursor&#39;s y-position after a block of raster data has been sent. Can be one of:</p>
NO_MOVE
AUTO_INCREMENT</td>
<td><p>Optional. If not specified, the default value is NO_MOVE, meaning the cursor&#39;s y-position is unchanged.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>MaxMultipleRowBytes</strong></p></td>
<td><p>Numeric value indicating the maximum-size raster block to use when downloading raster data on devices that set *SendMultipleRows? to <strong>TRUE</strong>.</p></td>
<td><p>The default value is 32 KB. The largest allowed value is 256 KB.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>MirrorRasterByte</strong>?</p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether Unidrv should mirror (reverse) each byte of image data.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>MirrorRasterPage?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether output is to be mirrored. When <strong>TRUE</strong>, this attribute causes everything on the page to be printed as raster, and then mirrored in the opposite direction from banding. This means that portrait pages are mirrored left to right; landscape pages are mirrored top to bottom.</p>
<p>This attribute is most useful for printing on transparencies or back-print film.</p></td>
<td><p>Optional. The default value is <strong>FALSE</strong>.</p>
<p>This attribute is a relocatable global attribute. It may appear as a root-level attribute (see <a href="root-level-only-attributes.md" data-raw-source="[Root-Level-Only Attributes](root-level-only-attributes.md)">Root-Level-Only Attributes</a>) when there are no configuration dependencies, or it may appear with *Option or *Case constructs on a per-media type basis.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>MoveToX0BeforeSetColor?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the cursor&#39;s x-coordinate must be set to zero before an explicit color selection command can be sent.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. Can be <strong>TRUE</strong> only if <em><strong>UseExpColorSelectCmd?</strong> is also <strong>TRUE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>OptimizeLeftBound?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether Unidrv should remove blanks at the left bound of each band.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td><p><em><strong>OutputDataFormat</strong></p></td>
<td><p>H_BYTE or V_BYTE, indicating whether the bits in a data byte are mapped to horizontal pixels or vertical pixels.</p></td>
<td><p>Optional. If not specified, the default value is H_BYTE.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>PreAnalysisOptions</strong></p></td>
<td><p>Numeric value, one of 0, 1, 2, 4, or 8.</p>
<p>For information about the meaning of each attribute parameter, see <a href="preanalysis-infrastructure.md" data-raw-source="[Preanalysis Infrastructure](preanalysis-infrastructure.md)">Preanalysis Infrastructure</a>.</p></td>
<td><p>Optional. If not specified, the default value is 1.</p></td>
</tr>
<tr class="even">
<td><p><em><strong>RasterSendAllData?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether Unidrv should send all raster data, including blank scan lines and blanks within scan lines.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>SendMultipleRows?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the command specified by CmdSendBlockData can send multiple blocks at one time.</p></td>
<td></td>
</tr>
<tr class="even">
<td><p><em><strong>StripBlanks</strong></p></td>
<td><p>LIST indicating which blanks in a raster data block should be stripped. Can be one or more of:</p>
LEADING
ENCLOSED
TRAILING</td>
<td><p>Optional. If not specified, Unidrv does not strip any blanks. Also see *<strong>MinStripBlankPixels</strong> in <a href="option-attributes-for-the-resolution-feature.md" data-raw-source="[Option Attributes for the Resolution Feature](option-attributes-for-the-resolution-feature.md)">Option Attributes for the Resolution Feature</a>.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>UseExpColorSelectCmd?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the printer requires explicit color selection commands, separate from color raster data.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. Dot-matrix printers require a value of <strong>TRUE</strong>.</p></td>
</tr>
</tbody>
</table>

 

For information about commands associated with raster data emission, see [Raster Data Emission Commands](raster-data-emission-commands.md).

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




