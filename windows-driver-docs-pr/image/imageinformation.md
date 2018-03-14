---
title: ImageInformation element
description: The required ImageInformation element contains information about the resulting image data from a scan made with a ScanTicket element that is currently being validated.
ms.assetid: 58a5dc09-07fa-4e31-93f1-7370dace3263
keywords: ["ImageInformation element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ImageInformation
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ImageInformation element


The required **ImageInformation** element contains information about the resulting image data from a scan made with a [**ScanTicket**](scanticket.md) element that is currently being validated.

Usage
-----

``` syntax
<wscn:ImageInformation>
  child elements
</wscn:ImageInformation>
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
<td><p>[<strong>MediaBackImageInfo</strong>](mediabackimageinfo.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>MediaFrontImageInfo</strong>](mediafrontimageinfo.md)</p></td>
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
<td><p>[<strong>ValidationInfo</strong>](validationinfo.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service returns the **ImageInformation** element through the [**CreateScanJobResponse**](createscanjobresponse.md) operation element. Scan applications can use the data that is specified within **ImageInformation** to decode the image within an image file.

## <span id="see_also"></span>See also


[**CreateScanJobResponse**](createscanjobresponse.md)

[**MediaBackImageInfo**](mediabackimageinfo.md)

[**MediaFrontImageInfo**](mediafrontimageinfo.md)

[**ValidationInfo**](validationinfo.md)

 

 






