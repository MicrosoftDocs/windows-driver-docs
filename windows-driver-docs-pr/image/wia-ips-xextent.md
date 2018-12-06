---
title: WIA\_IPS\_XEXTENT
description: The WIA\_IPS\_XEXTENT property contains the current width, in pixels, of a selected image to acquire.
ms.assetid: 00e8f705-5c2a-40ac-8635-b21a5d3315a3
keywords: ["WIA_IPS_XEXTENT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_XEXTENT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_XEXTENT


The WIA\_IPS\_XEXTENT property contains the current width, in pixels, of a selected image to acquire.

## <span id="ddk_wia_ips_xextent_si"></span><span id="DDK_WIA_IPS_XEXTENT_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

An application sets the WIA\_IPS\_XEXTENT property to mark the upper-left corner (that is, the width) of the selection area to acquire. The minidriver creates and maintains this property.

WIA\_IPS\_XEXTENT is required for all image acquisition enabled items and child items of these items; this property is not available for storage items or stored image items.

When a fixed page size is set, the driver has to set the WIA\_IPS\_XEXTENT, [**WIA\_IPS\_XPOS**](wia-ips-xpos.md), [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md), and [**WIA\_IPS\_YPOS**](wia-ips-ypos.md) properties to match the page size dimensions and a "0" origin. For center document alignment, the driver has to set WIA\_IPS\_XPOS to ((scan area width - document width) / 2) \* resolution \[DPI\]) and WIA\_IPS\_YPOS to ((scan area height - document height) / 2) \* resolution \[DPI\]).

When the origin or one extent is changed, the driver has to update the [**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md) property to CUSTOM\_SIZE and the [**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md) and [**WIA\_IPS\_PAGE\_HEIGHT**](wia-ips-page-height.md) properties to match the scan area extents. Orientation and rotation should not affect these properties, unless an orientation change (not a rotation change) renders the origin or one extent outside of the available document scan area.

A driver must also to update the WIA\_IPS\_XEXTENT, WIA\_IPS\_XPOS, WIA\_IPS\_YEXTENT, and WIA\_IPS\_YPOS properties when [**WIA\_IPS\_XRES**](wia-ips-xres.md) and [**WIA\_IPS\_YRES**](wia-ips-yres.md) are changed.

**Note**   Flatbed and Film child items must support only the WIA\_IPS\_XEXTENT, WIA\_IPS\_XPOS, WIA\_IPS\_XRES, WIA\_IPS\_YEXTENT, WIA\_IPS\_YPOS, and WIA\_IPS\_YRES properties. All other properties, required or optional for their parent (the base Flatbed or Film items), are only optional for these items. The only exceptions are the WIA\_IPA\_ITEM\_*Xxx* properties, which are required for all items.

 

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


[**WIA\_IPA\_PIXELS\_PER\_LINE**](wia-ipa-pixels-per-line.md)

[**WIA\_IPS\_PAGE\_HEIGHT**](wia-ips-page-height.md)

[**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md)

[**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_XRES**](wia-ips-xres.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

[**WIA\_IPS\_YRES**](wia-ips-yres.md)

 

 






