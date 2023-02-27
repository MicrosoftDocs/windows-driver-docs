---
title: WIA_DPA_CONNECT_STATUS
description: The WIA_DPA_CONNECT_STATUS property contains the current connection status for a device. The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPA_CONNECT_STATUS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPA_CONNECT_STATUS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPA_CONNECT_STATUS

The WIA_DPA_CONNECT_STATUS property contains the current connection status for a device. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The following table lists the possible values for the WIA_DPA_CONNECT_STATUS property.

| Value | Definition |
|--|--|
| WIA_DEVICE_NOT_CONNECTED | The device is not connected. |
| WIA_DEVICE_CONNECTED | The device is connected and operational. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
