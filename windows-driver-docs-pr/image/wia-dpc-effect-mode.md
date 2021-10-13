---
title: WIA_DPC_EFFECT_MODE
description: The WIA_DPC_EFFECT_MODE property specifies the special image acquisition mode of a camera.
keywords: ["WIA_DPC_EFFECT_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EFFECT_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
ms.localizationpriority: medium
---

# WIA_DPC_EFFECT_MODE

The WIA_DPC_EFFECT_MODE property specifies the special image acquisition mode of a camera.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The following table describes the constants that are valid with the WIA_DPC_EFFECT_MODE property.

| Value | Definition |
|--|--|
| EFFECTMODE_BW | Capture a grayscale image |
| EFFECTMODE_SEPIA | Capture a sepia image |
| EFFECTMODE_STANDARD | Capture an image in the standard mode for the camera |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
