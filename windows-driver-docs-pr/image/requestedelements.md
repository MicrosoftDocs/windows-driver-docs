---
title: RequestedElements element
description: The required RequestedElements element identifies the elements that the client wants data for when it calls GetScannerElementsRequest or GetJobElementsRequest.
ms.assetid: 0023afc1-723d-4b6a-9f1a-0bc21a309a65
keywords: ["RequestedElements element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn RequestedElements
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# RequestedElements element


The required **RequestedElements** element identifies the elements that the client wants data for when it calls [**GetScannerElementsRequest**](getscannerelementsrequest.md) or [**GetJobElementsRequest**](getjobelementsrequest.md).

Usage
-----

``` syntax
<wscn:RequestedElements>
  child elements
</wscn:RequestedElements>
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
<td><p>[<strong>Name for RequestedElements Element</strong>](name-for-requestedelements-element.md)</p></td>
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
<td><p>[<strong>GetJobElementsRequest</strong>](getjobelementsrequest.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GetScannerElementsRequest</strong>](getscannerelementsrequest.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **RequestedElements** element contains one or more **Name** elements for parent **RequestedElements** elements that identify the data that the client is querying.

## <span id="see_also"></span>See also


[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Name for RequestedElements Element**](name-for-requestedelements-element.md)

 

 






