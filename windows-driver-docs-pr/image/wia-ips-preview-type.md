---
title: WIA_IPS_PREVIEW_TYPE
description: The WIA_IPS_PREVIEW_TYPE property indicates if WIA_IPA_DATATYPE and WIA_IPA_DEPTH are changed, without having to request a new preview scan. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PREVIEW_TYPE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PREVIEW_TYPE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PREVIEW_TYPE

The WIA_IPS_PREVIEW_TYPE property indicates if [**WIA_IPA_DATATYPE**](wia-ipa-datatype.md) and [**WIA_IPA_DEPTH**](wia-ipa-depth.md) are changed, without having to request a new preview scan. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The following table describes the constants that are valid with the WIA_IPS_PREVIEW_TYPE property.

| Value | Definition |
|--|--|
| WIA_ADVANCED_PREVIEW | Live preview updates are supported. |
| WIA_BASIC_PREVIEW | Preview images can be updated only with a new preview scan. |

**Note**   WIA_IPS_PREVIEW_TYPE should describe only the [**WIA_IPA_DATATYPE**](wia-ipa-datatype.md) and [**WIA_IPA_DEPTH**](wia-ipa-depth.md) properties.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_DATATYPE**](wia-ipa-datatype.md)

[**WIA_IPA_DEPTH**](wia-ipa-depth.md)
