---
title: DocumentSizeAutoDetect element
description: The optional DocumentSizeAutoDetect element specifies whether the scan device automatically determines the size of the original scan media.
keywords: ["DocumentSizeAutoDetect element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DocumentSizeAutoDetect
api_type:
- Schema
ms.date: 04/24/2023
---

# DocumentSizeAutoDetect element

The optional **DocumentSizeAutoDetect** element specifies whether the scan device automatically determines the size of the original scan media.

## Usage

```xml
<wscn:DocumentSizeAutoDetect>
  text
</wscn:DocumentSizeAutoDetect>
```

## Attributes

There are no attributes.

## Text value

Required. A Boolean value that must be 0, false, 1, or true.**falsetrue**

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**InputSize**](inputsize.md) |

## Remarks

If the specified text value is 1 or **true**, the scan device will automatically determine the size of the original scan media. If the **DocumentSizeAutoDetect** element is specified along with a [**ScanRegion**](scanregion.md) element, the scan region will be ignored if it falls outside of the media size that the device detected.

## See also

[**ScanRegion**](scanregion.md)

[**InputSize**](inputsize.md)
