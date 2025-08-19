---
title: CompressionQualityFactor Element
description: The optional CompressionQualityFactor element specifies an idealized integer amount of image quality, on a scale from 0 through 100.
keywords: ["CompressionQualityFactor element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn CompressionQualityFactor wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 03/29/2023
---

# CompressionQualityFactor element

The optional **CompressionQualityFactor** element specifies an idealized integer amount of image quality, on a scale from 0 through 100.

## Usage

```xml
<wscn:CompressionQualityFactor wscn:MustHonor=""                               wscn:Override=""                               wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:CompressionQualityFactor wscn:MustHonor=""                               wscn:Override=""                               wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **Override** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **UsedDefault** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

Required. An integer in the range from 0 through 100.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md) |

## Remarks

Any lossy compression type uses the integer value to determine the amount of acceptable image loss, where a higher value indicates a higher image quality and a correspondingly larger file size. A value of 100 indicates that the device should use the least amount of compression that it supports to produce the highest image quality possible. Currently, JPEG compression is the only supported lossy compression type.

If the requested image compression type is lossless and **MustHonor** is not present or is **false**, the WSD Scan Service should ignore the **CompressionQualityFactor** element and instead use a value of 100. If the compression type is lossless and **MustHonor** is **true**, the WSD Scan Service should reject the [**ScanTicket**](scanticket.md) element if a value other than 100 is specified.

The client can specify the optional **MustHonor** attribute only when the **CompressionQualityFactor** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **CompressionQualityFactor** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can subset the allowed values for this element.

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)
