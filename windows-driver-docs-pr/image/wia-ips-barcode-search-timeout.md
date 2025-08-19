---
title: WIA_IPS_BARCODE_SEARCH_TIMEOUT
description: The WIA_IPS_BARCODE_SEARCH_TIMEOUT property describes the maximum time to search for barcodes on a document page.
keywords: ["WIA_IPS_BARCODE_SEARCH_TIMEOUT Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_BARCODE_SEARCH_TIMEOUT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_BARCODE_SEARCH_TIMEOUT

The **WIA_IPS_BARCODE_SEARCH_TIMEOUT** property describes the maximum time to search for barcodes on a document page.

Property Type: VT_UI4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/Write

## Remarks

The time unit is not specified (it can be milliseconds or tenths of a second, for example) but the application can choose values in the minimum – maximum range reported by the WIA minidriver.

This property is required for all Barcode Reader items. The property can be implemented to support a range that contain one single value (meaning that the application cannot change this timeout).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
