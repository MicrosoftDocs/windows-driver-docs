---
title: BytesPerLine Element
description: The required BytesPerLine element specifies the number of bytes per scan line in the resultant image file.
keywords: ["BytesPerLine element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn BytesPerLine
api_type:
- Schema
ms.date: 03/27/2023
---

# BytesPerLine element

The required **BytesPerLine** element specifies the number of bytes per scan line in the resultant image file.

## Usage

```xml
<wscn:BytesPerLine>
  text
</wscn:BytesPerLine>
```

## Attributes

There are no attributes.

## Text value

Required. An integer value from 0 through 2147483647.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**MediaBackImageInfo**](mediabackimageinfo.md) |
| [**MediaFrontImageInfo**](mediafrontimageinfo.md) |

## Remarks

The integer value that the WSD Scan Service returns is the total bytes that are required for both the data pixels and any padding that the scanner will add to each scan line.

[**Format**](format.md)

The **BytesPerLine** element is valid only if the requested [**Format**](format.md) value is an uncompressed file format. If the file format indicates compression, the Scan Service must return a value of zero for **BytesPerLine**.

## See also

[**Format**](format.md)

[**MediaBackImageInfo**](mediabackimageinfo.md)

[**MediaFrontImageInfo**](mediafrontimageinfo.md)
