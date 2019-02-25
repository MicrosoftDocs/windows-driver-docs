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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# RequestedElements element


The required **RequestedElements** element identifies the elements that the client wants data for when it calls [**GetScannerElementsRequest**](getscannerelementsrequest.md) or [**GetJobElementsRequest**](getjobelementsrequest.md).

Usage
-----

```xml
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
<td><p><a href="name-for-requestedelements-element.md" data-raw-source="[&lt;strong&gt;Name for RequestedElements Element&lt;/strong&gt;](name-for-requestedelements-element.md)"><strong>Name for RequestedElements Element</strong></a></p></td>
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
<td><p><a href="getjobelementsrequest.md" data-raw-source="[&lt;strong&gt;GetJobElementsRequest&lt;/strong&gt;](getjobelementsrequest.md)"><strong>GetJobElementsRequest</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="getscannerelementsrequest.md" data-raw-source="[&lt;strong&gt;GetScannerElementsRequest&lt;/strong&gt;](getscannerelementsrequest.md)"><strong>GetScannerElementsRequest</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **RequestedElements** element contains one or more **Name** elements for parent **RequestedElements** elements that identify the data that the client is querying.

## See also


[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Name for RequestedElements Element**](name-for-requestedelements-element.md)

 

 






