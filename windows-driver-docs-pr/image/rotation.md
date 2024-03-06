---
title: Rotation Element
description: The optional Rotation element specifies the amount to rotate each image of the scanned document.
keywords: ["Rotation element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Rotation wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 05/01/2023
---

# Rotation element

The optional **Rotation** element specifies the amount to rotate each image of the scanned document.

## Usage

```xml
<wscn:Rotation wscn:MustHonor="" wscn:Override="" wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:Rotation wscn:MustHonor="" wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **Override** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **UsedDefault** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

Required. One of 0, 90, 180, or 270.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md) |

## Remarks

The integer value of the **Rotation** element specifies the clockwise rotation to apply to each image of the scanned document. All WSD Scan Services must support the value 0 (that is, no rotation).

The client can specify the optional **MustHonor** attribute only when the **Rotation** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Rotation** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)
