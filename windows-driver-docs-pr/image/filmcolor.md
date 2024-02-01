---
title: FilmColor Element
description: The required FilmColor element contains the list of color processing capabilities that the film scanning input source supports.
keywords: ["FilmColor element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn FilmColor
api_type:
- Schema
ms.date: 04/24/2023
---

# FilmColor element

The required **FilmColor** element contains the list of color processing capabilities that the film scanning input source supports.

## Usage

```xml
<wscn:FilmColor>
  child elements
</wscn:FilmColor>
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
| [**Film**](film.md) |

## Remarks

The **FilmColor** element contains the information that is needed to determine the type of color processing and acquisition that the scanner's film scanning input source supports.

The amount of information that is needed to describe each pixel depends on the specific [**ColorEntry**](colorentry.md) keyword. Black and white images require only one bit per pixel (bpp), whereas grayscale and color images require significantly more information. The exact amount of information is determined by the color space and technical capabilities of the scan device.

Another important aspect of the returned scan data is the photometric interpretation of the acquired data. All image data that the scan device returns is required to be black on white, where black is represented by 0 and white is represented by 1.

## See also

[**ColorEntry**](colorentry.md)

[**Film**](film.md)
