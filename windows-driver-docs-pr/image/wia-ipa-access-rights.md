---
title: WIA_IPA_ACCESS_RIGHTS
description: The WIA_IPA_ACCESS_RIGHTS property contains the access rights for a WIA item.
keywords: ["WIA_IPA_ACCESS_RIGHTS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPA_ACCESS_RIGHTS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/04/2021
---

# WIA_IPA_ACCESS_RIGHTS

The WIA_IPA_ACCESS_RIGHTS property contains the access rights for a WIA item.

Property Type: VT_I4

Valid Values: WIA_PROP_FLAG

Access Rights: Read/write or read-only (depending on the item's ability to have its access rights changed)

## Remarks

*Access rights* control the ability of an application to delete items in the WIA item tree. The WIA minidriver creates and maintains the WIA_IPA_ACCESS_RIGHTS property.

The following table describes the constants that are valid with WIA_IPA_ACCESS_RIGHTS.

| Value | Definition |
|--|--|
| WIA_ITEM_CAN_BE_DELETED | This WIA item can be deleted. |
| WIA_ITEM_READ | Access to the item is read-only. |
| WIA_ITEM_WRITE | Access to the item is read/write. |
| WIA_ITEM_RD | OR of the following: WIA_ITEM_READ, WIA_ITEM_CAN_BE_DELETED |
| WIA_ITEM_RWD | OR of the following: WIA_ITEM_READ, WIA_ITEM_WRITE, WIA_ITEM_CAN_BE_DELETED |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
