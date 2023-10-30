---
title: RotationValue element
description: The required RotationValue element specifies a single rotation value supported by the scan device.
keywords: ["RotationValue element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn RotationValue
api_type:
- Schema
ms.date: 05/01/2023
---

# RotationValue element

The required **RotationValue** element specifies a single rotation value supported by the scan device.

## Usage

```xml
<wscn:RotationValue>
  text
</wscn:RotationValue>
```

## Attributes

There are no attributes.

## Text value

Required. A numeric value that must be 0, 90, 180, or 270.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**RotationsSupported**](rotationssupported.md) |

## Remarks

The **RotationValue** element specifies the number of degrees that the scanner should rotate each image of a scanned document. All rotations are applied in the clockwise direction.

All WSD Scan Services must support the value of 0. You can both extend and subset the allowed values for this element.

## See also

[**RotationsSupported**](rotationssupported.md)
