---
title: WIA_DPA_FIRMWARE_VERSION
description: The WIA_DPA_FIRMWARE_VERSION property contains a device firmware version. The minidriver creates and maintains this property.
keywords: ["WIA_DPA_FIRMWARE_VERSION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPA_FIRMWARE_VERSION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
ms.localizationpriority: medium
---

# WIA_DPA_FIRMWARE_VERSION

The WIA_DPA_FIRMWARE_VERSION property contains a device firmware version. The minidriver creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The value of the WIA_DPA_FIRMWARE_VERSION property must be a string value, such as "1.0.4" or "1.0abc".

## Requirements

**Header:** wiadef.h (include Wiadef.h)
