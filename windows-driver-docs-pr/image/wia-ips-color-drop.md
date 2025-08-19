---
title: WIA_IPS_COLOR_DROP
description: The WIA_IPS_COLOR_DROP property is used to configure color filtering for the image data acquired from the hardware device. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_COLOR_DROP Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_COLOR_DROP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_COLOR_DROP

The **WIA_IPS_COLOR_DROP** property is used to configure color filtering for the image data acquired from the hardware device. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_COLOR_DROP** property.

| Value | Definition |
|--|--|
| WIA_COLOR_DROP_DISABLED | Color drop is disabled. This is the required default value if the property is supported. |
| WIA_COLOR_DROP_RED | The Red channel is dropped in the amount described by [**WIA_IPS_COLOR_DROP_RED**](wia-ips-color-drop-red.md). |
| WIA_COLOR_DROP_GREEN | The Green channel is dropped in the amount described by [**WIA_IPS_COLOR_DROP_GREEN**](wia-ips-color-drop-green.md). |
| WIA_COLOR_DROP_BLUE | The Blue channel is dropped in the amount described by [**WIA_IPS_COLOR_DROP_BLUE**](wia-ips-color-drop-blue.md). |
| WIA_COLOR_DROP_RGB | The Red, Green, and/or Blue channels are dropped in the amounts specified by [**WIA_IPS_COLOR_DROP_RED**](wia-ips-color-drop-red.md), [**WIA_IPS_COLOR_DROP_GREEN**](wia-ips-color-drop-green.md), and [**WIA_IPS_COLOR_DROP_BLUE**](wia-ips-color-drop-blue.md). |

This property is valid for all programmable image data source items, including Flatbed (WIA_CATEGORY_FLATBED) and Feeder (WIA_CATEGORY_FEEDER) and is optional. When the property is supported, WIA_COLOR_DROP_DISABLED is the required default value.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
