---
title: PlatenMaximumSize Element
description: The required PlatenMaximumSize element specifies the largest size document that an end user can scan on the flatbed platen.
keywords: ["PlatenMaximumSize element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn PlatenMaximumSize
api_type:
- Schema
ms.date: 05/01/2023
---

# PlatenMaximumSize element

The required **PlatenMaximumSize** element specifies the largest size document that an end user can scan on the flatbed platen.

## Usage

```xml
<wscn:PlatenMaximumSize>
  child elements
</wscn:PlatenMaximumSize>
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

The [**Width**](width.md) child element specifies the maximum size of media that the platen supports in the fast scan direction. The [**Height**](height.md) child element specifies the maximum size of media that the platen supports in the slow scan direction.

All media dimensions are measured in one-thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## See also

[**Height**](height.md)

[**Platen**](platen.md)

[**Width**](width.md)
