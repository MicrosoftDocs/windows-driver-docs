---
title: WIA_IPS_SUPPORTED_PATCH_CODE_TYPES
description: The WIA minidriver uses the WIA_IPS_SUPPORTED_PATCH_CODE_TYPES property to list all patch code types that are supported (understood) by the Patch Code Reader.
keywords: ["WIA_IPS_SUPPORTED_PATCH_CODE_TYPES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_SUPPORTED_PATCH_CODE_TYPES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_SUPPORTED_PATCH_CODE_TYPES

The WIA minidriver uses the **WIA_IPS_SUPPORTED_PATCH_CODE_TYPES** property to list all patch code types that are supported (understood) by the Patch Code Reader. The supported barcode types are reported in a VT_VECTOR array as a single value that contains multiple entries.

Property Type: VT_I4 | VT_VECTOR

Valid Values: WIA_PROP_NONE (single 'array'/vector value)

Access Rights: Read-only

## Remarks

The following table describes the valid values for the **WIA_IPS_SUPPORTED_PATCH_CODE_TYPES** property.

| Value | Definition |
|--|--|
| WIA_PATCH_CODE_1 | Patch code 1 |
| WIA_PATCH_CODE_2 | Patch code 2 |
| WIA_PATCH_CODE_3 | Patch code 3 |
| WIA_PATCH_CODE_4 | Patch code 4 |
| WIA_PATCH_CODE_6 | Patch code 6 |
| WIA_PATCH_CODE_T | Patch code T |
| WIA_PATCH_CODE_CUSTOM_BASE + N | WIA_PATCH_CODE_CUSTOM_BASE is the offset to all custom patch code values the WIA minidriver may add. N is a positive integer. |

The WIA minidriver can extend this list with additional custom values defined as WIA_PATCH_CODE_CUSTOM_BASE + N, where N is a positive integer.

This property is required for all Patch Code Reader items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
