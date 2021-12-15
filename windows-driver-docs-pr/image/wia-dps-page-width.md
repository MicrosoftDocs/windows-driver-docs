---
title: WIA_DPS_PAGE_WIDTH
description: The WIA_DPS_PAGE_WIDTH property contains the width of the currently selected page, in thousandths of an inch (.001).
keywords: ["WIA_DPS_PAGE_WIDTH Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PAGE_WIDTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_PAGE_WIDTH

The WIA_DPS_PAGE_WIDTH property contains the width of the currently selected page, in thousandths of an inch (.001).

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads the WIA_DPS_PAGE_WIDTH property to determine the physical dimensions of the page that is being scanned. If the extent settings are different from known page sizes, this property reports the width of the page whose [**WIA_DPS_PAGE_SIZE**](wia-dps-page-size.md) property is set to WIA_PAGE_CUSTOM. The WIA minidriver creates and maintains WIA_DPS_PAGE_WIDTH.

WIA_DPS_PAGE_WIDTH must provide a measurement equivalent to the value of the [**WIA_IPS_XEXTENT**](wia-ips-xextent.md) property, which reports the width, in pixels, of the page to scan.

## Requirements

**Version:** Obsolete, use the WIA_IPS_PAGE_WIDTH property instead.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_PAGE_HEIGHT**](wia-dps-page-height.md)

[**WIA_DPS_PAGE_SIZE**](wia-dps-page-size.md)

[**WIA_IPS_PAGE_WIDTH**](wia-ips-page-width.md)

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)
