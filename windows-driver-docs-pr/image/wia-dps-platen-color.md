---
title: WIA_DPS_PLATEN_COLOR
description: The WIA_DPS_PLATEN_COLOR property contains the current platen color.
keywords: ["WIA_DPS_PLATEN_COLOR Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PLATEN_COLOR
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_PLATEN_COLOR

The WIA_DPS_PLATEN_COLOR property contains the current platen color.

Property Type: VT_UI1 | VT_VECTOR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

A minidriver should report the WIA_DPS_PLATEN_COLOR as a vector of four BYTE values in the form of an RGBQUAD structure (which is described in the Microsoft Windows SDK documentation). The WIA minidriver creates and maintains this property.

An application reads WIA_DPS_PLATEN_COLOR to get the scanner's platen color. This color can help the application post-process the final image.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
