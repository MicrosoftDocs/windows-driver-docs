---
title: Scaling Element
description: The optional Scaling element specifies the scaling of both the width and height of the scanned document.
keywords: ["Scaling element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Scaling wscn MustHonor ""
api_type:
- Schema
ms.date: 05/02/2023
---

# Scaling element

The optional **Scaling** element specifies the scaling of both the width and height of the scanned document.

## Usage

```xml
<wscn:Scaling wscn:MustHonor=""
  MustHonor = "xs:string">
  child elements
</wscn:Scaling wscn:MustHonor="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Child elements

| Element |
|--|
| [**ScalingHeight**](scalingheight.md) |
| [**ScalingWidth**](scalingwidth.md) |

## Parent elements

| Element |
|--|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md) |

## Remarks

The **Scaling** element must contain both the [**ScalingWidth**](scalingwidth.md) and [**ScalingHeight**](scalingheight.md) elements. The **ScalingWidth** element specifies the scaling in the fast scan direction, and the **ScalingHeight** element specifies the scaling in the slow scan direction.

The client can specify the optional **MustHonor** attribute only when the **Scaling** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**ScalingHeight**](scalingheight.md)

[**ScalingWidth**](scalingwidth.md)
