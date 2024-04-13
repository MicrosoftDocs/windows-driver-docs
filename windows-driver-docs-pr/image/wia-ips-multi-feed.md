---
title: WIA_IPS_MULTI_FEED
description: The WIA_IPS_MULTI_FEED property is used to configure the action to be performed by the WIA minidriver when a multiple feed condition is detected at the device. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_MULTI_FEED Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_MULTI_FEED
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_MULTI_FEED

The **WIA_IPS_MULTI_FEED** property is used to configure the action to be performed by the WIA minidriver when a multiple feed condition is detected at the device. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_MULTI_FEED** property.

| Value | Definition |
|--|--|
| WIA_MULTI_FEED_DETECT_DISABLED | Multi-feed detection is disabled. This is the required default value if the property is supported. |
| WIA_MULTI_FEED_DETECT_STOP_ERROR | The device detects multi-feed, stops scanning, sets the MULTIPLE_FEED bit for [**WIA_DPS_DOCUMENT_HANDLING_STATUS**](wia-dps-document-handling-status.md), and returns WIA_ERROR_MULTI_FEED to [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata). |
| WIA_MULTI_FEED_DETECT_STOP_SUCCESS | The device detects multi-feed, stops scanning, sets the MULTIPLE_FEED bit for [**WIA_DPS_DOCUMENT_HANDLING_STATUS**](wia-dps-document-handling-status.md), and [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) returns and does not fail because of the multi-feed. |
| WIA_MULTI_FEED_DETECT_CONTINUE | The device detects multi-feed, beeps or produces an audible or visible signal at the hardware device (recommended but not required), and continues scanning. |

This property is optional, and is valid only for the Feeder data source item (represented in the [**WIA_IPA_ITEM_CATEGORY**](wia-ipa-item-category.md) property as WIA_CATEGORY_FEEDER).

When the WIA minidriver sets the MULTIPLE_FEED bit for the [**WIA_DPS_DOCUMENT_HANDLING_STATUS**](wia-dps-document-handling-status.md) property, the minidriver should clear this bit (flag) as soon as the minidriver detects that the feeder is unloaded, is reloaded, or a new scan job begins.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
