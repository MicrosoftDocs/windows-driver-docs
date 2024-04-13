---
title: WIA_DPS_PAD_COLOR
description: The WIA_DPS_PAD_COLOR property contains the current pad color that is used when the WIA minidriver pads unaligned data. The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_PAD_COLOR Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPS_PAD_COLOR
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_PAD_COLOR

The WIA_DPS_PAD_COLOR property contains the current pad color that is used when the WIA minidriver pads unaligned data. The WIA minidriver creates and maintains this property.

Property Type: VT_UI1 | VT_VECTOR

Valid Values: WIA_PROP_NONE

Access Rights: Read/write

## Remarks

The WIA_DPS_PAD_COLOR property should be reported as a vector of four BYTE values in the form of an RGBQUAD structure (which is described in the Microsoft Windows SDK documentation).

An application reads WIA_DPS_PAD_COLOR to get the padding color that is used.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
