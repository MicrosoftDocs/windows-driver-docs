---
title: WIA_IPS_LONG_DOCUMENT
description: The WIA_IPS_LONG_DOCUMENT property is used by the WIA minidriver to report whether long document scanning is supported and by the WIA client application to enable this feature. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_LONG_DOCUMENT Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_LONG_DOCUMENT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_LONG_DOCUMENT

The **WIA_IPS_LONG_DOCUMENT** property is used by the WIA minidriver to report whether long document scanning is supported and by the WIA client application to enable this feature. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_LONG_DOCUMENT** property.

| Value | Definition |
|--|--|
| WIA_LONG_DOCUMENT_DISABLED | Long document scanning is disabled. This is the required default value if the property is supported. |
| WIA_LONG_DOCUMENT_ENABLED | The device scans long documents up to the device's maximum possible length.[**WIA_IPS_PAGE_SIZE**](wia-ips-page-size.md) property must be set to WIA_PAGE_AUTO for this value to be accepted. |
| WIA_LONG_DOCUMENT_SPLIT | Long documents are automatically split (and transferred as separate images) at current [**WIA_IPS_PAGE_SIZE**](wia-ips-page-size.md) length. The last scanned page can be shorter. |

This property is optional, and is valid only for the Feeder data source item (represented in the [**WIA_IPA_ITEM_CATEGORY**](wia-ipa-item-category.md) property as WIA_CATEGORY_FEEDER).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
