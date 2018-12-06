---
title: JobState element
description: The required JobState element specifies the current state of the job.
ms.assetid: 7198feea-ce6c-4827-a3b4-c248c6f62e37
keywords: ["JobState element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobState
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobState element


The required **JobState** element specifies the current state of the job.

Usage
-----

```xml
<wscn:JobState>
  text
</wscn:JobState>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>Aborted</p></td>
<td><p>The system aborted the job.</p></td>
</tr>
<tr class="even">
<td><p><span id="Canceled"></span><span id="canceled"></span><span id="CANCELED"></span>Canceled</p></td>
<td><p>The job was canceled by a client that is using the CancelJobRequest operation or by means outside the scope of the WSD Scan Service.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>Completed</p></td>
<td><p>The job is finished processing and all of the image data has been sent to the client.</p></td>
</tr>
<tr class="even">
<td><p><span id="Creating"></span><span id="creating"></span><span id="CREATING"></span>Creating</p></td>
<td><p>The job is being initialized.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Held"></span><span id="held"></span><span id="HELD"></span>Held</p></td>
<td><p>The job is waiting to be processed but is unavailable for scheduling. The job can reach this state only by methods outside the scope of the WSD Scan Service.</p></td>
</tr>
<tr class="even">
<td><p><span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>Pending</p></td>
<td><p>The job has been initialized and is waiting to be processed.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Processing"></span><span id="processing"></span><span id="PROCESSING"></span>Processing</p></td>
<td><p>The job data is being digitized, transformed, or transferred.</p></td>
</tr>
<tr class="even">
<td><p><span id="Started"></span><span id="started"></span><span id="STARTED"></span>Started</p></td>
<td><p>The scan device has started processing the job. This state is a transient state and will typically be seen only with a JobStatusEvent event.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Terminating"></span><span id="terminating"></span><span id="TERMINATING"></span>Terminating</p></td>
<td><p>The job was canceled by either a client-initiated CancelJobRequest operation or aborted by means outside the scope of the WSD Scan Service.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="jobstatus.md" data-raw-source="[&lt;strong&gt;JobStatus&lt;/strong&gt;](jobstatus.md)"><strong>JobStatus</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobsummary.md" data-raw-source="[&lt;strong&gt;JobSummary&lt;/strong&gt;](jobsummary.md)"><strong>JobSummary</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

When the **JobState** element is contained in a [**JobEndStateEvent**](jobendstateevent.md) event or [**JobHistory**](jobhistory2.md) element, **JobState** represents the completed state of a job. Otherwise, **JobState** specifies the current state of the job.

You can both extend and subset the allowed values for this element.

## See also


[**CancelJobRequest**](canceljobrequest.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobHistory**](jobhistory2.md)

[**JobStatus**](jobstatus.md)

[**JobStatusEvent**](jobstatusevent.md)

[**JobSummary**](jobsummary.md)

 

 






