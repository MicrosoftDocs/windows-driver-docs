---
title: WIA_IPS_PATCH_CODE_SEARCH_DIRECTION
description: The WIA_IPS_PATCH_CODE_SEARCH_DIRECTION property is used to configure the direction (relative to the scan direction) in which the device searches for patch codes on each scan document page.
keywords: ["WIA_IPS_PATCH_CODE_SEARCH_DIRECTION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PATCH_CODE_SEARCH_DIRECTION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PATCH_CODE_SEARCH_DIRECTION

The **WIA_IPS_PATCH_CODE_SEARCH_DIRECTION** property is used to configure the direction (relative to the scan direction) in which the device searches for patch codes on each scan document page.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

| Value | Definition |
|--|--|
| WIA_PATCH_CODE_HORIZONTAL_SEARCH | Device searches for patch codes horizontally. |
| WIA_PATCH_CODE_VERTICAL_SEARCH | Device searches for patch codes vertically. |
| WIA_PATCH_CODE_HORIZONTAL_VERTICAL_SEARCH | Device searches for patch codes first horizontally then vertically. |
| WIA_PATCH_CODE_VERTICAL_HORIZONTAL_SEARCH | Device searches for patch codes first vertically then horizontally. |
| WIA_PATCH_CODE_AUTO_SEARCH | Device searches for patch codes in its own direction that is automatically detected at run-time or predefined. |

This property is required for all Patch Code Reader items but it can be implemented to support only the WIA_PATCH_CODE_AUTO_SEARCH value.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
