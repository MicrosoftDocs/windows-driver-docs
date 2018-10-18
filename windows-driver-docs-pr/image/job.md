---
title: Job element
description: The required Job element contains all elements that are associated with a scan job.
ms.assetid: c5622ea6-c57a-4c80-a6ef-e6b9014b2b59
keywords: ["Job element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Job
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Job element


The required **Job** element contains all elements that are associated with a scan job.

Usage
-----

```xml
<wscn:Job>
  child elements
</wscn:Job>
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
<td><p>[<strong>Documents</strong>](documents.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScanTicket</strong>](scanticket.md)</p></td>
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
<td><p>[<strong>ActiveJobs</strong>](activejobs.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A scan job (which the **Job** element represents) can contain one or more documents. The WSD Scan Service's processing instructions for both a job and its documents are executed at the **Job** level.

## See also


[**ActiveJobs**](activejobs.md)

[**Documents**](documents.md)

[**JobStatus**](jobstatus.md)

[**ScanTicket**](scanticket.md)

 

 






