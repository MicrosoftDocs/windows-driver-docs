---
title: WIA_DIP_DEV_DESC
description: The WIA_DIP_DEV_DESC property contains the device description string for a WIA minidriver. The WIA service creates and maintains this property.
keywords: ["WIA_DIP_DEV_DESC Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DIP_DEV_DESC
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DIP_DEV_DESC

The WIA_DIP_DEV_DESC property contains the device description string for a WIA minidriver. The WIA service creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The device description string that the WIA_DIP_DEV_DESC property contains is obtained from the driver's INF file. An application reads this property to get a description of the device.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
