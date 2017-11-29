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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# JobState element


The required **JobState** element specifies the current state of the job.

Usage
-----

``` syntax
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
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobSummary</strong>](jobsummary.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

When the **JobState** element is contained in a [**JobEndStateEvent**](jobendstateevent.md) event or [**JobHistory**](jobhistory2.md) element, **JobState** represents the completed state of a job. Otherwise, **JobState** specifies the current state of the job.

You can both extend and subset the allowed values for this element.

## <span id="see_also"></span>See also


[**CancelJobRequest**](canceljobrequest.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobHistory**](jobhistory2.md)

[**JobStatus**](jobstatus.md)

[**JobStatusEvent**](jobstatusevent.md)

[**JobSummary**](jobsummary.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobState%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





