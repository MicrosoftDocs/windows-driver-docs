---
title: WIA_DPC_COMPRESSION_SETTING
description: The WIA_DPC_COMPRESSION_SETTING property contains either a range or a list of integers to represent perceived image quality.
keywords: ["WIA_DPC_COMPRESSION_SETTING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_COMPRESSION_SETTING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_COMPRESSION_SETTING

The WIA_DPC_COMPRESSION_SETTING property contains either a range or a list of integers to represent perceived image quality.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST or WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

The WIA_DPC_COMPRESSION_SETTING property is intended to approximately linearly describe the perceived image quality over a broad range of scene content. Smaller integers represent lower quality (that is, maximum compression), and larger integers represent higher quality (that is, minimum compression). Any available settings on a device are relative only to that device and are therefore device-specific.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
