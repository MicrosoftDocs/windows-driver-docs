---
title: FilmOpticalResolution Element
description: The required FilmOpticalResolution element specifies the maximum optical resolution at which the film scanning input source can scan.
keywords: ["FilmOpticalResolution element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn FilmOpticalResolution
api_type:
- Schema
ms.date: 04/24/2023
---

# FilmOpticalResolution element

The required **FilmOpticalResolution** element specifies the maximum optical resolution at which the film scanning input source can scan.

## Usage

```xml
<wscn:FilmOpticalResolution/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**Film**](film.md) |

## Remarks

Resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

If **Height** is absent, the WSD Scan Service should assume a square image resolution. For example, if only a **Width** element of 100 is provided, assume that the resolution is 100 x 100 pixels per square inch.

## See also

[**Film**](film.md)

[**Height**](height.md)

[**Width**](width.md)
