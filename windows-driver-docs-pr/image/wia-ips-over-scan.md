---
title: WIA_IPS_OVER_SCAN
description: The WIA_IPS_OVER_SCAN property is used to enable and configure over scanning (scanning beyond physical document boundaries). The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_OVER_SCAN Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_OVER_SCAN
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/11/2023
---

# WIA_IPS_OVER_SCAN

The **WIA_IPS_OVER_SCAN** property is used to enable and configure over scanning (scanning beyond physical document boundaries). The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_OVER_SCAN** property.

| Value | Definition |
|--|--|
| WIA_OVER_SCAN_DISABLED | Over scanning is disabled. This is the required default value if the property is supported. |
| WIA_OVER_SCAN_TOP_BOTTOM | Over scan at the top and bottom sides of the document. |
| WIA_OVER_SCAN_LEFT_RIGHT | Over scan at the left and right sides of the document. |
| WIA_OVER_SCAN_ALL | Over scan at all sides of the document. |

This property is valid for all programmable image data source items, including Flatbed (WIA_CATEGORY_FLATBED) and Feeder (WIA_CATEGORY_FEEDER) and is optional. When the property is supported, WIA_OVER_SCAN_DISABLED is the required default value.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
