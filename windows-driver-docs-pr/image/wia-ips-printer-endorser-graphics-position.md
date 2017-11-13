---
title: WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_POSITION
description: The WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_POSITION property is used to configure the position of the image (graphics) relative to the text content to be printed/endorsed. The WIA minidriver creates and maintains this property.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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
---

# WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_POSITION


The **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_POSITION** property is used to configure the position of the image (graphics) relative to the text content to be printed/endorsed. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




