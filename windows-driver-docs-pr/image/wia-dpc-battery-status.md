---
title: WIA_DPC_BATTERY_STATUS
description: The WIA_DPC_BATTERY_STATUS property defines the percentage of battery power that is left to operate a camera device.
keywords: ["WIA_DPC_BATTERY_STATUS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_BATTERY_STATUS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_BATTERY_STATUS

The WIA_DPC_BATTERY_STATUS property defines the percentage of battery power that is left to operate a camera device.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The value of the WIA_DPC_BATTERY_STATUS property should be an integer from 0 through 100. An application reads this property to determine the remaining battery life of the camera device.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
