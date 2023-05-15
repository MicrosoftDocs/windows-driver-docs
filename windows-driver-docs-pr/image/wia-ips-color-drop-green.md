---
title: WIA_IPS_COLOR_DROP_GREEN
description: The WIA_IPS_COLOR_DROP_GREEN property is used to configure the amount of color drop-out for the Green color channel.
keywords: ["WIA_IPS_COLOR_DROP_GREEN Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_COLOR_DROP_GREEN
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_COLOR_DROP_GREEN

The **WIA_IPS_COLOR_DROP_GREEN** property is used to configure the amount of color drop-out for the Green color channel (G in RGB), as a percentage in a range from 0% (no dropout) to 100% (full channel dropout). The WIA minidriver creates and maintains this property.

Property Type: VT_I4 | VT_VECTOR

Valid Values: WIA_PROP_NONE

Access Rights: Read/Write

## Remarks

When the [**WIA_IPS_COLOR_DROP**](wia-ips-color-drop.md) property is supported, this property is valid for all programmable image data source items, including Flatbed (WIA_CATEGORY_FLATBED) and Feeder (WIA_CATEGORY_FEEDER) and is required. Valid values for this property are between 0 and 100, inclusive.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
