---
title: ScannerElements element
description: The required ScannerElements contains all of the scanner information that is being returned to a client.
ms.assetid: 7e1b6e49-34a3-486f-83f2-472b181399d0
keywords: ["ScannerElements element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerElements
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ScannerElements element


The required **ScannerElements** contains all of the scanner information that is being returned to a client.

Usage
-----

``` syntax
<wscn:ScannerElements>
  child elements
</wscn:ScannerElements>
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
<td><p>[<strong>ElementData for ScannerElements Element</strong>](elementdata-for-scannerelements-element.md)</p></td>
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
<td><p>[<strong>GetScannerElementsResponse</strong>](getscannerelementsresponse.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service returns the **ScannerElements** element in the [**GetScannerElementsResponse**](getscannerelementsresponse.md) operation.

## <span id="see_also"></span>See also


[**ElementData for ScannerElements Element**](elementdata-for-scannerelements-element.md)

[**GetScannerElementsResponse**](getscannerelementsresponse.md)

 

 






