---
title: WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_HEIGHT
description: The WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_HEIGHT property along with WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_HEIGHT, WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_WIDTH, and WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_WIDTH are used to report the minimum and maximum dimensions, in pixels, of the images that can be uploaded to the Imprinter/Endorser to be rendered. The WIA minidriver creates and maintains this property.
ms.assetid: 96010EAE-835D-48F7-8EB4-27BAF05252A0
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_HEIGHT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_HEIGHT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_HEIGHT


The **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_HEIGHT** property along with [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_HEIGHT**](wia-ips-printer-endorser-graphics-min-height.md), [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_WIDTH**](wia-ips-printer-endorser-graphics-max-width.md), and [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_WIDTH**](wia-ips-printer-endorser-graphics-min-width.md) are used to report the minimum and maximum dimensions, in pixels, of the images that can be uploaded to the Imprinter/Endorser to be rendered. The WIA minidriver creates and maintains this property.




Property Type: VT\_UI4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The value reported for [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_HEIGHT**](wia-ips-printer-endorser-graphics-min-height.md) must be less than or equal to the value reported for **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_HEIGHT**. The value reported for[**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_WIDTH**](wia-ips-printer-endorser-graphics-min-width.md) must be less than or equal to the value reported for [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_WIDTH**](wia-ips-printer-endorser-graphics-max-width.md). The WIA minidriver can report a 0 value for all these properties to indicate that images of any size are accepted.

If nonzero values are reported, the WIA application client should not attempt and must not expect success in uploading an image that is smaller than the minimum or larger than the maximum sizes reported by the WIA minidriver through these properties. The WIA minidriver must fail image upload requests when the image size doesn't match the supported range.

This property is required and valid for all Imprinter/Endorser items that report a nonzero value (True) for [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS**](wia-ips-printer-endorser-graphics.md). These properties are invalid otherwise.

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

 

 





