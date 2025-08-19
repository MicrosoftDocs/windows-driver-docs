---
title: WIA_IPS_YSCALING
description: The WIA_IPS_YSCALING property indicates if scaling along the y-axis should be applied to a scan. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_YSCALING Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_YSCALING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_YSCALING

The WIA_IPS_YSCALING property indicates if scaling along the y-axis should be applied to a scan. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE or WIA_PROP_LIST

Access Rights: Read/write or read-only

## Remarks

Valid values for the WIA_IPS_YSCALING property range from 1 through 65535.

WIA_IPS_YSCALING indicates only scaling along the y-axis. If you want to scale an image uniformly, you must set a similar value in WIA_IPS_YSCALING and in the [**WIA_IPS_XSCALING**](wia-ips-xscaling.md) property.

Consider the following examples:

- 100, no scaling (1x, 100%). The image is not changed.

- 050, 1/2 scaling (1/2x, 50%). The image size is reduced along the y-axis by 50% (1/2 the original size).

- 200, 2x scaling (200%). The image size is enlarged along the y-axis by 200% (double).

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_XSCALING**](wia-ips-xscaling.md)
