---
title: Printer Capability Attributes
description: Printer Capability Attributes
ms.assetid: 3ee98eee-8f46-4bf0-ac2c-f47f8402fa86
keywords:
- printer capability attributes WDK Unidrv
- general printer attributes WDK Unidrv , printer capability
- capability attributes WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Capability Attributes





Printer capability attributes are [general printing attributes](general-printing-attributes.md) that specify such printer characteristics as page margin, rotation, and text printing capabilities that affect all paper sizes and orientations.

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
<td><p><em><strong>MemoryUsage</strong></p></td>
<td><p></p>
LIST of constants indicating the types of data that are stored in printer memory. Can be one or more of:
FONT
RASTER
VECTOR
<p>If a data type is listed but not supported by the printer, it is ignored.</p></td>
<td><p>Optional. If not specified, the default value is LIST(FONT, RASTER, VECTOR). For more information, see <a href="describing-printer-memory-configurations.md" data-raw-source="[Describing Printer Memory Configurations](describing-printer-memory-configurations.md)">Describing Printer Memory Configurations</a>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>OEMCustomData</strong></p></td>
<td><p>Quoted text string to be supplied to a <a href="rendering-plug-ins.md" data-raw-source="[rendering plug-in](rendering-plug-ins.md)">rendering plug-in</a> when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff553128" data-raw-source="[&lt;strong&gt;IPrintOemDriverUni::DrvGetGPDData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553128)"><strong>IPrintOemDriverUni::DrvGetGPDData</strong></a>.</p></td>
<td><p>Required if a rendering plug-in calls <strong>IPrintOemDriverUni::DrvGetGPDData</strong>.</p>
<p>Interpretation of text string contents is determined by the rendering plug-in.</p>
<p>This attribute is a relocatable global attribute; it may be placed at the root level (see <a href="root-level-only-attributes.md" data-raw-source="[Root-Level-Only Attributes](root-level-only-attributes.md)">Root-Level-Only Attributes</a>) to signify that it has no dependency on printer configuration, or it may appear with <em>Option or *Case constructs if there is some dependency.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>OutputOrderReversed?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether multipage documents are sorted from last page to first.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p>
<p>The EXTERN_GLOBAL symbol should not be used with <em><strong>OutputOrderReversed?</strong>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>ReselectFont</strong></p></td>
<td><p></p>
LIST of constants indicating operations after which Unidrv must reselect the current font. Can be on of the following:
AFTER_GRXDATA - After any CmdSend<em>Xxxx</em>Data <a href="raster-data-emission-commands.md" data-raw-source="[raster data emission commands](raster-data-emission-commands.md)">raster data emission commands</a>.
AFTER_XMOVE - After any x-movement <a href="cursor-commands.md" data-raw-source="[cursor commands](cursor-commands.md)">cursor commands</a>.
AFTER_FF - After the CmdFF command.</td>
<td><p>Optional. If not specified, Unidrv does not reselect fonts.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>ReverseBandOrderForEvenPages?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether reverse banding is enabled. This attribute is used to support printers with auto-duplex capability; that is, printers that are able to print on both sides of a sheet of paper.</p>
<p>The section following this table contains more information.</p></td>
<td><p>The default value of this attribute is <strong>FALSE</strong>. Setting this attribute to <strong>TRUE</strong> enables reverse banding order.</p>
<p>This attribute is a relocatable global attribute; it may be placed at the root level (see <a href="root-level-only-attributes.md" data-raw-source="[Root-Level-Only Attributes](root-level-only-attributes.md)">Root-Level-Only Attributes</a>) to signify that it has no dependency on printer configuration, or it may appear with *Option or *Case constructs if there is some dependency.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>RotateCoordinate?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the printer supports commands to rotate the coordinate system to match the page orientation.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. If <strong>TRUE</strong>, <em>Option entries for the Orientation feature must specify printer commands. Cannot be placed in a <a href="conditional-statements.md" data-raw-source="[&lt;/em&gt;Case](conditional-statements.md)"></em>Case</a> entry.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>RotateFont?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the printer automatically rotates fonts to match the page orientation.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. If <strong>TRUE</strong>, then *<strong>RotateCoordinate?</strong> must also be <strong>TRUE</strong>. Cannot be placed in a *Case entry.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>RotateRaster?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the printer automatically rotates raster data to match the page orientation.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. If <strong>TRUE</strong>, then <em><strong>RotateCoordinate?</strong> must also be <strong>TRUE</strong>. Cannot be placed in a *Case entry.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>TextCaps</strong></p></td>
<td><p>LIST of constants indicating the printer&#39;s text capabilities. Can consist of one or more of the TC_<em>xxx</em> flags described in the Microosft Windows SDK documentation&#39;s description of <strong>GetDeviceCaps</strong>.</p></td>
<td><p>Optional. If not specified, Unidrv assumes no text capabilities are supported.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

