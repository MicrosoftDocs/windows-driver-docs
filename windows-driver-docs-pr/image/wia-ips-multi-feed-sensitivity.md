---
title: WIA_IPS_MULTI_FEED_SENSITIVITY
description: The WIA_IPS_MULTI_FEED_SENSITIVITY property is used to change the multi-feed detection trigger to a lower or higher value between the lowest and highest sensitivity supported by the device. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_MULTI_FEED_SENSITIVITY Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_MULTI_FEED_SENSITIVITY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_MULTI_FEED_SENSITIVITY

The **WIA_IPS_MULTI_FEED_SENSITIVITY** property is used to change the multi-feed detection trigger to a lower or higher value between the lowest and highest sensitivity supported by the device. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/Write

## Remarks

This property is optional, and is valid only for the Feeder data source item (represented in the [**WIA_IPA_ITEM_CATEGORY**](wia-ipa-item-category.md) property as WIA_CATEGORY_FEEDER) when [**WIA_IPS_MULTI_FEED**](wia-ips-multi-feed.md) is supported with at least one other value besides WIA_MULTI_FEED_DETECT_DISABLED.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
