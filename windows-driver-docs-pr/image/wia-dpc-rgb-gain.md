---
title: WIA_DPC_RGB_GAIN
description: The WIA_DPC_RGB_GAIN property contains a null-terminated Unicode string that represents the red, green, and blue gain, respectively, that is applied to image data.
keywords: ["WIA_DPC_RGB_GAIN Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_RGB_GAIN
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
ms.localizationpriority: medium
---

# WIA_DPC_RGB_GAIN

The WIA_DPC_RGB_GAIN property contains a null-terminated Unicode string that represents the red, green, and blue gain, respectively, that is applied to image data. For example, "4:25:50" represents a red gain of 4, a green gain of 25, and a blue gain of 50.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE or WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The WIA_DPC_RGB_GAIN property is parsed as follows: *R*:*G*:*B*. *R* represents the red gain, *G* represents the green gain, and *B* represents the blue gain. For example, for an RGB ratio of red=4, green=2, blue=3, the RGB string could be "4:2:3" or "2000:1000:1500". These values are relative to each other. You can use larger numbers for added granularity, but the color will be same if the ratio of red, green, and blue remains the same. The string parser for this property value should support UINT16 integers for *R*, *G*, and *B*.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
