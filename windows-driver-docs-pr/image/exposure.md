---
title: Exposure element
description: The optional Exposure element specifies the exposure settings of the document.
keywords: ["Exposure element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Exposure wscn MustHonor ""
api_type:
- Schema
ms.date: 04/24/2023
---

# Exposure element

The optional **Exposure** element specifies the exposure settings of the document.

## Usage

```xml
<wscn:Exposure wscn:MustHonor=""
  MustHonor = "xs:string">
  child elements
</wscn:Exposure wscn:MustHonor="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Child elements

| Element |
|--|
| [**AutoExposure**](autoexposure.md) |
| [**ExposureSettings**](exposuresettings.md) |

## Parent elements

| Element |
|--|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md) |

## Remarks

The **Exposure** element can contain a [**AutoExposure**](autoexposure.md) or [**ExposureSettings**](exposuresettings.md) element, but not both. **AutoExposure** specifies that the device should automatically employ image processing techniques to reduce the background of the document to a white image. **ExposureSettings** specifies the specific **Exposure** adjustment values that the WSD Scan Service should apply to the image data after acquisition.

The client can specify the optional **MustHonor** attribute only when the **Exposure** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

## See also

[**AutoExposure**](autoexposure.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**ExposureSettings**](exposuresettings.md)