### <a href="" id="additional-information-about--reversebandorderforevenpages-"></a>Additional information about \*ReverseBandOrderForEvenPages?

A side effect of the auto-duplex capability is that the bottom edge of a page that has just been printed is fed back into the printer, to become the top edge of the next page. To maintain the orientation of the second page relative to the first, the raster image of the second page must be sent to the printer in reverse order. In other words, if the printer printed the front side by sending the top scan line first, it must print the back side bottom scan line first.

When \***ReverseBandOrderForEvenPages?** is **TRUE** and duplexing is on, Unidrv enumerates each band in reverse order for even-numbered pages (the back sides of odd-numbered pages). The OEM rendering plug-in needs to cache only one band of data before sending it to the printer. The order of the scan lines within each band is not reversed, so the plug-in must still handle that task, and it must also reverse the order of the bits within each scan line. Although this is extra work for the plug-in, the advantage is that the plug-in does not need to cache any raster data and can begin sending data to the printer immediately.

**Note**  The \***ReverseBandOrderForEvenPages?** attribute is evaluated only when duplexing is set to "Flip on Long Edge". This attribute is ignored when duplexing is set to "Flip on Short Edge".

 

Both the value of the \***ReverseBandOrderForEvenPages?** attribute and the driver-simulated rotation affect the way bands are enumerated, which is shown in the following table. The band enumeration order specified in the column headed with **TRUE** applies when \***ReverseBandOrderForEvenPages?** is **TRUE**, and duplexing is selected, and the page to be printed is the second (or back) side. Otherwise the column headed with **FALSE** applies.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Driver-Simulated Rotation</th>
<th><strong>TRUE</strong> and Even Page</th>
<th><strong>FALSE</strong> or Odd Page</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CCW_ROTATE90</p></td>
<td><p>SW_LTOR</p></td>
<td><p>SW_RTOL</p></td>
</tr>
<tr class="even">
<td><p>CCW_ROTATE270</p></td>
<td><p>SW_RTOL</p></td>
<td><p>SW_LTOR</p></td>
</tr>
<tr class="odd">
<td><p>No Rotation</p></td>
<td><p>SW_UP</p></td>
<td><p>SW_DOWN</p></td>
</tr>
</tbody>
</table>

 

Legend: SW\_LTOR = Left To Right, SW\_RTOL = Right To Left, SW\_UP = Bottom To Top, SW\_DOWN = Top To Bottom.

An OEM rendering plug-in can support auto-duplexing without using the \***ReverseBandOrderForEvenPages?** attribute. The plug-in can do so by simply caching all of the data for the entire page and sending it to the printer, beginning with the bottom scan line. That scan line, as well as all the others on that page, must be sent in reverse order.

**Note**   The OEM rendering plug-in is responsible for reversing the order of the bits with each scan line and the order of the scan lines with each band as it sends the data to the printer. To determine when this must be done, the value of the PageNumber standard variable can be obtained by making a call to [**IPrintOemDriverUni::DrvGetStandardVariable**](https://msdn.microsoft.com/library/windows/hardware/ff553129), using the index SVI\_PAGENUMBER. If the page number is odd, no reversing is needed. If the number is even and duplexing is selected, reversing is needed.

 

 

 




