---
title: WIA_DPS_PREVIEW
description: The WIA_DPS_PREVIEW property indicates the preview mode for a device. An application sets this property to place the device into a preview mode.
keywords: ["WIA_DPS_PREVIEW Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PREVIEW
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_PREVIEW

The WIA_DPS_PREVIEW property indicates the preview mode for a device. An application sets this property to place the device into a preview mode.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The following table describes the constants that are valid with the WIA_DPS_PREVIEW property.

| Value | Definition |
|--|--|
| WIA_FINAL_SCAN | The application will perform a final scan. |
| WIA_PREVIEW_SCAN | The application will perform a preview scan. |

## Requirements

**Version:** Obsolete, use the WIA_IPS_PREVIEW property instead.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_PREVIEW**](wia-ips-preview.md)
