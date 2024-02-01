---
title: PlatenOpticalResolution Element
description: The required PlatenOpticalResolution element specifies the maximum optical resolution at which the platen can scan.
keywords: ["PlatenOpticalResolution element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn PlatenOpticalResolution
api_type:
- Schema
ms.date: 05/01/2023
---

# PlatenOpticalResolution element

The required **PlatenOpticalResolution** element specifies the maximum optical resolution at which the platen can scan.

## Usage

```xml
<wscn:PlatenOpticalResolution>
  child elements
</wscn:PlatenOpticalResolution>
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

Resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

If the Height element is not specified, the WSD Scan Service should assume a square image resolution. For example, if only a **Width** element of 100 is provided, assume a resolution is 100 x 100 pixels per square inch.

## See also

[**Height**](height.md)

[**Platen**](platen.md)

[**Width**](width.md)
