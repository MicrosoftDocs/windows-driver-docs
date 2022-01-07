---
title: WIA_DPC_FOCUS_METERING_MODE
description: The WIA_DPC_FOCUS_METERING_MODE property specifies the mode that a camera uses to automatically adjust the focus.
keywords: ["WIA_DPC_FOCUS_METERING_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_FOCUS_METERING_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_FOCUS_METERING_MODE

The WIA_DPC_FOCUS_METERING_MODE property specifies the mode that a camera uses to automatically adjust the focus.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The following table describes the constants that are valid with the WIA_DPC_FOCUS_METERING_MODE property.

| Value | Definition |
|--|--|
| FOCUSMETERING_CENTERSPOT | Adjust the focus based on a center spot. |
| FOCUSMETERING_MULTISPOT | Adjust the focus based on a multispot pattern. |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
