---
title: WIA_DPC_FOCUS_MODE
description: The WIA_DPC_FOCUS_MODE property defines the current focus mode setting for a camera device.
keywords: ["WIA_DPC_FOCUS_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_FOCUS_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_FOCUS_MODE

The WIA_DPC_FOCUS_MODE property defines the current focus mode setting for a camera device.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

A device driver enumerates the supported values of the WIA_DPC_FOCUS_MODE property, and an application writes this property to set the focus mode for the camera device.

The following table describes the constants that are valid with the WIA_DPC_FOCUS_MODE property.

| Value | Definition |
|--|--|
| FOCUSMODE_AUTO | The camera device is configured to focus automatically. |
| FOCUSMODE_MACROAUTO | The camera device is configured to focus automatically by using short-range macro settings. |
| FOCUSMODE_MANUAL | The camera device is configured to allow a user to focus manually. |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
