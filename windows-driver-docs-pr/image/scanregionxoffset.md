---
title: ScanRegionXOffset element
description: The optional ScanRegionXOffset element specifies the distance from the fast scan lead edge to the beginning of the scan region.
keywords: ["ScanRegionXOffset element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScanRegionXOffset wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 05/02/2023
---

# ScanRegionXOffset element

The optional **ScanRegionXOffset** element specifies the distance from the fast scan lead edge to the beginning of the scan region.

## Usage

```xml
<wscn:ScanRegionXOffset wscn:MustHonor="" wscn:Override="" wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ScanRegionXOffset wscn:MustHonor="" wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **Override** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **UsedDefault** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

Required. An integer between 0 and the InputSize width.[**InputSize**](inputsize.md)

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ScanRegion**](scanregion.md) |

## Remarks

For more information about the scan region parameters, see [**ScanRegion**](scanregion.md).

The client can specify the optional **MustHonor** attribute only when the **ScanRegionXOffset** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ScanRegionXOffset** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**InputSize**](inputsize.md)

[**ScanRegion**](scanregion.md)

[**ScanRegionYOffset**](scanregionyoffset.md)
