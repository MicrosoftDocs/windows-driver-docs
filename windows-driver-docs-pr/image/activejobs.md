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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ActiveJobs element


The required **ActiveJobs** element contains a list of all currently active scan jobs.

Usage
-----

``` syntax
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
<td><p>[<strong>Job</strong>](job.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobSummary</strong>](jobsummary.md)</p></td>
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
<td><p>[<strong>GetActiveJobsResponse</strong>](getactivejobsresponse.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobTable</strong>](jobtable.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ActiveJobs** element contains all jobs that have not yet completed processing. The state of active jobs could be scanning, pending, or stopped. **ActiveJobs** is empty when there are no currently active jobs.

A client can ask for the list of active jobs through the [**GetActiveJobsRequest**](getactivejobsrequest.md) operation. The WSD Scan Service returns the list in a [**GetActiveJobsResponse**](getactivejobsresponse.md) operation element.

## <span id="see_also"></span>See also


[**GetActiveJobsRequest**](getactivejobsrequest.md)

[**GetActiveJobsResponse**](getactivejobsresponse.md)

[**Job**](job.md)

[**JobSummary**](jobsummary.md)

[**JobTable**](jobtable.md)

 

 






