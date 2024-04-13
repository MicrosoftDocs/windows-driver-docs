---
title: WIA_DPS_MAX_SCAN_TIME
description: The WIA_DPS_MAX_SCAN_TIME property contains the maximum time to scan a single page with the current property settings, in milliseconds.
keywords: ["WIA_DPS_MAX_SCAN_TIME Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPS_MAX_SCAN_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_MAX_SCAN_TIME

The WIA_DPS_MAX_SCAN_TIME property contains the maximum time to scan a single page with the current property settings, in milliseconds.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads the WIA_DPS_MAX_SCAN_TIME property to estimate how much the time it will take to scan a page. This estimate is helpful when you are determining the conditions of a device that has stopped responding. The WIA minidriver creates and maintains this property.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
