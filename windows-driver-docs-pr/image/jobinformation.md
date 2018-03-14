---
title: JobInformation element
description: The optional JobInformation element describes the intended use of the job.
ms.assetid: 0e5d41a0-49df-43db-a2e6-3639e60d2378
keywords: ["JobInformation element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobInformation
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# JobInformation element


The optional **JobInformation** element describes the intended use of the job.

Usage
-----

``` syntax
<wscn:JobInformation>
  text
</wscn:JobInformation>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid character string.

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
<td><p>[<strong>JobDescription</strong>](jobdescription.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobInformation** value is useful when the client will reuse the scan ticket that is used to create the job.

## <span id="see_also"></span>See also


[**JobDescription**](jobdescription.md)

 

 






