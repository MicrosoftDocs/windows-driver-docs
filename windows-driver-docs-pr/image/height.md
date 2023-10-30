---
title: Height element
description: The Height element specifies a height value that the scan device supports for scanner configuration elements that require a height.
keywords: ["Height element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Height wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 04/25/2023
---

# Height element

The **Height** element specifies a height value that the scan device supports for scanner configuration elements that require a height.

## Usage

```xml
<wscn:Height wscn:Override="" wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:Height wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **Override** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **UsedDefault** | xs:string | No | Optional. A Boolean value of 0, false, 1, or true.**falsetrue** |

## Text value

Required. For possible values, see the specific parent element.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**Heights**](heights.md) |
| [**InputMediaSize**](inputmediasize.md) |
| [**PlatenMaximumSize**](platenmaximumsize.md) |
| [**PlatenMinimumSize**](platenminimumsize.md) |
| [**PlatenOpticalResolution**](platenopticalresolution.md) |

## Remarks

The value of the **Height** element depends on its parent element. For more information about whether **Height** is required or optional and about its possible values, see the appropriate parent value.

[**DocumentFinalParameters**](documentfinalparameters.md)

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Height** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also

[**DocumentFinalParameters**](documentfinalparameters.md)

[**Heights**](heights.md)

[**InputMediaSize**](inputmediasize.md)

[**PlatenMaximumSize**](platenmaximumsize.md)

[**PlatenMinimumSize**](platenminimumsize.md)

[**PlatenOpticalResolution**](platenopticalresolution.md)

[**Width**](width.md)
