---
title: WIA_IPS_DESKEW_X
description: The WIA_IPS_DESKEW_X property, together with the WIA_IPS_DESKEW_Y property, describes the upper two corners of a skewed image. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_DESKEW_X Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_DESKEW_X
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_DESKEW_X

The WIA_IPS_DESKEW_X property, together with the [**WIA_IPS_DESKEW_Y**](wia-ips-deskew-y.md) property, describes the upper two corners of a skewed image. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

The WIA_IPS_DESKEW_X and WIA_IPS_DESKEW_Y properties describe where the two upper corners of a skewed image are located within the bounding rectangle that [**WIA_IPS_XPOS**](wia-ips-xpos.md), [**WIA_IPS_YPOS**](wia-ips-ypos.md), [**WIA_IPS_XEXTENT**](wia-ips-xextent.md), and [**WIA_IPS_YEXTENT**](wia-ips-yextent.md) properties define.

The valid values for WIA_IPS_DESKEW_X must be between 0 and (WIA_IPS_XEXTENT - 1). A value of 0 means that no skew correction should be performed.

WIA_IPS_DESKEW_X contains the number of pixels in the x-direction from WIA_IPS_XPOS to the x-coordinate of the uppermost corner of the image to be corrected.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_DESKEW_Y**](wia-ips-deskew-y.md)

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)

[**WIA_IPS_XPOS**](wia-ips-xpos.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)

[**WIA_IPS_YPOS**](wia-ips-ypos.md)
