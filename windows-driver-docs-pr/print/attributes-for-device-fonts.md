---
title: Attributes for Device Fonts
description: Attributes for Device Fonts
ms.assetid: 748faa90-9c31-44c2-8bb3-641a1f95eab1
keywords:
- device fonts WDK Unidrv
- font attributes WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attributes for Device Fonts





The following table lists attributes describing the printer's support for device fonts.

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
<td><p><strong><em>CharPosition</strong></p></td>
<td><p>UPPERLEFT or BASELINE. Indicates the area of the character bounding box to which the print head should be positioned before printing a character.</p></td>
<td><p>Optional. If not specified, the default value is UPPERLEFT.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>DefaultCTT</strong></p></td>
<td><p>Numeric value representing the RC_CTT resource identifier of the default character translation table.</p></td>
<td><p></p>
Optional. Applies only to TTY printers.
If not specified, there is no translation table. (This attribute is provided only for backward compatibility with GPC files.)</td>
</tr>
<tr class="odd">
<td><p><strong><em>DefaultFont</strong></p></td>
<td><p>Numeric value representing the RC_FONT or RC_UFM resource identifier of the default font.</p></td>
<td><p>Required if the printer supports device fonts.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>LookAheadRegion</strong></p></td>
<td><p>Numeric (integer) value representing how far ahead the driver must &quot;look&quot; to determine whether it should emit text. This value is in <em>y</em> master units, but must be convertible to an integral number of pixels. For more information, see the comment that follows this table.</p></td>
<td><p>Optional. If not specified, the default value is zero. Used only with serial printers, (for example, HP DeskJet), for ordering text and bitmap data.</p></td>
</tr>
<tr class="odd">
<td><p><strong><em>MaxFontUsePerPage</strong></p></td>
<td><p>Numeric value representing the maximum number of fonts the printer can use per page.</p></td>
<td><p>Optional. If not specified, there is no limit.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>TextYOffset</strong></p></td>
<td><p>Numeric value representing the vertical distance, in <em>y</em> master units, by which resident fonts must be repositioned to align with bitmap font baselines.</p></td>
<td><p>Optional. If not specified, the default value is 0. (Used with some dot-matrix printers.)</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

### <a href="" id="note-on--lookaheadregion"></a>Note on \*LookAheadRegion

To determine the size of the lookahead region, the printer driver must perform an addition based on the current scan line and the value of the \***LookAheadRegion** attribute. Because the scan line is in units of pixels while \***LookAheadRegion** is in vertical master units, the driver must convert the attribute value into pixels.

For example, if the value of the \***LookAheadRegion** attribute is 600, and there are 1200 vertical master units per inch, then the size of the lookahead region one-half inch. If the current resolution is 300 dpi, one-half inch corresponds to 150 pixels (vertical), or 150 scan lines. If the printer is currently on scan line 100, the driver must look for text baselines between scan lines 100 and 250.

The driver repeats this process for each scan line, although it emits the text it finds only once.

 

 




