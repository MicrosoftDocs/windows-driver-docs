---
title: ActiveJobs element
description: The required ActiveJobs element contains a list of all currently active scan jobs.
ms.assetid: 90acd196-60d3-43e5-9346-a8514bcf0bb8
keywords: ["ActiveJobs element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ActiveJobs
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ActiveJobs element


The required **ActiveJobs** element contains a list of all currently active scan jobs.

Usage
-----

```xml
<wscn:ActiveJobs>
  child elements
</wscn:ActiveJobs>
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
<td><p><a href="getactivejobsresponse.md" data-raw-source="[&lt;strong&gt;GetActiveJobsResponse&lt;/strong&gt;](getactivejobsresponse.md)"><strong>GetActiveJobsResponse</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobtable.md" data-raw-source="[&lt;strong&gt;JobTable&lt;/strong&gt;](jobtable.md)"><strong>JobTable</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ActiveJobs** element contains all jobs that have not yet completed processing. The state of active jobs could be scanning, pending, or stopped. **ActiveJobs** is empty when there are no currently active jobs.

A client can ask for the list of active jobs through the [**GetActiveJobsRequest**](getactivejobsrequest.md) operation. The WSD Scan Service returns the list in a [**GetActiveJobsResponse**](getactivejobsresponse.md) operation element.

## See also


[**GetActiveJobsRequest**](getactivejobsrequest.md)

[**GetActiveJobsResponse**](getactivejobsresponse.md)

[**Job**](job.md)

[**JobSummary**](jobsummary.md)

[**JobTable**](jobtable.md)

 

 






