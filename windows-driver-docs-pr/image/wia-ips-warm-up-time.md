---
title: WIA_IPS_WARM_UP_TIME
description: The WIA_IPS_WARM_UP_TIME property contains the maximum warm-up time, in milliseconds, that a device needs before starting the scanning operation. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_WARM_UP_TIME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_WARM_UP_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA_IPS_WARM_UP_TIME

The WIA_IPS_WARM_UP_TIME property contains the maximum warm-up time, in milliseconds, that a device needs before starting the scanning operation. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application can read the WIA_IPS_WARM_UP_TIME property to determine the maximum warm-up time for a device. The application can then present a "waiting for the device to warm up" dialog box to let users know that a wait or pause might occur before anything happens.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
