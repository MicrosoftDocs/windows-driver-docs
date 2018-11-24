---
title: JobHistory element
description: The optional JobHistory element contains information about scan jobs that have recently completed processing.
ms.assetid: 7f46044e-ac34-4181-9a35-62dea5ec8c82
keywords: ["JobHistory element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobHistory
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobHistory element


The optional **JobHistory** element contains information about scan jobs that have recently completed processing.

Usage
-----

```xml
<wscn:JobHistory>
  child elements
</wscn:JobHistory>
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
<td><p><a href="job.md" data-raw-source="[&lt;strong&gt;Job&lt;/strong&gt;](job.md)"><strong>Job</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobsummary.md" data-raw-source="[&lt;strong&gt;JobSummary&lt;/strong&gt;](jobsummary.md)"><strong>JobSummary</strong></a></p></td>
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
<td><p><a href="getjobhistoryresponse.md" data-raw-source="[&lt;strong&gt;GetJobHistoryResponse&lt;/strong&gt;](getjobhistoryresponse.md)"><strong>GetJobHistoryResponse</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobtable.md" data-raw-source="[&lt;strong&gt;JobTable&lt;/strong&gt;](jobtable.md)"><strong>JobTable</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobHistory** element contains a subset of the most recent jobs that have finished processing. These jobs could have scanned, been aborted, or failed for other reasons. The maximum number of jobs in this list depends on the device.

A client can ask for job history through the [**GetJobHistoryRequest**](getjobhistoryrequest.md) operation element. The WSD Scan Service returns this history in a [**GetJobHistoryResponse**](getjobhistoryresponse.md) operation element.

## See also


[**GetJobHistoryRequest**](getjobhistoryrequest.md)

[**GetJobHistoryResponse**](getjobhistoryresponse.md)

[**Job**](job.md)

[**JobSummary**](jobsummary.md)

[**JobTable**](jobtable.md)

 

 






