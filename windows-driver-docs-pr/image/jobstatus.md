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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobStatus%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





