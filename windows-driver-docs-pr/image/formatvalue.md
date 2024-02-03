---
title: FormatValue Element
description: The required FormatValue element specifies a single supported file format and compression type.
keywords: ["FormatValue element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn FormatValue
api_type:
- Schema
ms.date: 09/27/2021
---

# FormatValue element

The required **FormatValue** element specifies a single supported file format and compression type.

## Usage

```xml
<wscn:FormatValue>
  text
</wscn:FormatValue>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| dib | Windows Device Independent Bitmap. |
| exif | Exchangeable Image File Format Version 2.x. |
| jbig | ISO/IEC 11544:1993 Standard - Coded representation of picture and audio information; progressive bi-level image compression. |
| jfif | JPEG File Interchange Format 1.x. |
| jpeg2k | JPEG 2000 standard-based file format and compression. |
| pdf-a | PDF/A format (standard based on ISO/CD 19005-1). |
| png | Portable Networks Graphics (PNG) format. This format supports only the PNG compression type. |
| tiff-single-uncompressed | Single page TIFF file with no compression type. |
| tiff-single-g4 | Single page TIFF file with g4 compression type. |
| tiff-single-g3mh | Single page TIFF file with g3mh compression type. |
| tiff-single-jpeg-tn2 | Single page TIFF file with jpeg compression type as described in Technical Note 2. |
| tiff-multi-uncompressed | Multiple page TIFF file with no compression type. |
| tiff-multi-g4 | Multiple page TIFF file with g4 compression type. |
| tiff-multi-g3mh | Multiple page TIFF file with g3mh compression type. |
| tiff-multi-jpeg-tn2 | Multiple page TIFF file with jpeg compression type as described in Technical Note 2. |
| xps | XML Paper Specification. |
| Any vendor-defined values. |  |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**FormatsSupported**](formatssupported.md) |

## Remarks

You can both extend and subset the allowed values for this element.

Although the WSD Scan Service supports the JBIG file format (ISO/IEC 11544:1993), it does *not* currently support JBIG2 (ISO/IEC 14492:2001).

## See also

[**FormatsSupported**](formatssupported.md)
