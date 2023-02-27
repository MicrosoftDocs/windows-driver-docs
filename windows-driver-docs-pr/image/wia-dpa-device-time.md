---
title: WIA_DPA_DEVICE_TIME
description: The WIA_DPA_DEVICE_TIME property contains the current clock time that is stored on a device. The minidriver creates and maintains this property.
keywords: ["WIA_DPA_DEVICE_TIME Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPA_DEVICE_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPA_DEVICE_TIME

The WIA_DPA_DEVICE_TIME property contains the current clock time that is stored on a device. The minidriver creates and maintains this property.

Property Type: VT_UI2 | VT_VECTOR

Valid Values: WIA_PROP_NONE

Access Rights: Read/write or read-only

## Remarks

When the WIA_DPA_DEVICE_TIME property is read, the minidriver should check the device's current clock time and should always return the current time. This property is supported only by devices that have an internal clock. If the device clock can be set, this property is read/write; otherwise, it is read-only. WIA devices report time in a [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) structure.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
