---
title: WIA_DIP_BAUDRATE
description: The WIA_DIP_BAUDRATE property contains the current baud rate setting for a device. The WIA service creates and maintains this property.
keywords: ["WIA_DIP_BAUDRATE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_BAUDRATE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DIP_BAUDRATE

The WIA_DIP_BAUDRATE property contains the current baud rate setting for a device. The WIA service creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The value of the WIA_DIP_BAUDRATE property should be "Empty" if the device is not connected by a serial cable.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
