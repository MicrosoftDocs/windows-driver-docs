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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# JobStatus element


The required **JobStatus** element contains all information about the status of the current scan job.

Usage
-----

``` syntax
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
<td><p>[<strong>JobCompletedTime</strong>](jobcompletedtime.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobCreatedTime</strong>](jobcreatedtime.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobId</strong>](jobid.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobState</strong>](jobstate.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobStateReasons</strong>](jobstatereasons.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScansCompleted</strong>](scanscompleted.md)</p></td>
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

Remarks
-------

**JobStatus** child elements are maintained through automata. The WSD Scan Service should update **JobStatus** elements accordingly as it processes a job. A client operation, such as [**CancelJobRequest**](canceljobrequest.md), can indirectly affect job status.

The WSD Scan Service notifies a client about changes to a job's status through a [**JobStatusEvent**](jobstatusevent.md) event element. The WSD Scan Service should generate a **JobStatusEvent** element for every change to all **JobStatus** child elements.

A client can query for job status through the [**GetJobElementsRequest**](getjobelementsrequest.md) operation.

## <span id="see_also"></span>See also


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

 

 






