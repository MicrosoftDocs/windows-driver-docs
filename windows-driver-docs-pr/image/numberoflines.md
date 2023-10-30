---
title: NumberOfLines element
description: The required NumberOfLines element describes the exact height, in pixels, of the final output image.
keywords: ["NumberOfLines element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn NumberOfLines
api_type:
- Schema
ms.date: 05/01/2023
---

# NumberOfLines element

The required **NumberOfLines** element describes the exact height, in pixels, of the final output image.

## Usage

```xml
<wscn:NumberOfLines>
  text
</wscn:NumberOfLines>
```

## Attributes

There are no attributes.

## Text value

Required. An integer value in the range from 1 through 2147483647.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**MediaBackImageInfo**](mediabackimageinfo.md) |
| [**MediaFrontImageInfo**](mediafrontimageinfo.md) |

## Remarks

The specified value describes the exact height, in pixels, or the number of lines, of the final output image that would be generated for the current [**ScanTicket**](scanticket.md) settings that are being validated. This height includes rotation and any adjustment that the scanner might perform on the scanned image before transferring it to the client.

## See also

[**MediaBackImageInfo**](mediabackimageinfo.md)

[**MediaFrontImageInfo**](mediafrontimageinfo.md)

[**ScanTicket**](scanticket.md)
