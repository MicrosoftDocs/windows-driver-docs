---
title: WIA_IPA_ITEM_SIZE
description: The WIA_IPA_ITEM_SIZE property contains the current size, in bytes, of the data that is associated with a WIA item. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_ITEM_SIZE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPA_ITEM_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPA_ITEM_SIZE

The WIA_IPA_ITEM_SIZE property contains the current size, in bytes, of the data that is associated with a WIA item. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The value that the WIA_IPA_ITEM_SIZE property contains is the total size of the data that is being transferred. If this value is zero, the WIA minidriver has no information about the exact size of the data. (This situation is common for compressed data.)

An application reads WIA_IPA_ITEM_SIZE to determine the size of the data before it is transferred. The WIA service reads this property to assist in allocating memory for data transfers. For more information about data transfers, see [Transferring Data to a WIA Application](./transferring-data-to-a-wia-application.md).

If WIA_IPA_ITEM_SIZE is set to zero and TYMED is configured for a file transfer, the WIA service does not allocate any memory for the WIA minidriver.

> [!NOTE]
> In Windows Vista and later versions of the operating system only set the WIA_IPA_ITEM_SIZE property to 0 for the ADF item when automatic document size detection is enabled.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
