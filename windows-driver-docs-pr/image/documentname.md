---
title: DocumentName element
description: The required DocumentName element contains the name of the document that the client supplies.
ms.assetid: 7d6d7dcd-db5d-420d-9e5f-3badeb0a511c
keywords: ["DocumentName element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DocumentName
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DocumentName element


The required **DocumentName** element contains the name of the document that the client supplies.

Usage
-----

``` syntax
<wscn:DocumentName>
  text
</wscn:DocumentName>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any character string.

## Child elements


There are no child elements.

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
<td><p>[<strong>DocumentDescription</strong>](documentdescription.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service must supply a value to store the document on the client.

## <span id="see_also"></span>See also


[**DocumentDescription**](documentdescription.md)

 

 






