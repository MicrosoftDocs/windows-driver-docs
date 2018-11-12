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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScannerDescription element


Usage
-----

```xml
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
<td><p><a href="scannerinfo.md" data-raw-source="[&lt;strong&gt;ScannerInfo&lt;/strong&gt;](scannerinfo.md)"><strong>ScannerInfo</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="scannerlocation.md" data-raw-source="[&lt;strong&gt;ScannerLocation&lt;/strong&gt;](scannerlocation.md)"><strong>ScannerLocation</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="scannername.md" data-raw-source="[&lt;strong&gt;ScannerName&lt;/strong&gt;](scannername.md)"><strong>ScannerName</strong></a></p></td>
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
<td><p><a href="elementchanges.md" data-raw-source="[&lt;strong&gt;ElementChanges&lt;/strong&gt;](elementchanges.md)"><strong>ElementChanges</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="elementdata-for-scannerelements-element.md" data-raw-source="[&lt;strong&gt;ElementData for parent ScannerElements&lt;/strong&gt;](elementdata-for-scannerelements-element.md)"><strong>ElementData for parent ScannerElements</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

The **ScannerDescription** element contains information about the scanner that rarely or never changes. A client retrieves this information by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation element.

## See also


[**ElementChanges**](elementchanges.md)

[**ElementData for parent ScannerElements**](elementdata-for-scannerelements-element.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerInfo**](scannerinfo.md)

[**ScannerLocation**](scannerlocation.md)

[**ScannerName**](scannername.md)

 

 






