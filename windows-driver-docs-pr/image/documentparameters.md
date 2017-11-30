---
title: DocumentParameters element
description: The optional DocumentParameters element specifies the image processing functions to apply to documents in a job.
ms.assetid: 3b76bf47-a674-4925-aa0f-b2310e1ad1ce
keywords: ["DocumentParameters element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DocumentParameters
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DocumentParameters element


The optional **DocumentParameters** element specifies the image processing functions to apply to documents in a job.

Usage
-----

``` syntax
<wscn:DocumentParameters>
  child elements
</wscn:DocumentParameters>
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
<td><p>[<strong>DefaultScanTicket</strong>](defaultscanticket.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanTicket</strong>](scanticket.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **DocumentParameters** element specifies the image processing functions and their values that will be applied against the job or document.

A client can optionally provide document processing parameters within the **ScanTicket** element during a [**CreateScanJobRequest**](createscanjobrequest.md) operation. The WSD Scan Service must validate all data that a client provides to ensure that each child element is set to a valid value that is specified in the [**ScannerConfiguration**](scannerconfiguration.md) element.

The WSD Scan Servie should use its default **DocumentParameters** values if the client does not provide any.

## <span id="see_also"></span>See also


[**CompressionQualityFactor**](compressionqualityfactor.md)

[**ContentType**](contenttype.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DefaultScanTicket**](defaultscanticket.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**Exposure**](exposure.md)

[**FilmScanMode**](filmscanmode.md)

[**Format**](format.md)

[**ImagesToTransfer**](imagestotransfer.md)

[**InputSize**](inputsize.md)

[**InputSource**](inputsource.md)

[**MediaSides**](mediasides.md)

[**Rotation**](rotation.md)

[**Scaling**](scaling.md)

[**ScanTicket**](scanticket.md)

[**ScannerConfiguration**](scannerconfiguration.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DocumentParameters%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





