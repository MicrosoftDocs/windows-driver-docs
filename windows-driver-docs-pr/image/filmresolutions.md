---
title: FilmResolutions Element
description: The required FilmResolutions element contains a list of resolutions at which the scanner's film scanning input source can scan.
keywords: ["FilmResolutions element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn FilmResolutions
api_type:
- Schema
ms.date: 04/25/2023
---

# FilmResolutions element

The required **FilmResolutions** element contains a list of resolutions at which the scanner's film scanning input source can scan.

## Usage

```xml
<wscn:FilmResolutions>
  child elements
</wscn:FilmResolutions>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**Heights**](heights.md) |
| [**Widths**](widths.md) |

## Parent elements

| Element |
|--|
| [**Film**](film.md) |

## Remarks

The resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

The WSD Scan Service should list all possible widths that the scan device supports within the **Widths** child element and all possible heights that the scan device supports within the **Heights** child element. All **Width** and **Height** values are independent of each other, and most devices will support them being paired in any combination within a [**ScanTicket**](scanticket.md) element.

## See also

[**Film**](film.md)

[**Height**](height.md)

[**Heights**](heights.md)

[**ScanTicket**](scanticket.md)

[**Width**](width.md)

[**Widths**](widths.md)
