---
title: WIA_DPS_PAGE_HEIGHT
description: The WIA_DPS_PAGE_HEIGHT property contains the height, in thousandths of an inch (.001), of the currently selected page. The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_PAGE_HEIGHT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PAGE_HEIGHT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_PAGE_HEIGHT

The WIA_DPS_PAGE_HEIGHT property contains the height, in thousandths of an inch (.001), of the currently selected page. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads WIA_DPS_PAGE_HEIGHT to determine the physical dimensions of the page that is being scanned. If the extent settings are different from the known page sizes, this property reports the height of the page whose [**WIA_DPS_PAGE_SIZE**](wia-dps-page-size.md) property is set to WIA_PAGE_CUSTOM (which is a value of the WIA_DPS_PAGE_SIZE property).

WIA_DPS_PAGE_HEIGHT must provide a measurement in thousandths of an inch that is equivalent to the pixel value reported by the [**WIA_IPS_YEXTENT**](wia-ips-yextent.md) property, which reports the height, in pixels, of the page to be scanned.

## Requirements

**Version:** Obsolete, use the WIA_IPS_PAGE_HEIGHT property instead.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_PAGE_SIZE**](wia-dps-page-size.md)

[**WIA_DPS_PAGE_WIDTH**](wia-dps-page-width.md)

[**WIA_IPS_PAGE_HEIGHT**](wia-ips-page-height.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)
