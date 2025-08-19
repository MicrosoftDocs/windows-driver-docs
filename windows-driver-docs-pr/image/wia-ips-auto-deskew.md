---
title: WIA_IPS_AUTO_DESKEW
description: The WIA_IPS_AUTO_DESKEW property indicates if a device should use automatic skew correction. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_AUTO_DESKEW Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_AUTO_DESKEW
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_AUTO_DESKEW

The WIA_IPS_AUTO_DESKEW property indicates if a device should use automatic skew correction. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The following table describes the constants that are valid with the **WIA_IPS_AUTO_DESKEW** property.

| Value | Definition |
|--|--|
| WIA_AUTO_DESKEW_ON | Use automatic skew correction. |
| WIA_AUTO_DESKEW_OFF | Do not use automatic skew correction. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
