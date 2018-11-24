---
title: DocumentFinalParameters element
description: The required DocumentFinalParameters element contains the actual DocumentParameters element that the scan device uses for image acquisition.
ms.assetid: 54e3c96c-70a1-48c5-8718-45b0a71ff9b1
keywords: ["DocumentFinalParameters element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DocumentFinalParameters
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DocumentFinalParameters element


The required **DocumentFinalParameters** element contains the actual [**DocumentParameters**](documentparameters.md) element that the scan device uses for image acquisition.

Usage
-----

```xml
<wscn:DocumentFinalParameters>
  child elements
</wscn:DocumentFinalParameters>
```

Attributes
----------

There are no attributes.

## Child elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="compressionqualityfactor.md" data-raw-source="[&lt;strong&gt;CompressionQualityFactor&lt;/strong&gt;](compressionqualityfactor.md)"><strong>CompressionQualityFactor</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="contenttype.md" data-raw-source="[&lt;strong&gt;ContentType&lt;/strong&gt;](contenttype.md)"><strong>ContentType</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="exposure.md" data-raw-source="[&lt;strong&gt;Exposure&lt;/strong&gt;](exposure.md)"><strong>Exposure</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="filmscanmode.md" data-raw-source="[&lt;strong&gt;FilmScanMode&lt;/strong&gt;](filmscanmode.md)"><strong>FilmScanMode</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="format.md" data-raw-source="[&lt;strong&gt;Format&lt;/strong&gt;](format.md)"><strong>Format</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="imagestotransfer.md" data-raw-source="[&lt;strong&gt;ImagesToTransfer&lt;/strong&gt;](imagestotransfer.md)"><strong>ImagesToTransfer</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="inputsize.md" data-raw-source="[&lt;strong&gt;InputSize&lt;/strong&gt;](inputsize.md)"><strong>InputSize</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="inputsource.md" data-raw-source="[&lt;strong&gt;InputSource&lt;/strong&gt;](inputsource.md)"><strong>InputSource</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="mediasides.md" data-raw-source="[&lt;strong&gt;MediaSides&lt;/strong&gt;](mediasides.md)"><strong>MediaSides</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="rotation.md" data-raw-source="[&lt;strong&gt;Rotation&lt;/strong&gt;](rotation.md)"><strong>Rotation</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="scaling.md" data-raw-source="[&lt;strong&gt;Scaling&lt;/strong&gt;](scaling.md)"><strong>Scaling</strong></a></p></td>
</tr>
</tbody>
</table>

## Parent elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="createscanjobresponse.md" data-raw-source="[&lt;strong&gt;CreateScanJobResponse&lt;/strong&gt;](createscanjobresponse.md)"><strong>CreateScanJobResponse</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="documents.md" data-raw-source="[&lt;strong&gt;Documents&lt;/strong&gt;](documents.md)"><strong>Documents</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

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

 

 






