---
title: ScalingWidth Element (Fast Scan Direction)
description: The required ScalingWidth element specifies the document scaling in the fast scan direction.
keywords: ["ScalingWidth element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScalingWidth wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 07/06/2020
---

# ScalingWidth element (fast scan direction)

The required **ScalingWidth** element specifies the document scaling in the fast scan direction.

## Usage

```xml
<wscn:ScalingWidth wscn:Override="" wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ScalingWidth wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **Override** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true. |
| **UsedDefault** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true. |

## Text value

Required. An integer in the range from 1 through 1000, inclusive.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**Scaling**](scaling.md) |

## Remarks

The **ScalingWidth** element specifies the scaling factor to apply in the fast scan direction. Scaling is expressed in 1 percent increments, where a value of 100 indicates a 100% width scale (no adjustment to the document width).

All WSD Scan Services must support at least the value 100.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ScalingWidth** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can subset the allowed values for this element.

## See also

[**DocumentFinalParameters**](documentfinalparameters.md)

[**Scaling**](scaling.md)

[**ScalingHeight**](scalingheight.md)
