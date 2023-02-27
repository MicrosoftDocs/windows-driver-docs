---
title: WIA_DIP_DEV_NAME
description: The WIA_DIP_DEV_NAME property contains the name of a device. The WIA service creates and maintains this property.
keywords: ["WIA_DIP_DEV_NAME Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DIP_DEV_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DIP_DEV_NAME

The WIA_DIP_DEV_NAME property contains the name of a device. The WIA service creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The device name that is contained in the WIA_DIP_DEV_NAME property is obtained from the driver's INF file. An application reads this property to obtain the name of the device.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
