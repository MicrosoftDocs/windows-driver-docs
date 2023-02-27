---
title: WIA_IPA_ITEM_TIME
description: The WIA_IPA_ITEM_TIME property contains the time that an image was originally captured.
keywords: ["WIA_IPA_ITEM_TIME Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPA_ITEM_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPA_ITEM_TIME

The WIA_IPA_ITEM_TIME property contains the time that an image was originally captured.

Property Type: VT_UI2 | VT_VECTOR

Valid Values: WIA_PROP_NONE

Access Rights: Read/write or read-only

## Remarks

The WIA minidriver creates and maintains the WIA_IPA_ITEM_TIME property. This property should be reported as a vector of eight WORD values in the form of a SYSTEMTIME structure (which is described in the Microsoft Windows SDK documentation).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
