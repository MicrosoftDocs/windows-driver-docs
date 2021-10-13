---
title: WIA_DPC_PICT_HEIGHT
description: The WIA_DPC_PICT_HEIGHT property contains the height, in pixels, to use for newly captured images.
keywords: ["WIA_DPC_PICT_HEIGHT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_PICT_HEIGHT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
ms.localizationpriority: medium
---

# WIA_DPC_PICT_HEIGHT

The WIA_DPC_PICT_HEIGHT property contains the height, in pixels, to use for newly captured images.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST or WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

The list of valid values for the WIA_DPC_PICT_HEIGHT property has a one-to-one correspondence with the list of valid values for the [**WIA_DPC_PICT_WIDTH**](wia-dpc-pict-width.md) property. If the individual width and height are linearly settable and orthogonal to each other, you can express them as a range.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPC_PICT_WIDTH**](wia-dpc-pict-width.md)
