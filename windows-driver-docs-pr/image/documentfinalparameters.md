---
title: DocumentFinalParameters element
description: The required DocumentFinalParameters element contains the actual DocumentParameters element that the scan device uses for image acquisition.
keywords: ["DocumentFinalParameters element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DocumentFinalParameters
api_type:
- Schema
ms.date: 04/24/2023
---

# DocumentFinalParameters element

The required **DocumentFinalParameters** element contains the actual [**DocumentParameters**](documentparameters.md) element that the scan device uses for image acquisition.

## Usage

```xml
<wscn:DocumentFinalParameters>
  child elements
</wscn:DocumentFinalParameters>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**CompressionQualityFactor**](compressionqualityfactor.md) |
| [**ContentType**](contenttype.md) |
| [**Exposure**](exposure.md) |
| [**FilmScanMode**](filmscanmode.md) |
| [**Format**](format.md) |
| [**ImagesToTransfer**](imagestotransfer.md) |
| [**InputSize**](inputsize.md) |
| [**InputSource**](inputsource.md) |
| [**MediaSides**](mediasides.md) |
| [**Rotation**](rotation.md) |
| [**Scaling**](scaling.md) |

## Parent elements

| Element |
|--|
| [**CreateScanJobResponse**](createscanjobresponse.md) |
| [**Documents**](documents.md) |

## Remarks

The **DocumentFinalParameters** element contains elements that contain the actual scan job values that the WSD Scan Service uses. These values might differ from the values that are requested in the job [**ScanTicket**](scanticket.md) for various reasons. Each parameter is represented in this hierarchy and must be filled in when the values are known.

Certain elements within the **DocumentFinalParameters** hierarchy can contain the **Override** and **UsedDefault** Boolean attributes. If the **Override** attribute is present and true in an element, the scan device overrode a requested value with the specified value. If the **UsedDefault** attribute is present and true in an element, the scan device used the specified default value.

[**Brightness**](brightness.md)[**ColorProcessing**](colorprocessing.md)[**CompressionQualityFactor**](compressionqualityfactor.md)[**ContentType**](contenttype.md)[**Contrast**](contrast.md)[**FilmScanMode**](filmscanmode.md)[**Format**](format.md)[**Height**](height.md)[**ImagesToTransfer**](imagestotransfer.md)[**InputSource**](inputsource.md)[**Rotation**](rotation.md)[**ScalingHeight**](scalingheight.md)[**ScalingWidth**](scalingwidth.md)[**ScanRegionHeight**](scanregionheight.md)[**ScanRegionWidth**](scanregionwidth.md)[**ScanRegionXOffset**](scanregionxoffset.md)[**ScanRegionYOffset**](scanregionyoffset.md)[**Sharpness**](sharpness.md)[**Width**](width.md)

The following elements can have the **Override** and **UsedDefault** attributes: [**Brightness**](brightness.md), [**ColorProcessing**](colorprocessing.md), [**CompressionQualityFactor**](compressionqualityfactor.md), [**ContentType**](contenttype.md), [**Contrast**](contrast.md), [**FilmScanMode**](filmscanmode.md), [**Format**](format.md), [**Height**](height.md), [**ImagesToTransfer**](imagestotransfer.md), [**InputSource**](inputsource.md), [**Rotation**](rotation.md), [**ScalingHeight**](scalingheight.md), [**ScalingWidth**](scalingwidth.md), [**ScanRegionHeight**](scanregionheight.md), [**ScanRegionWidth**](scanregionwidth.md), [**ScanRegionXOffset**](scanregionxoffset.md), [**ScanRegionYOffset**](scanregionyoffset.md), [**Sharpness**](sharpness.md), and [**Width**](width.md).

## See also

[**Brightness**](brightness.md)

[**ColorProcessing**](colorprocessing.md)

[**CompressionQualityFactor**](compressionqualityfactor.md)

[**ContentType**](contenttype.md)

[**Contrast**](contrast.md)

[**CreateScanJobResponse**](createscanjobresponse.md)

[**DocumentParameters**](documentparameters.md)

[**Documents**](documents.md)

[**Exposure**](exposure.md)

[**FilmScanMode**](filmscanmode.md)

[**Format**](format.md)

[**Height**](height.md)

[**ImagesToTransfer**](imagestotransfer.md)

[**InputSize**](inputsize.md)

[**InputSource**](inputsource.md)

[**MediaSides**](mediasides.md)

[**Rotation**](rotation.md)

[**Scaling**](scaling.md)

[**ScalingHeight**](scalingheight.md)

[**ScalingWidth**](scalingwidth.md)

[**ScanRegionHeight**](scanregionheight.md)

[**ScanRegionWidth**](scanregionwidth.md)

[**ScanRegionXOffset**](scanregionxoffset.md)

[**ScanRegionYOffset**](scanregionyoffset.md)

[**ScanTicket**](scanticket.md)

[**Sharpness**](sharpness.md)

[**Width**](width.md)
