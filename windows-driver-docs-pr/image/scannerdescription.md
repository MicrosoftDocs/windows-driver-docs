---
title: ScannerDescription element
description: ScannerDescription element
ms.assetid: 4429702e-18de-4b7c-83a2-ac405517e730
keywords: ["ScannerDescription element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerDescription
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ScannerDescription element


Usage
-----

``` syntax
<wscn:ScannerDescription>
  child elements
</wscn:ScannerDescription>
```

Attributes
----------

There are no attributes.

Text value
----------

None

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
<td><p>[<strong>ScannerInfo</strong>](scannerinfo.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScannerLocation</strong>](scannerlocation.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScannerName</strong>](scannername.md)</p></td>
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
<td><p>[<strong>ElementChanges</strong>](elementchanges.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ElementData for parent ScannerElements</strong>](elementdata-for-scannerelements-element.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

The **ScannerDescription** element contains information about the scanner that rarely or never changes. A client retrieves this information by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation element.

## <span id="see_also"></span>See also


[**ElementChanges**](elementchanges.md)

[**ElementData for parent ScannerElements**](elementdata-for-scannerelements-element.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerInfo**](scannerinfo.md)

[**ScannerLocation**](scannerlocation.md)

[**ScannerName**](scannername.md)

 

 






