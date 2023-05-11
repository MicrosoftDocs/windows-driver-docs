---
title: WIA_IPS_DESKEW_Y
description: The WIA_IPS_DESKEW_Y property, together with the WIA_IPS_DESKEW_X property, describes the upper two corners of a skewed image. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_DESKEW_Y Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_DESKEW_Y
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_DESKEW_Y

The WIA_IPS_DESKEW_Y property, together with the [**WIA_IPS_DESKEW_X**](wia-ips-deskew-x.md) property, describes the upper two corners of a skewed image. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

The WIA_IPS_DESKEW_X and WIA_IPS_DESKEW_Y properties describe where the two upper corners of a skewed image are located within the bounding rectangle that the [**WIA_IPS_XPOS**](wia-ips-xpos.md), [**WIA_IPS_YPOS**](wia-ips-ypos.md), [**WIA_IPS_XEXTENT**](wia-ips-xextent.md), and [**WIA_IPS_YEXTENT**](wia-ips-yextent.md) properties define.

The valid values for WIA_IPS_DESKEW_Y must be between 0 and (WIA_IPS_YEXTENT - 1). A value of 0 means that no deskew should be performed.

WIA_IPS_DESKEW_Y contains the number of pixels in the y-direction from WIA_IPS_YPOS to the y-coordinate of the leftmost corner of the image to be deskewed.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_DESKEW_X**](wia-ips-deskew-x.md)

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)

[**WIA_IPS_XPOS**](wia-ips-xpos.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)

[**WIA_IPS_YPOS**](wia-ips-ypos.md)
