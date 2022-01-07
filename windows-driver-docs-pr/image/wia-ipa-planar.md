---
title: WIA_IPA_PLANAR
description: The WIA_IPA_PLANAR property contains image data packing options. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_PLANAR Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_PLANAR
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPA_PLANAR

The WIA_IPA_PLANAR property contains image data packing options. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST or WIA_PROP_NONE

Access Rights: Read/write or read-only

## Remarks

An application reads WIA_IPA_PLANAR to determine the image packing options or sets the current image packing options.

The following table describes the constants that are valid with WIA_IPA_PLANAR.

| Value | Definition |
|--|--|
| WIA_PACKED_PIXEL | Image data is in packed-pixel format. |
| WIA_PLANAR | Image data is in planar format. |

If a device can be set to only a single value, you can implement the WIA_IPA_PLANAR property as WIA_PROP_NONE and read-only.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems.

**Header:** wiadef.h (include Wiadef.h)
