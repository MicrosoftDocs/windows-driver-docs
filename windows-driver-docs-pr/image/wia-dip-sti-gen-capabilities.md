---
title: WIA_DIP_STI_GEN_CAPABILITIES
description: The WIA_DIP_STI_GEN_CAPABILITIES property contains the generic STI capabilities for a device, which are obtained from the driver's INF file. The WIA service creates and maintains this property.
keywords: ["WIA_DIP_STI_GEN_CAPABILITIES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DIP_STI_GEN_CAPABILITIES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DIP_STI_GEN_CAPABILITIES

The WIA_DIP_STI_GEN_CAPABILITIES property contains the generic STI capabilities for a device, which are obtained from the driver's INF file. The WIA service creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An application reads the WIA_DIP_STI_GEN_CAPABILITIES property to determine the generic STI capabilities of the device.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
