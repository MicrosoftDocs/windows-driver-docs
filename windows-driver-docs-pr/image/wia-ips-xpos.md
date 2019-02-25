---
title: WIA\_IPS\_XPOS
description: The WIA\_IPS\_XPOS property contains the x-coordinate, in pixels, of the upper-left corner of a selected image. The WIA minidriver creates and maintains this property.
ms.assetid: 3fa45aab-c0d0-4061-b145-795fb02c1547
keywords: ["WIA_IPS_XPOS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_XPOS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_XPOS


The WIA\_IPS\_XPOS property contains the x-coordinate, in pixels, of the upper-left corner of a selected image. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ips_xpos_si"></span><span id="DDK_WIA_IPS_XPOS_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

An application sets the WIA\_IPS\_XPOS property to mark the upper-left corner of a selection area.

WIA\_IPS\_XPOS is required for all image acquisition-enabled items and child items of these items; this property is not available for storage items or stored image items.

When a fixed page size is set, the driver has to set the [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md), WIA\_IPS\_XPOS, [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md), and [**WIA\_IPS\_YPOS**](wia-ips-ypos.md) properties to match the page size dimensions and a "0" origin. For center document alignment, the driver has to set WIA\_IPS\_XPOS to ((scan area width - document width) / 2) \* resolution \[DPI\]) and WIA\_IPS\_YPOS to ((scan area height - document height) / 2) \* resolution \[DPI\]).

When the origin or one extent is changed, the driver has to update [**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md) to CUSTOM\_SIZE and the [**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md) and [**WIA\_IPS\_PAGE\_HEIGHT**](wia-ips-page-height.md) properties to match the scan area extents. Orientation and rotation should not affect these properties, unless an orientation change (not a rotation change) renders the origin or one extent outside of the available document scan area.

A driver must also update the WIA\_IPS\_XEXTENT, WIA\_IPS\_XPOS, WIA\_IPS\_YEXTENT, and WIA\_IPS\_YPOS properties when the [**WIA\_IPS\_XRES**](wia-ips-xres.md) and [**WIA\_IPS\_YRES**](wia-ips-yres.md) properties are changed.

**Note**   Flatbed and Film child items are required to support only the WIA\_IPS\_XEXTENT, WIA\_IPS\_XPOS, WIA\_IPS\_XRES, WIA\_IPS\_YEXTENT, WIA\_IPS\_YPOS, and WIA\_IPS\_YRES properties. All other properties, required or optional for their parent (the base Flatbed or Film items), are only optional for these items. The only exceptions are the WIA\_IPA\_ITEM\_*Xxx* properties, which are required for all items.

 

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

## See also


[**WIA\_IPS\_PAGE\_HEIGHT**](wia-ips-page-height.md)

[**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md)

[**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_XRES**](wia-ips-xres.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

[**WIA\_IPS\_YRES**](wia-ips-yres.md)

 

 






