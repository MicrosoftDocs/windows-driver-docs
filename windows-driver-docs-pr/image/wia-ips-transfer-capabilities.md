---
title: WIA_IPS_TRANSFER_CAPABILITIES
description: The WIA_IPS_TRANSFER_CAPABILITIES property indicates if a device can transfer parent and child items together. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_TRANSFER_CAPABILITIES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_TRANSFER_CAPABILITIES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_TRANSFER_CAPABILITIES

The WIA_IPS_TRANSFER_CAPABILITIES property indicates if a device can transfer parent and child items together. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The following table describes the constant that is valid with the WIA_IPS_TRANSFER_CAPABILITIES property

| Flag | Definition |
|--|--|
| WIA_TRANSFER_CHILDREN_SINGLE_SCAN | The device can transfer the parent and child items together or the device must make a separate scan for each item and each child item. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
