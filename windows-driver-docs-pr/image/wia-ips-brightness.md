---
title: WIA_IPS_BRIGHTNESS
description: The WIA_IPS_BRIGHTNESS property contains the current hardware brightness setting for a device.
keywords: ["WIA_IPS_BRIGHTNESS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_BRIGHTNESS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA_IPS_BRIGHTNESS

The WIA_IPS_BRIGHTNESS property contains the current hardware brightness setting for a device.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

An application sets the WIA_IPS_BRIGHTNESS property to the hardware's brightness value. The WIA minidriver creates and maintains this property.

Values for WIA_IPS_BRIGHTNESS should be mapped in a range from −1000 through 1000, where 1000 corresponds to the maximum brightness, 0 corresponds to normal brightness, and −1000 corresponds to the minimum brightness.

WIA_IPS_BRIGHTNESS is required for all image acquisition items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
