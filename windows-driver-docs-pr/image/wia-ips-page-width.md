---
title: WIA_IPS_PAGE_WIDTH
description: The WIA_IPS_PAGE_WIDTH property contains the width of the current page selected, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PAGE_WIDTH Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PAGE_WIDTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_PAGE_WIDTH

The WIA_IPS_PAGE_WIDTH property contains the width of the current page selected, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads WIA_IPS_PAGE_WIDTH to determine the physical dimensions of the page that is being scanned. If the extent settings are different from known page sizes, this property reports the width of the page whose [**WIA_IPS_PAGE_SIZE**](wia-ips-page-size.md) property is set to WIA_PAGE_CUSTOM.

WIA_IPS_PAGE_WIDTH must be in sync with the value of WIA_IPS_XEXTENT, which reports the width, in pixels, of the page to be scanned.

The compatibility layer within the WIA service does not add support for the WIA_IPS_PAGE_WIDTH property to the ADF item that is translated from a Windows XP WIA device if the property is not supported on the child item of the device. Applications should not expect an ADF item to always support WIA_IPS_PAGE_WIDTH and should always check if it is supported at run time. (Typically, applications should check the support for any property to be negotiated.)

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_PAGE_WIDTH**](wia-dps-page-width.md)

[**WIA_IPS_PAGE_HEIGHT**](wia-ips-page-height.md)

[**WIA_IPS_PAGE_SIZE**](wia-ips-page-size.md)
