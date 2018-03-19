---
title: JobElements element
description: The required JobElements element contains all of the job-related elements that a client requests through a call to GetJobElementsRequest.
ms.assetid: ac7d8749-272d-4817-bc80-8f220e06436c
keywords: ["JobElements element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobElements
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# JobElements element


The required **JobElements** element contains all of the job-related elements that a client requests through a call to [**GetJobElementsRequest**](getjobelementsrequest.md).

Usage
-----

``` syntax
<wscn:JobElements>
  child elements
</wscn:JobElements>
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
<td><p>[<strong>ElementData for parent JobElements</strong>](elementdata-for-jobelements-element.md)</p></td>
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
<td><p>[<strong>GetJobElementsResponse</strong>](getjobelementsresponse.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service returns the **JobElements** element in [**GetJobElementsResponse**](getjobelementsresponse.md).

## <span id="see_also"></span>See also


[**ElementData for parent JobElements**](elementdata-for-jobelements-element.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetJobElementsResponse**](getjobelementsresponse.md)

 

 






