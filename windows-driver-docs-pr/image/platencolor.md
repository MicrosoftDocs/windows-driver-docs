---
title: PlatenColor Element
description: The required PlatenColor element contains a list of ColorEntry elements that describe the color processing capabilities of the platen.
keywords: ["PlatenColor element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn PlatenColor
api_type:
- Schema
ms.date: 05/01/2023
---

# PlatenColor element

The required **PlatenColor** element contains a list of [**ColorEntry**](colorentry.md) elements that describe the color processing capabilities of the platen.

## Usage

```xml
<wscn:PlatenColor>
  child elements
</wscn:PlatenColor>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ColorEntry**](colorentry.md) |

## Parent elements

| Element |
|--|
| [**Platen**](platen.md) |

## Remarks

The **PlatenColor** element contains the information needed to determine the type of color processing and acquisition that the flatbed platen supports. The amount of information that is needed to describe each pixel depends on the specific [**ColorEntry**](colorentry.md) keyword. Black and white images require only one bit per pixel (bpp), whereas grayscale and color images require significantly more information. The exact amount of information is determined by the color space and technical capabilities of the scan device.

Another important aspect of the returned scan data is the photometric interpretation of the acquired data. All image data that the scan device returns is required to be black on white, where black is represented by 0 and white is represented by 1.

## See also

[**ColorEntry**](colorentry.md)

[**Platen**](platen.md)
