---
title: WIA_IPS_MAXIMUM_BARCODE_SEARCH_RETRIES
description: The WIA_IPS_MAXIMUM_BARCODE_SEARCH_RETRIES property describes the maximum number of retries the reader attempts if no barcode can be found when barcode detection is enabled.
keywords: ["WIA_IPS_MAXIMUM_BARCODE_SEARCH_RETRIES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_MAXIMUM_BARCODE_SEARCH_RETRIES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_MAXIMUM_BARCODE_SEARCH_RETRIES

The **WIA_IPS_MAXIMUM_BARCODE_SEARCH_RETRIES** property describes the maximum number of retries the reader attempts if no barcode can be found when barcode detection is enabled.

Property Type: VT_UI4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/Write

## Remarks

This property is required for all Barcode Reader items. The property can be implemented to support a range containing one single value, including 0 (no retries).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
