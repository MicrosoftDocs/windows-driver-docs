---
title: ScalingHeight element (slow scan direction)
description: The required ScalingHeight element specifies the document scaling in the slow scan direction.
keywords: ["ScalingHeight element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScalingHeight wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 07/06/2020
ms.localizationpriority: medium
---

# ScalingHeight element (slow scan direction)

The required **ScalingHeight** element specifies the document scaling in the slow scan direction.

## Usage

```xml
<wscn:ScalingHeight wscn:Override="" wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ScalingHeight wscn:Override="" wscn:UsedDefault="">
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

The **ScalingHeight** element specifies the scaling factor to apply in the slow scan direction. Scaling is expressed in 1 percent increments, where a value of 100 indicates a 100% width scale (no adjustment to the document height).

All WSD Scan Services must support at least the value 100.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ScalingHeight** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can subset the allowed values for this element.

## See also

[**DocumentFinalParameters**](documentfinalparameters.md)

[**Scaling**](scaling.md)

[**ScalingWidth**](scalingwidth.md)
