---
title: WIA_IPS_CONTRAST
description: The WIA_IPS_CONTRAST property contains the current hardware contrast setting for a device.
keywords: ["WIA_IPS_CONTRAST Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_CONTRAST
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPS_CONTRAST

The WIA_IPS_CONTRAST property contains the current hardware contrast setting for a device.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

An application sets the WIA_IPS_CONTRAST property to the hardware's contrast value. The WIA minidriver creates and maintains this property.

Values for WIA_IPS_CONTRAST should be mapped in a range from −1000 through 1000, where −1000 corresponds to the minimum contrast, 0 corresponds to normal contrast, and 1000 corresponds to the maximum contrast.

WIA_IPS_CONTRAST is required for all image acquisition items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
