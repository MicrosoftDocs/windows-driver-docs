---
title: WIA_IPA_PROP_STREAM_COMPAT_ID
description: The WIA_IPA_PROP_STREAM_COMPAT_ID property specifies a class identifier (CLSID) that represents a set of device property values.
keywords: ["WIA_IPA_PROP_STREAM_COMPAT_ID Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_PROP_STREAM_COMPAT_ID
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA_IPA_PROP_STREAM_COMPAT_ID

The WIA_IPA_PROP_STREAM_COMPAT_ID property specifies a class identifier (CLSID) that represents a set of device property values.

Property Type: VT_CLSID

Valid Values: WIA_PROP_LIST

Access Rights: Read-only

## Remarks

If a device driver implements the WIA_IPA_PROP_STREAM_COMPAT_ID property, applications use this property to determine whether the device supports a set of values.

The following table describes the constants that are valid with WIA_IPA_PROP_STREAM_COMPAT_ID.

| Format | Description |
|--|--|
| WiaImgFmt_BMP | Microsoft Windows bitmap with a header file |
| WiaImgFmt_EMF | Extended Windows metafile |
| WiaImgFmt_EXIF | Exchangeable File Format |
| WiaImgFmt_FLASHPIX | FlashPix format |
| WiaImgFmt_GIF | GIF image format |
| WiaImgFmt_ICO | Windows icon file format |
| WiaImgFmt_JPEG | JPEG compressed format |
| WiaImgFmt_PHOTOCD | Eastman Kodak file format |
| WiaImgFmt_PNG | W3C PNG format |
| WiaImgFmt_MEMORYBMP | Windows bitmap without a header file |
| WiaImgFmt_TIFF | Tag Image File Format |
| WiaImgFmt_WMF | Windows metafile |

## Requirements

**Header:** wiadef.h (include Wiadef.h)
