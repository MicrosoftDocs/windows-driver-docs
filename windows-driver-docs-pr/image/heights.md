---
title: Heights element
description: The required Heights element contains the list of heights at which the scanner can scan images.
keywords: ["Heights element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Heights
api_type:
- Schema
ms.date: 04/25/2023
---

# Heights element

The required **Heights** element contains the list of heights at which the scanner can scan images.

## Usage

```xml
<wscn:Heights>
  child elements
</wscn:Heights>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**Height**](height.md) |

## Parent elements

| Element |
|--|
| [**ADFResolutions**](adfresolutions.md) |
| [**FilmResolutions**](filmresolutions.md) |
| [**PlatenResolutions**](platenresolutions.md) |

## Remarks

Each [**Height**](height.md) child element specifies a valid number of vertical pixels per inch at which the device can scan images.

The [**Widths**](widths.md) element contains the list of widths that the scanner supports.

## See also

[**ADFResolutions**](adfresolutions.md)

[**FilmResolutions**](filmresolutions.md)

[**Height**](height.md)

[**PlatenResolutions**](platenresolutions.md)

[**Width**](width.md)

[**Widths**](widths.md)
