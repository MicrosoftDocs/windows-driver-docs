---
title: WIA_IPS_XRES
description: The WIA_IPS_XRES property contains the current horizontal resolution, in pixels per inch, for a device.
keywords: ["WIA_IPS_XRES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_XRES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPS_XRES

The WIA_IPS_XRES property contains the current horizontal resolution, in pixels per inch, for a device.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE or WIA_PROP_LIST

Access Rights: Read/write or read-only

## Remarks

An application sets the WIA_IPS_XRES property to set the horizontal resolution. The WIA minidriver creates and maintains this property.

If a device can be set to only a single value, create a WIA_PROP_LIST type and place the valid value in it. This situation also applies when one resolution setting depends on another resolution. (For example, the vertical resolution can depend on the horizontal resolution.)

WIA_IPS_XRES is required for all image acquisition-enabled items and stored image items; it is not available for storage items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)

[**WIA_IPS_XPOS**](wia-ips-xpos.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)

[**WIA_IPS_YPOS**](wia-ips-ypos.md)

[**WIA_IPS_YRES**](wia-ips-yres.md)
