---
title: Brightness Element
description: The optional Brightness element specifies the relative amount to reduce or enhance the brightness of the scanned document.
keywords: ["Brightness element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Brightness wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 03/27/2023
---

# Brightness element

The optional **Brightness** element specifies the relative amount to reduce or enhance the brightness of the scanned document.

## Usage

```xml
<wscn:Brightness wscn:Override="" wscn:UsedDefault=""
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:Brightness wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| ****Override**** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| ****UsedDefault**** | xs:string | No | Optional. A boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

The Brightness value must lie in the range from -1000 through 1000, inclusive.**Brightness**

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ExposureSettings**](exposuresettings.md) |

## Remarks

The **Brightness** element indicates the relative amount to reduce or enhance the brightness of the scanned document. A value of 0 indicates that the WSD Scan Service should make no adjustments to the scanned brightness.

All WSD Scan Services must support all values from, and including, -1000 through 1000. The services must internally map these values to the actual **Brightness** values that the scan device supports.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Brightness** element is contained within a [**DocumentFinalParameters**](documentfinalparameters.md) hierarchy. For more information about **Override** and **UsedDefault** and their usage, see **DocumentFinalParameters**.

You can subset the allowed values for the **Brightness** element.

## See also

[**DocumentFinalParameters**](documentfinalparameters.md)

[**ExposureSettings**](exposuresettings.md)
