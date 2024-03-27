---
title: ScalingHeight Element (Output Document Height)
description: The required ScalingHeight element contains the range of allowable values for scaling the height of the output document.
keywords: ["ScalingHeight element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScalingHeight
api_type:
- Schema
ms.date: 07/06/2020
---

# ScalingHeight element (output document height)

The required **ScalingHeight** element contains the range of allowable values for scaling the height of the output document.

## Usage

```xml
<wscn:ScalingHeight>
  child elements
</wscn:ScalingHeight>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**MaxValue**](maxvalue.md) |
| [**MinValue**](minvalue.md) |

## Parent elements

| Element |
|--|
| [**ScalingRangeSupported**](scalingrangesupported.md) |

## Remarks

The **ScalingHeight** element contains the [**MinValue**](minvalue.md) and [**MaxValue**](maxvalue.md) elements that specify the minimum and maximum values that the scan device supports for scaling the height of an output document.

**MinValue** and **MaxValue** must be integers from 1 through 1000, with **MinValue** less than or equal to **MaxValue**. A value of 100 means that the scan device should not make any adjustments to the height of the scanned image. At a minimum, the WSD Scan Service must support the value of 100.

## See also

[**MaxValue**](maxvalue.md)

[**MinValue**](minvalue.md)

[**ScalingRangeSupported**](scalingrangesupported.md)

[**ScalingWidth2**](scalingwidth.md)
