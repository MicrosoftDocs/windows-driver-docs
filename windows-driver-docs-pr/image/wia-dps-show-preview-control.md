---
title: WIA_DPS_SHOW_PREVIEW_CONTROL
description: The WIA_DPS_SHOW_PREVIEW_CONTROL property indicates whether an item needs a preview control displayed to the user. The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_SHOW_PREVIEW_CONTROL Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPS_SHOW_PREVIEW_CONTROL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# WIA_DPS_SHOW_PREVIEW_CONTROL

The WIA_DPS_SHOW_PREVIEW_CONTROL property indicates whether an item needs a preview control displayed to the user. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The following table describes the constants that are valid with WIA_DPS_SHOW_PREVIEW_CONTROL.

| Value | Definition |
|--|--|
| WIA_DONT_SHOW_PREVIEW_CONTROL | Do not show a preview control to the user, because this device cannot perform a preview. |
| WIA_SHOW_PREVIEW_CONTROL | Show a preview control to the user, because this device can perform a preview. |

The WIA_DPS_SHOW_PREVIEW_CONTROL property helps control devices that cannot preview. For example, some feeder-driven devices cannot reload the paper for a preview scan.

## Requirements

**Version:** Obsolete, use the WIA_IPS_SHOW_PREVIEW_CONTROL property instead.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_SHOW_PREVIEW_CONTROL**](wia-ips-show-preview-control.md)
