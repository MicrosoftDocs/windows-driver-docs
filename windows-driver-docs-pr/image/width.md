---
title: Width element
description: The required Width element specifies a width value that the scan device supports for scanner configuration elements that require a Width.
keywords: ["Width element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Width wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 05/02/2023
---

# Width element

The required **Width** element specifies a width value that the scan device supports for scanner configuration elements that require a **Width**.

## Usage

```xml
<wscn:Width wscn:Override="" wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:Width wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **Override** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **UsedDefault** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

Required. For possible values, see the specific parent element.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ADFOpticalResolution**](adfopticalresolution.md) |
| [**InputMediaSize**](inputmediasize.md) |
| [**PlatenMaximumSize**](platenmaximumsize.md) |
| [**PlatenMinimumSize**](platenminimumsize.md) |
| [**PlatenOpticalResolution**](platenopticalresolution.md) |
| [**Widths**](widths.md) |

## Remarks

The **Width** element is a required child element for all of its parent elements. The value of **Width** depends on its parent element. For possible values, see the appropriate parent element.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Width** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and about their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also

[**ADFOpticalResolution**](adfopticalresolution.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**Height**](height.md)

[**InputMediaSize**](inputmediasize.md)

[**PlatenMaximumSize**](platenmaximumsize.md)

[**PlatenMinimumSize**](platenminimumsize.md)

[**PlatenOpticalResolution**](platenopticalresolution.md)

[**Widths**](widths.md)
