---
title: Attributes for Device Fonts
description: Attributes for Device Fonts
ms.assetid: 748faa90-9c31-44c2-8bb3-641a1f95eab1
keywords: ["device fonts WDK Unidrv", "font attributes WDK Unidrv"]
---

# Attributes for Device Fonts


## <a href="" id="ddk-attributes-for-device-fonts-gg"></a>


The following table lists attributes describing the printer's support for device fonts.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute Name</th>
<th align="left">Attribute Parameter</th>
<th align="left">Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*CharPosition</strong></p></td>
<td align="left"><p>UPPERLEFT or BASELINE. Indicates the area of the character bounding box to which the print head should be positioned before printing a character.</p></td>
<td align="left"><p>Optional. If not specified, the default value is UPPERLEFT.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>*DefaultCTT</strong></p></td>
<td align="left"><p>Numeric value representing the RC_CTT resource identifier of the default character translation table.</p></td>
<td align="left"><p></p>
Optional. Applies only to TTY printers.
If not specified, there is no translation table. (This attribute is provided only for backward compatibility with GPC files.)</td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*DefaultFont</strong></p></td>
<td align="left"><p>Numeric value representing the RC_FONT or RC_UFM resource identifier of the default font.</p></td>
<td align="left"><p>Required if the printer supports device fonts.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>*LookAheadRegion</strong></p></td>
<td align="left"><p>Numeric (integer) value representing how far ahead the driver must &quot;look&quot; to determine whether it should emit text. This value is in <em>y</em> master units, but must be convertible to an integral number of pixels. For more information, see the comment that follows this table.</p></td>
<td align="left"><p>Optional. If not specified, the default value is zero. Used only with serial printers, (for example, HP DeskJet), for ordering text and bitmap data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*MaxFontUsePerPage</strong></p></td>
<td align="left"><p>Numeric value representing the maximum number of fonts the printer can use per page.</p></td>
<td align="left"><p>Optional. If not specified, there is no limit.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>*TextYOffset</strong></p></td>
<td align="left"><p>Numeric value representing the vertical distance, in <em>y</em> master units, by which resident fonts must be repositioned to align with bitmap font baselines.</p></td>
<td align="left"><p>Optional. If not specified, the default value is 0. (Used with some dot-matrix printers.)</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

### <a href="" id="note-on--lookaheadregion"></a>Note on \*LookAheadRegion

To determine the size of the lookahead region, the printer driver must perform an addition based on the current scan line and the value of the \***LookAheadRegion** attribute. Because the scan line is in units of pixels while \***LookAheadRegion** is in vertical master units, the driver must convert the attribute value into pixels.

For example, if the value of the \***LookAheadRegion** attribute is 600, and there are 1200 vertical master units per inch, then the size of the lookahead region one-half inch. If the current resolution is 300 dpi, one-half inch corresponds to 150 pixels (vertical), or 150 scan lines. If the printer is currently on scan line 100, the driver must look for text baselines between scan lines 100 and 250.

The driver repeats this process for each scan line, although it emits the text it finds only once.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Attributes%20for%20Device%20Fonts%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




