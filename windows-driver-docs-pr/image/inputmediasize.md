---
title: InputMediaSize element
description: The required InputMediaSize element specifies the size of the media to be scanned for the current job.
keywords: ["InputMediaSize element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn InputMediaSize
api_type:
- Schema
ms.date: 04/28/2023
---

# InputMediaSize element

The required **InputMediaSize** element specifies the size of the media to be scanned for the current job.

## Usage

```xml
<wscn:InputMediaSize>
  child elements
</wscn:InputMediaSize>
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
| [**InputSize**](inputsize.md) |

## Remarks

The **InputMediaSize** element contains the width and height of the input media to be scanned, specified in the [**Width**](width.md) and [**Height**](height.md) elements, respectively.

The **Width** element contains the width of the original media in the fast scan direction, and the **Height** element contains the height of the original media in the slow scan direction. Both **Width** and **Height** must be in the range from 1 through 2147483648 and are in units of one-thousandths (1/1000) of an inch.

## See also

[**Height**](height.md)

[**InputSize**](inputsize.md)

[**Width**](width.md)
