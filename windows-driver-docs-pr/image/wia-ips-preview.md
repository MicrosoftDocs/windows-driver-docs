---
title: WIA_IPS_PREVIEW
description: The WIA_IPS_PREVIEW property indicates the preview mode for a device.
keywords: ["WIA_IPS_PREVIEW Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PREVIEW
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PREVIEW

The WIA_IPS_PREVIEW property indicates the preview mode for a device.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

An application sets WIA_IPS_PREVIEW to place a device into a preview mode.

The following table describes the constants that are valid with WIA_IPS_PREVIEW.

| Value | Definition |
|--|--|
| WIA_FINAL_SCAN | The application will perform a final scan. |
| WIA_PREVIEW_SCAN | The application will perform a preview scan. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_PREVIEW**](wia-dps-preview.md)
