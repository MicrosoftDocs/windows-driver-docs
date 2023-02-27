---
title: WIA_DPS_HORIZONTAL_BED_REGISTRATION
description: The WIA_DPS_HORIZONTAL_BED_REGISTRATION property contains the registration, or horizontal alignment, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_HORIZONTAL_BED_REGISTRATION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPS_HORIZONTAL_BED_REGISTRATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_HORIZONTAL_BED_REGISTRATION

The WIA_DPS_HORIZONTAL_BED_REGISTRATION property contains the registration, or horizontal alignment, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The following table describes the constants that are valid with the WIA_DPS_HORIZONTAL_BED_REGISTRATION property.

| Value | Definition |
|--|--|
| CENTERED | The paper is centered. |
| LEFT_JUSTIFIED | The paper is left-aligned. |
| RIGHT_JUSTIFIED | The paper is right-aligned. |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_VERTICAL_BED_REGISTRATION**](wia-dps-vertical-bed-registration.md)
