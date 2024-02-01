---
title: PlatenMinimumSize Element
description: The required PlatenMinimumSize element specifies the smallest size document that an end user can scan on the flatbed platen.
keywords: ["PlatenMinimumSize element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn PlatenMinimumSize
api_type:
- Schema
ms.date: 05/01/2023
---

# PlatenMinimumSize element

The required **PlatenMinimumSize** element specifies the smallest size document that an end user can scan on the flatbed platen.

## Usage

```xml
<wscn:PlatenMinimumSize>
  child elements
</wscn:PlatenMinimumSize>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**Height**](height.md) |
| [**Width**](width.md) |

## Parent elements

| Element |
|--|
| [**Platen**](platen.md) |

## Remarks

The [**Width**](width.md) child element specifies the minimum size of media that the platen supports in the fast scan direction. The [**Height**](height.md) child element specifies the minimum size of media that the platen supports in the slow scan direction.

All media dimensions are measured in one-thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## See also

[**Height**](height.md)

[**Platen**](platen.md)

[**Width**](width.md)
