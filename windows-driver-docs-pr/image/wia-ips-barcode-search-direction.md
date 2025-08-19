---
title: WIA_IPS_BARCODE_SEARCH_DIRECTION
description: The WIA_IPS_BARCODE_SEARCH_DIRECTION property is used to configure the direction (relative to the scan direction) in which the device searches for barcodes on each scanned document page.
keywords: ["WIA_IPS_BARCODE_SEARCH_DIRECTION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_BARCODE_SEARCH_DIRECTION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_BARCODE_SEARCH_DIRECTION

The **WIA_IPS_BARCODE_SEARCH_DIRECTION** property is used to configure the direction (relative to the scan direction) in which the device searches for barcodes on each scanned document page.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_BARCODE_SEARCH_DIRECTION** property.

| Value | Definition |
|--|--|
| WIA_BARCODE_HORIZONTAL_SEARCH | Device searches for barcodes horizontally. |
| WIA_BARCODE_VERTICAL_SEARCH | Device searches for barcodes vertically. |
| WIA_BARCODE_HORIZONTAL_VERTICAL_SEARCH | Device searches for barcodes first horizontally then vertically. |
| WIA_BARCODE_VERTICAL_HORIZONTAL_SEARCH | Device searches for barcodes first vertically then horizontally. |
| WIA_BARCODE_AUTO_SEARCH | Device searches for barcodes in its own direction that is automatically detected at run time or predefined. |

This property is required for all Barcode Reader items, but it can be implemented to support only the WIA_BARCODE_AUTO_SEARCH value.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
