---
title: WIA_DPC_POWER_MODE
description: The WIA_DPC_POWER_MODE property defines the current power source for the camera device.
keywords: ["WIA_DPC_POWER_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_POWER_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPC_POWER_MODE

The WIA_DPC_POWER_MODE property defines the current power source for the camera device.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads the WIA_DPC_POWER_MODE property to determine what power source the camera is using.

The following table describes the constants that are valid with WIA_DPC_POWER_MODE.

| Value | Definition |
|--|--|
| POWERMODE_BATTERY | The camera device is operating on battery power. |
| POWERMODE_LINE | The camera device is operating on a power adapter. |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
