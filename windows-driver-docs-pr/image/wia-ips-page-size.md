---
title: WIA_IPS_PAGE_SIZE
description: The WIA_IPS_PAGE_SIZE property contains the size of the page that is currently selected to be scanned.
keywords: ["WIA_IPS_PAGE_SIZE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PAGE_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_PAGE_SIZE

The WIA_IPS_PAGE_SIZE property contains the size of the page that is currently selected to be scanned.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

To select the dimensions of the page to scan, an application sets the WIA_IPS_PAGE_SIZE property. The WIA minidriver creates and maintains this property.

The following table describes the constants that are valid with WIA_IPS_PAGE_SIZE.

| Value | Definition |
|--|--|
| WIA_PAGE_A4 | 8267 × 11692 (PORTRAIT orientation). |
| WIA_PAGE_AUTO | Used to configure automatic page size detection. |
| WIA_PAGE_CUSTOM | Defined by the values of the [**WIA_IPS_PAGE_HEIGHT**](wia-ips-page-height.md) and [**WIA_IPS_PAGE_WIDTH**](wia-ips-page-width.md) properties. |
| WIA_PAGE_CUSTOM_BASE | Defined by the values of the WIA_IPS_PAGE_HEIGHT and WIA_IPS_PAGE_WIDTH properties. This value is used to define custom page sizes, instead of the single page that the WIA_PAGE_CUSTOM value enables. |
| WIA_PAGE_LETTER | 8500 × 11000 (PORTRAIT orientation). |

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**IWiaMiniDrv::drvValidateItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties)

[**WIA_DPS_PAGE_SIZE**](wia-dps-page-size.md)

[**WIA_IPS_ORIENTATION**](wia-ips-orientation.md)

[**WIA_IPS_PAGE_HEIGHT**](wia-ips-page-height.md)

[**WIA_IPS_PAGE_WIDTH**](wia-ips-page-width.md)

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)

[**WIA_IPS_XPOS**](wia-ips-xpos.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)

[**WIA_IPS_YPOS**](wia-ips-ypos.md)
