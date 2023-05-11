---
title: WIA_IPS_BLANK_PAGES
description: The WIA_IPS_BLANK_PAGES property is used to configure blank page detection. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_BLANK_PAGES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_BLANK_PAGES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_BLANK_PAGES

The **WIA_IPS_BLANK_PAGES** property is used to configure blank page detection. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_BLANK_PAGES** property.

| Value | Definition |
|--|--|
| WIA_BLANK_PAGE_DETECTION_DISABLED | Blank page detection is disabled. This is the required default value if the property is supported. |
| WIA_BLANK_PAGE_DISCARD | The device detects blank pages and automatically skips scanning them (discards scanned data if any) and continues scanning. |
| WIA_BLANK_PAGE_JOB_SEPARATOR | The device detects blank pages and acts as configured through the [**WIA_IPS_JOB_SEPARATORS**](wia-ips-job-separators.md) property. This value is valid only when the Feeder item supports the **WIA_IPS_JOB_SEPARATORS** property. |

This property is optional, and is valid only for the Feeder data source item (represented in the [**WIA_IPA_ITEM_CATEGORY**](wia-ipa-item-category.md) property as WIA_CATEGORY_FEEDER).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
