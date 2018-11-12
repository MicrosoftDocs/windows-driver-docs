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
<td><p><a href="documents.md" data-raw-source="[&lt;strong&gt;Documents&lt;/strong&gt;](documents.md)"><strong>Documents</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobstatus.md" data-raw-source="[&lt;strong&gt;JobStatus&lt;/strong&gt;](jobstatus.md)"><strong>JobStatus</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="scanticket.md" data-raw-source="[&lt;strong&gt;ScanTicket&lt;/strong&gt;](scanticket.md)"><strong>ScanTicket</strong></a></p></td>
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
<td><p><a href="activejobs.md" data-raw-source="[&lt;strong&gt;ActiveJobs&lt;/strong&gt;](activejobs.md)"><strong>ActiveJobs</strong></a></p></td>
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

 

 






