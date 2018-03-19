---
title: JobTable element
description: The required JobTable element contains current and historical information about scan jobs.
ms.assetid: 349ca443-5296-4200-884d-91fcdb222be4
keywords: ["JobTable element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobTable
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# JobTable element


The required **JobTable** element contains current and historical information about scan jobs.

Usage
-----

``` syntax
<wscn:JobTable>
  child elements
</wscn:JobTable>
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
<td><p>[<strong>ActiveJobs</strong>](activejobs.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobHistory</strong>](jobhistory2.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service uses a **JobTable** element to track all current and finished scan jobs that are submitted to the WSD Scan Service. Current jobs are tracked in the [**ActiveJobs**](activejobs.md) child element; finished jobs are optionally tracked in the [**JobHistory**](jobhistory2.md) child element.

## <span id="see_also"></span>See also


[**ActiveJobs**](activejobs.md)

[**JobHistory**](jobhistory2.md)

 

 






