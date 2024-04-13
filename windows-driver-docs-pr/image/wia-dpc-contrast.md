---
title: WIA_DPC_CONTRAST
description: The WIA_DPC_CONTRAST property indicates the perceived contrast of a captured image.
keywords: ["WIA_DPC_CONTRAST Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_CONTRAST
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_CONTRAST

The WIA_DPC_CONTRAST property indicates the perceived contrast of a captured image.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST or WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

The WIA_DPC_CONTRAST property can contain either a list of values or a range of values.

The minimum supported value for WIA_DPC_CONTRAST represents the least amount of contrast, and the maximum value represents the most contrast. Typically, a value in the middle of the range represents normal, or default, contrast.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
