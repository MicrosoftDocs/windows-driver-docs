---
title: WIA_IPA_SUPPRESS_PROPERTY_PAGE
description: The WIA_IPA_SUPPRESS_PROPERTY_PAGE property specifies whether to suppress the general property pages for items on a device.
keywords: ["WIA_IPA_SUPPRESS_PROPERTY_PAGE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPA_SUPPRESS_PROPERTY_PAGE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPA_SUPPRESS_PROPERTY_PAGE

The WIA_IPA_SUPPRESS_PROPERTY_PAGE property specifies whether to suppress the general property pages for items on a device.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The following table describes the constants that are valid with the WIA_IPA_SUPPRESS_PROPERTY_PAGE property.

| Value | Definition |
|--|--|
| WIA_PROPPAGE_CAMERA_ITEM_GENERAL | Suppress the general item property page for a camera. |
| WIA_PROPPAGE_SCANNER_ITEM_GENERAL | Suppress the general item property page for a scanner. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
