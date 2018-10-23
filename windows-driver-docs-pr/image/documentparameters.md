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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DocumentParameters element


The optional **DocumentParameters** element specifies the image processing functions to apply to documents in a job.

Usage
-----

```xml
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

## See also


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

 

 






