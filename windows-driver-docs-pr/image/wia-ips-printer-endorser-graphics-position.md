---
title: WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_POSITION
description: The WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_POSITION property is used to configure the position of the image (graphics) relative to the text content to be printed/endorsed. The WIA minidriver creates and maintains this property.
ms.assetid: CB7B84F0-A585-49AB-ADDE-039C2D415E72
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_POSITION


The **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_POSITION** property is used to configure the position of the image (graphics) relative to the text content to be printed/endorsed. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the constants that are valid with **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_POSITION**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_LEFT</p></td>
<td><p>The image is printed/endorsed at the left side of the of the imprinter/endorser area.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_RIGHT</p></td>
<td><p>The image is printed/endorsed at the right side of the of the imprinter/endorser area.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_TOP</p></td>
<td><p>The image is printed/endorsed at the top of the of the imprinter/endorser area.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_BOTTOM</p></td>
<td><p>The image is printed/endorsed at the bottom of the of the imprinter/endorser area.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_TOP_LEFT</p></td>
<td><p>The image is printed/endorsed at the top-left corner of the imprinter/endorser area.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_TOP_RIGHT</p></td>
<td><p>The image is printed/endorsed at the top-right corner of the imprinter/endorser area.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_BOTTOM_LEFT</p></td>
<td><p>The image is printed/endorsed at the bottom-left corner of the imprinter/endorser area.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_BOTTOM_RIGHT</p></td>
<td><p>The image is printed/endorsed at the bottom-right corner of the imprinter/endorser area.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_BACKGROUND</p></td>
<td><p>The image is printed/endorsed as background and the text is printed/endorsed over the image.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_GRAPHICS_RANDOM</p></td>
<td><p>The image is printed/endorsed at a random position chosen by the device.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINTER_ENDORSER_ GRAPHICS_DEVICE_DEFAULT</p></td>
<td><p>The image is printed/endorsed at the default (preferred) position chosen by the device.</p></td>
</tr>
</tbody>
</table>

 

The WIA\_PRINTER\_ENDORSER\_ GRAPHICS\_DEVICE\_DEFAULT value is the required default value that all Imprinter/Endorser items must support when this property is supported.

This property is required and valid for all Imprinter/Endorser items that report a value of nonzero (True) for [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS**](wia-ips-printer-endorser-graphics.md). The property is invalid otherwise.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





