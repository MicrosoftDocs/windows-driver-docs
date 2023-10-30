---
title: MediaFront element
description: The required MediaFront element contains all parameters that are specific to the scanning of the front side of the physical media.
keywords: ["MediaFront element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn MediaFront
api_type:
- Schema
ms.date: 05/01/2023
---

# MediaFront element

The required **MediaFront** element contains all parameters that are specific to the scanning of the front side of the physical media.

## Usage

```xml
<wscn:MediaFront>
  child elements
</wscn:MediaFront>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ColorProcessing**](colorprocessing.md) |
| [**Resolution**](resolution.md) |
| [**ScanRegion**](scanregion.md) |

## Parent elements

| Element |
|--|
| [**MediaSides**](mediasides.md) |

## Remarks

If the **MediaFront** element does not contain a [**ScanRegion**](scanregion.md) element, the WSD Scan Service should use 0 as the offsets and the width and height of the [**InputMediaSize**](inputmediasize.md), if given. If **ScanRegion** is missing and **InputMediaSize** is not specified or cannot be determined by the scan device, you can determine the implementation.

## See also

[**ColorProcessing**](colorprocessing.md)

[**InputMediaSize**](inputmediasize.md)

[**MediaBack**](mediaback.md)

[**MediaSides**](mediasides.md)

[**Resolution**](resolution.md)

[**ScanRegion**](scanregion.md)
