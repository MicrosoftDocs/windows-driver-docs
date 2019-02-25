---
title: JobStatus element
description: The required JobStatus element contains all information about the status of the current scan job.
ms.assetid: e3eb2cc7-70a4-4ae0-8569-4a91f2b42228
keywords: ["JobStatus element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobStatus
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobStatus element


The required **JobStatus** element contains all information about the status of the current scan job.

Usage
-----

```xml
<wscn:JobStatus>
  child elements
</wscn:JobStatus>
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
<td><p><a href="jobcompletedtime.md" data-raw-source="[&lt;strong&gt;JobCompletedTime&lt;/strong&gt;](jobcompletedtime.md)"><strong>JobCompletedTime</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobcreatedtime.md" data-raw-source="[&lt;strong&gt;JobCreatedTime&lt;/strong&gt;](jobcreatedtime.md)"><strong>JobCreatedTime</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="jobid.md" data-raw-source="[&lt;strong&gt;JobId&lt;/strong&gt;](jobid.md)"><strong>JobId</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobstate.md" data-raw-source="[&lt;strong&gt;JobState&lt;/strong&gt;](jobstate.md)"><strong>JobState</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="jobstatereasons.md" data-raw-source="[&lt;strong&gt;JobStateReasons&lt;/strong&gt;](jobstatereasons.md)"><strong>JobStateReasons</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="scanscompleted.md" data-raw-source="[&lt;strong&gt;ScansCompleted&lt;/strong&gt;](scanscompleted.md)"><strong>ScansCompleted</strong></a></p></td>
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
<td><p><a href="job.md" data-raw-source="[&lt;strong&gt;Job&lt;/strong&gt;](job.md)"><strong>Job</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

**JobStatus** child elements are maintained through automata. The WSD Scan Service should update **JobStatus** elements accordingly as it processes a job. A client operation, such as [**CancelJobRequest**](canceljobrequest.md), can indirectly affect job status.

The WSD Scan Service notifies a client about changes to a job's status through a [**JobStatusEvent**](jobstatusevent.md) event element. The WSD Scan Service should generate a **JobStatusEvent** element for every change to all **JobStatus** child elements.

A client can query for job status through the [**GetJobElementsRequest**](getjobelementsrequest.md) operation.

## See also


[**CancelJobRequest**](canceljobrequest.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**Job**](job.md)

[**JobCompletedTime**](jobcompletedtime.md)

[**JobCreatedTime**](jobcreatedtime.md)

[**JobId**](jobid.md)

[**JobState**](jobstate.md)

[**JobStateReasons**](jobstatereasons.md)

[**JobStatusEvent**](jobstatusevent.md)

[**ScansCompleted**](scanscompleted.md)

 

 






