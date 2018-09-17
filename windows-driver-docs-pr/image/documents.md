---
title: Documents element
description: The required Documents element contains the actual scan characteristics that are used during image acquisition, plus a collection of all Document elements that the scan job contains.
ms.assetid: b547ed17-b533-4dde-8194-dee1b0f9f85f
keywords: ["Documents element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Documents
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Documents element


The required **Documents** element contains the actual scan characteristics that are used during image acquisition, plus a collection of all **Document** elements that the scan job contains.

Usage
-----

``` syntax
<wscn:Documents>
  child elements
</wscn:Documents>
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
<td><p>[<strong>Document</strong>](document.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DocumentFinalParameters</strong>](documentfinalparameters.md)</p></td>
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
<td><p>[<strong>Job</strong>](job.md)</p></td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**Document**](document.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**Job**](job.md)

 

 






