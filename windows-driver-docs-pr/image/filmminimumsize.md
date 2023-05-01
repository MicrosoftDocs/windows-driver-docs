---
title: FilmMinimumSize element
description: The required FilmMinimumSize element specifies the smallest size original that an end user can scan with the film scanning option.
keywords: ["FilmMinimumSize element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn FilmMinimumSize
api_type:
- Schema
ms.date: 04/24/2023
---

# FilmMinimumSize element

The required **FilmMinimumSize** element specifies the smallest size original that an end user can scan with the film scanning option.

## Usage

```xml
<wscn:FilmMinimumSize>
  child elements
</wscn:FilmMinimumSize>
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
| [**Film**](film.md) |

## Remarks

The [**Width**](width.md) child element specifies the minimum size of media that the film scanning input source supports in the fast scan direction. The [**Height**](height.md) child element specifies the minimum size of media that the film scanning input source supports in the slow scan direction.

All media dimensions are measured in one-thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## See also

[**Film**](film.md)

[**Height**](height.md)

[**Width**](width.md)
