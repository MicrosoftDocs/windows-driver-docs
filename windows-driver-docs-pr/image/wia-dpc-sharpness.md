---
title: WIA_DPC_SHARPNESS
description: The WIA_DPC_SHARPNESS property indicates the perceived sharpness of a captured image.
keywords: ["WIA_DPC_SHARPNESS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_SHARPNESS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPC_SHARPNESS

The WIA_DPC_SHARPNESS property indicates the perceived sharpness of a captured image.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST or WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

The WIA_DPC_SHARPNESS property can use either a list of values or a range of values. The minimum value represents the least amount of sharpness, and the maximum value represents the maximum sharpness. Typically, a value in the middle of the range represents normal, or default, sharpness.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
