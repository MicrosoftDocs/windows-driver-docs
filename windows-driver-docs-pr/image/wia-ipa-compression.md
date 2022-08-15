---
title: WIA_IPA_COMPRESSION
description: The WIA_IPA_COMPRESSION property contains the current compression type that is used. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_COMPRESSION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_COMPRESSION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/04/2021
---

# WIA_IPA_COMPRESSION

The WIA_IPA_COMPRESSION property contains the current compression type that is used. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write (image acquisitions); read-only (image storage)

## Remarks

An application reads the WIA_IPA_COMPRESSION property to determine the image compression type, or the application sets this property to configure the compression setting.

The following table describes the constants that are valid with WIA_IPA_COMPRESSION.

| Value | Definition |
|--|--|
| WIA_COMPRESSION_BI_RLE4 | RLE 4 compression |
| WIA_COMPRESSION_BI_RLE8 | RLE 8 compression |
| WIA_COMPRESSION_G3 | Group 3 compression |
| WIA_COMPRESSION_G4 | Group 4 compression |
| WIA_COMPRESSION_JBIG | IS 11544 (ITU-T T.82) compression |
| WIA_COMPRESSION_JPEG | JPEG compression |
| WIA_COMPRESSION_JPEG2K | JPEG 2000 compression |
| WIA_COMPRESSION_NONE | No compression |
| WIA_COMPRESSION_PNG | W3C PNG compression |

> [!NOTE]
> When the file format is WiaImgFmt_XPS or WiaImgFmt_PDFA, WIA_COMPRESSION_NONE means "not defined"; the device cannot choose the internal compression (if any) for images that are stored in these two document formats.

All WIA 2.0 minidrivers must set the initial value of this property to its default value, which is WIA_COMPRESSION_NONE.

The access rights of the WIA_IPA_COMPRESSION property are read/write for all image acquisitions but read-only for stored image items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
