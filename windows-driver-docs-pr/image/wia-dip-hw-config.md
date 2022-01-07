---
title: WIA_DIP_HW_CONFIG
description: The WIA_DIP_HW_CONFIG property indicates the type of connection that a device is using. The WIA service creates and maintains this property, and only the WIA service can change it.
keywords: ["WIA_DIP_HW_CONFIG Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_HW_CONFIG
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# WIA_DIP_HW_CONFIG

The WIA_DIP_HW_CONFIG property indicates the type of connection that a device is using. The WIA service creates and maintains this property, and only the WIA service can change it.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads the WIA_DIP_HW_CONFIG property to determine the device's connection type.

The following table describes the possible values for WIA_DIP_HW_CONFIG.

| Value | Definition |
|--|--|
| 1 | Generic WDM device |
| 2 | SCSI device |
| 4 | USB device |
| 8 | Serial device |
| 16 | Parallel device |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
