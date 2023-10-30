---
title: Sharpness element
description: The optional Sharpness element specifies the relative amount to reduce or enhance the sharpness of the scanned document.
keywords: ["Sharpness element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Sharpness wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 05/02/2023
---

# Sharpness element

The optional **Sharpness** element specifies the relative amount to reduce or enhance the sharpness of the scanned document.

## Usage

```xml
<wscn:Sharpness wscn:Override="" wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:Sharpness wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **Override** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **UsedDefault** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

A value in the range from -100 through 100, inclusive.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ExposureSettings**](exposuresettings.md) |

## Remarks

The **Sharpness** element indicates the relative amount to reduce or enhance the sharpness of the scanned document. A value of 0 indicates that the WSD Scan Service should make no adjustments to the scanned sharpness.

All Scan Services must support at least the value 0.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Sharpness** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can subset the allowed values for this element.

## See also

[**DocumentFinalParameters**](documentfinalparameters.md)

[**ExposureSettings**](exposuresettings.md)
