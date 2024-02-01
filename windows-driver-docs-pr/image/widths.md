---
title: Widths Element
description: The required Widths element contains the list of widths at which the scanner can scan images.
keywords: ["Widths element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Widths
api_type:
- Schema
ms.date: 05/02/2023
---

# Widths element

The required **Widths** element contains the list of widths at which the scanner can scan images.

## Usage

```xml
<wscn:Widths>
  child elements
</wscn:Widths>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**Width**](width.md) |

## Parent elements

| Element |
|--|
| [**ADFResolutions**](adfresolutions.md) |
| [**FilmResolutions**](filmresolutions.md) |
| [**PlatenResolutions**](platenresolutions.md) |

## Remarks

Each [**Width**](width.md) child element specifies a valid number of horizontal pixels per inch at which the device can scan images.

The [**Heights**](heights.md) element contains the list of heights that the scanner supports.

## See also

[**ADFResolutions**](adfresolutions.md)

[**FilmResolutions**](filmresolutions.md)

[**Height**](height.md)

[**Heights**](heights.md)

[**PlatenResolutions**](platenresolutions.md)

[**Width**](width.md)
