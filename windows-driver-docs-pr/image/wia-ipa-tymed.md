---
title: WIA_IPA_TYMED
description: The WIA_IPA_TYMED property contains the method setting for image transfer . The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_TYMED Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_TYMED
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPA_TYMED

The WIA_IPA_TYMED property contains the method setting for image transfer . The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

An application reads the WIA_IPA_TYMED property to determine the minidriver's method of data transfer.

The following table describes the constants that are valid with WIA_IPA_TYMED.

| Value | Definition |
|--|--|
| TYMED_CALLBACK | This constant is obsolete. Transfer an image to memory, in bands. |
| TYMED_FILE | Transfer an image to a file. |
| TYMED_MULTIPAGE_CALLBACK | This constant is obsolete. Transfer multiple images to memory, in bands. |
| TYMED_MULTIPAGE_FILE | Transfer multiple images to a file. |

All WIA 2.0 minidrivers must set the initial value of this property to its default value, which is TYMED_FILE.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
