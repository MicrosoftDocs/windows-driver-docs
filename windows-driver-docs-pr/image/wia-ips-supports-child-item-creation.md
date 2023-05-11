---
title: WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION
description: The WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION property indicates if a device supports the creation of child items.
keywords: ["WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION

The WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION property indicates if a device supports the creation of child items. The WIA minidriver creates and maintains this property

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

Items that support the [**WIA_IPS_SEGMENTATION**](wia-ips-segmentation.md) property and the WIA_USE_SEGMENTATION_FILTER value must also support the WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION property and have it set to **TRUE**.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_SEGMENTATION**](wia-ips-segmentation.md)
