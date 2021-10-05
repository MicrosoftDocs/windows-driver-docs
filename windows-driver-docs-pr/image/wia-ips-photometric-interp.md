---
title: WIA_IPS_PHOTOMETRIC_INTERP
description: The WIA_IPS_PHOTOMETRIC_INTERP property contains the current setting for white and black pixels. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PHOTOMETRIC_INTERP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PHOTOMETRIC_INTERP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA_IPS_PHOTOMETRIC_INTERP

The WIA_IPS_PHOTOMETRIC_INTERP property contains the current setting for white and black pixels. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

An application reads the WIA_IPS_PHOTOMETRIC_INTERP property to determine the value assigned to white or black pixels (depending on what the application is doing).

The following table describes the constants that are valid with WIA_IPS_PHOTOMETRIC_INTERP.

| Value | Definition |
|--|--|
| WIA_PHOTO_WHITE_0 | White is 0, and black is 1. |
| WIA_PHOTO_WHITE_1 | White is 1, and black is 0. |

If a device can be set to only a single value, create a WIA_PROP_LIST type, and place the valid value in it.

The WIA_IPS_PHOTOMETRIC_INTERP property is required for all image acquisition items and stored images.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
