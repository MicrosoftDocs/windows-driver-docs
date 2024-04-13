---
title: MinValue Element
description: The required MinValue element specifies the minimum value that the scan device supports for scanner configuration elements that require a range of values.
keywords: ["MinValue element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn MinValue
api_type:
- Schema
ms.date: 05/01/2023
---

# MinValue element

The required **MinValue** element specifies the minimum value that the scan device supports for scanner configuration elements that require a range of values.

## Usage

```xml
<wscn:MinValue>
  text
</wscn:MinValue>
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

The value of the **MinValue** element depends on its parent element. For the possible values, see the appropriate parent element.

## See also

[**CompressionQualityFactorSupported**](compressionqualityfactorsupported.md)

[**MaxValue**](maxvalue.md)

[**ScalingHeight**](scalingheight2.md)

[**ScalingWidth**](scalingwidth2.md)
