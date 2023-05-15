---
title: ScanRegion element
description: The optional ScanRegion element specifies the area to scan within the input document boundaries.
keywords: ["ScanRegion element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScanRegion
api_type:
- Schema
ms.date: 05/02/2023
---

# ScanRegion element

The optional **ScanRegion** element specifies the area to scan within the input document boundaries.

## Usage

```xml
<wscn:ScanRegion>
  child elements
</wscn:ScanRegion>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ScanRegionHeight**](scanregionheight.md) |
| [**ScanRegionWidth**](scanregionwidth.md) |
| [**ScanRegionXOffset**](scanregionxoffset.md) |
| [**ScanRegionYOffset**](scanregionyoffset.md) |

## Parent elements

| Element |
|--|
| [**MediaBack**](mediaback.md) |
| [**MediaFront**](mediafront.md) |

## Remarks

All **ScanRegion** values represent one-thousandths (1/1000) of an inch.

If the requested scan region of a scan job would fall completely outside the supported acquisition area of the scan device, the scan operation should be rejected.

[**ScanRegionXOffset**](scanregionxoffset.md) + [**ScanRegionWidth**](scanregionwidth.md) must be equal or less than the [**InputSize**](inputsize.md) width.

[**ScanRegionYOffset**](scanregionyoffset.md) + [**ScanRegionHeight**](scanregionheight.md) must be equal or less than the **InputSize** height.

The WSD Scan Service can adjust a requested scan region if it cannot fulfill the specified dimensions. Any changes to the scan region should be reported in the [**DocumentFinalParameters**](documentfinalparameters.md) elements in the scan job.

## See also

[**DocumentFinalParameters**](documentfinalparameters.md)

[**InputSize**](inputsize.md)

[**MediaBack**](mediaback.md)

[**MediaFront**](mediafront.md)

[**ScanRegionHeight**](scanregionheight.md)

[**ScanRegionWidth**](scanregionwidth.md)

[**ScanRegionXOffset**](scanregionxoffset.md)

[**ScanRegionYOffset**](scanregionyoffset.md)
