---
title: WIA_IPS_XEXTENT
description: The WIA_IPS_XEXTENT property contains the current width, in pixels, of a selected image to acquire.
keywords: ["WIA_IPS_XEXTENT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_XEXTENT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPS_XEXTENT

The WIA_IPS_XEXTENT property contains the current width, in pixels, of a selected image to acquire.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

An application sets the WIA_IPS_XEXTENT property to mark the upper-left corner (that is, the width) of the selection area to acquire. The minidriver creates and maintains this property.

WIA_IPS_XEXTENT is required for all image acquisition enabled items and child items of these items; this property is not available for storage items or stored image items.

When a fixed page size is set, the driver has to set the WIA_IPS_XEXTENT, [**WIA_IPS_XPOS**](wia-ips-xpos.md), [**WIA_IPS_YEXTENT**](wia-ips-yextent.md), and [**WIA_IPS_YPOS**](wia-ips-ypos.md) properties to match the page size dimensions and a "0" origin. For center document alignment, the driver has to set WIA_IPS_XPOS to ((scan area width - document width) / 2) \* resolution \[DPI\]) and WIA_IPS_YPOS to ((scan area height - document height) / 2) \* resolution \[DPI\]).

When the origin or one extent is changed, the driver has to update the [**WIA_IPS_PAGE_SIZE**](wia-ips-page-size.md) property to CUSTOM_SIZE and the [**WIA_IPS_PAGE_WIDTH**](wia-ips-page-width.md) and [**WIA_IPS_PAGE_HEIGHT**](wia-ips-page-height.md) properties to match the scan area extents. Orientation and rotation should not affect these properties, unless an orientation change (not a rotation change) renders the origin or one extent outside of the available document scan area.

A driver must also to update the WIA_IPS_XEXTENT, WIA_IPS_XPOS, WIA_IPS_YEXTENT, and WIA_IPS_YPOS properties when [**WIA_IPS_XRES**](wia-ips-xres.md) and [**WIA_IPS_YRES**](wia-ips-yres.md) are changed.

**Note**   Flatbed and Film child items must support only the WIA_IPS_XEXTENT, WIA_IPS_XPOS, WIA_IPS_XRES, WIA_IPS_YEXTENT, WIA_IPS_YPOS, and WIA_IPS_YRES properties. All other properties, required or optional for their parent (the base Flatbed or Film items), are only optional for these items. The only exceptions are the WIA_IPA_ITEM_*Xxx* properties, which are required for all items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_PIXELS_PER_LINE**](wia-ipa-pixels-per-line.md)

[**WIA_IPS_PAGE_HEIGHT**](wia-ips-page-height.md)

[**WIA_IPS_PAGE_SIZE**](wia-ips-page-size.md)

[**WIA_IPS_PAGE_WIDTH**](wia-ips-page-width.md)

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)

[**WIA_IPS_XPOS**](wia-ips-xpos.md)

[**WIA_IPS_XRES**](wia-ips-xres.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)

[**WIA_IPS_YPOS**](wia-ips-ypos.md)

[**WIA_IPS_YRES**](wia-ips-yres.md)
