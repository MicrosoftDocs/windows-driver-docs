---
title: Contrast element
description: The optional Contrast element specifies the relative amount to reduce or enhance the contrast of the scanned document.
keywords: ["Contrast element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Contrast wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 03/29/2023
---

# Contrast element

The optional **Contrast** element specifies the relative amount to reduce or enhance the contrast of the scanned document.

## Usage

```xml
<wscn:Contrast wscn:Override="" wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:Contrast wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| ****Override**** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| ****UsedDefault**** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

The Contrast value must lie in the range from -1000 through 1000, inclusive.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ExposureSettings**](exposuresettings.md) |

## Remarks

The **Contrast** element indicates the relative amount to enhance or reduce the contrast of the scanned document. A value of 0 indicates that the WSD Scan Service should make no adjustments to the scanned contrast.

All WSD Scan Services must support all values between, and including, -1000 to 1000. The services must internally map these values to the actual **Contrast** values that the scan device supports.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Contrast** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also

[**DocumentFinalParameters**](documentfinalparameters.md)

[**ExposureSettings**](exposuresettings.md)
