---
title: MaxValue Element
description: The required MaxValue element specifies the maximum value that the scan device supports for scanner configuration elements that require a range of values.
keywords: ["MaxValue element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn MaxValue
api_type:
- Schema
ms.date: 05/01/2023
---

# MaxValue element

The required **MaxValue** element specifies the maximum value that the scan device supports for scanner configuration elements that require a range of values.

## Usage

```xml
<wscn:MaxValue>
  text
</wscn:MaxValue>
```

## Attributes

There are no attributes.

## Text value

Required. For possible values, see the specific parent element.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**CompressionQualityFactorSupported**](compressionqualityfactorsupported.md) |
| [**ScalingHeight**](scalingheight2.md) |
| [**ScalingWidth**](scalingwidth2.md) |

## Remarks

The value of the **MaxValue** element depends on its parent element. For the possible values, see the appropriate parent element.

## See also

[**CompressionQualityFactorSupported**](compressionqualityfactorsupported.md)

[**MinValue**](minvalue.md)

[**ScalingHeight**](scalingheight2.md)

[**ScalingWidth**](scalingwidth2.md)
