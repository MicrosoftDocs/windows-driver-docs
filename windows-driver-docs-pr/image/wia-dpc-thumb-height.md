---
title: WIA_DPC_THUMB_HEIGHT
description: The WIA_DPC_THUMB_HEIGHT property defines the height, in pixels, of a thumbnail image to use for newly captured images.
keywords: ["WIA_DPC_THUMB_HEIGHT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_THUMB_HEIGHT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
ms.localizationpriority: medium
---

# WIA_DPC_THUMB_HEIGHT

The WIA_DPC_THUMB_HEIGHT property defines the height, in pixels, of a thumbnail image to use for newly captured images.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE or WIA_PROP_LIST

Access Rights: Read-only or read/write

## Remarks

An application reads the WIA_DPC_THUMB_HEIGHT value to get an estimated size for displaying thumbnail images in its user interface.

If the value or WIA_DPC_THUMB_HEIGHT is WIA_PROP_NONE, the access rights must be read-only. If the value is WIA_PROP_LIST, the access rights must be read/write.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPC_THUMB_WIDTH**](wia-dpc-thumb-width.md)
