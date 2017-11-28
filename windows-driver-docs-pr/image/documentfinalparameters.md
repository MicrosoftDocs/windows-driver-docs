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
---

# DocumentFinalParameters element


The required **DocumentFinalParameters** element contains the actual [**DocumentParameters**](documentparameters.md) element that the scan device uses for image acquisition.

Usage
-----

``` syntax
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
<td><p>[<strong>CompressionQualityFactor</strong>](compressionqualityfactor.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ContentType</strong>](contenttype.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>Exposure</strong>](exposure.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>FilmScanMode</strong>](filmscanmode.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>Format</strong>](format.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ImagesToTransfer</strong>](imagestotransfer.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>InputSize</strong>](inputsize.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>InputSource</strong>](inputsource.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>MediaSides</strong>](mediasides.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Rotation</strong>](rotation.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>Scaling</strong>](scaling.md)</p></td>
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
<td><p>[<strong>CreateScanJobResponse</strong>](createscanjobresponse.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Documents</strong>](documents.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **DocumentFinalParameters** element contains elements that contain the actual scan job values that the WSD Scan Service uses. These values might differ from the values that are requested in the job [**ScanTicket**](scanticket.md) for various reasons. Each parameter is represented in this hierarchy and must be filled in when the values are known.

Certain elements within the **DocumentFinalParameters** hierarchy can contain the **Override** and **UsedDefault** Boolean attributes. If the **Override** attribute is present and true in an element, the scan device overrode a requested value with the specified value. If the **UsedDefault** attribute is present and true in an element, the scan device used the specified default value.

[**Brightness**](brightness.md)[**ColorProcessing**](colorprocessing.md)[**CompressionQualityFactor**](compressionqualityfactor.md)[**ContentType**](contenttype.md)[**Contrast**](contrast.md)[**FilmScanMode**](filmscanmode.md)[**Format**](format.md)[**Height**](height.md)[**ImagesToTransfer**](imagestotransfer.md)[**InputSource**](inputsource.md)[**Rotation**](rotation.md)[**ScalingHeight**](scalingheight.md)[**ScalingWidth**](scalingwidth.md)[**ScanRegionHeight**](scanregionheight.md)[**ScanRegionWidth**](scanregionwidth.md)[**ScanRegionXOffset**](scanregionxoffset.md)[**ScanRegionYOffset**](scanregionyoffset.md)[**Sharpness**](sharpness.md)[**Width**](width.md)

The following elements can have the **Override** and **UsedDefault** attributes: [**Brightness**](brightness.md), [**ColorProcessing**](colorprocessing.md), [**CompressionQualityFactor**](compressionqualityfactor.md), [**ContentType**](contenttype.md), [**Contrast**](contrast.md), [**FilmScanMode**](filmscanmode.md), [**Format**](format.md), [**Height**](height.md), [**ImagesToTransfer**](imagestotransfer.md), [**InputSource**](inputsource.md), [**Rotation**](rotation.md), [**ScalingHeight**](scalingheight.md), [**ScalingWidth**](scalingwidth.md), [**ScanRegionHeight**](scanregionheight.md), [**ScanRegionWidth**](scanregionwidth.md), [**ScanRegionXOffset**](scanregionxoffset.md), [**ScanRegionYOffset**](scanregionyoffset.md), [**Sharpness**](sharpness.md), and [**Width**](width.md).

## <span id="see_also"></span>See also


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DocumentFinalParameters%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





