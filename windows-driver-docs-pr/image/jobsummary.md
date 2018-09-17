---
title: JobSummary element
description: The optional JobSummary element contains a summary about a scan job.
ms.assetid: db81cad5-d157-403c-b3a4-1e5f91f858da
keywords: ["JobSummary element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobSummary
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# JobSummary element


The optional **JobSummary** element contains a summary about a scan job.

Usage
-----

``` syntax
<wscn:JobSummary>
  child elements
</wscn:JobSummary>
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
<td><p>[<strong>JobId</strong>](jobid.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobName</strong>](jobname.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobOriginatingUserName</strong>](joboriginatingusername.md)</p></td>
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
<td><p>[<strong>ActiveJobs</strong>](activejobs.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobHistory</strong>](jobhistory.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the parent element of the **JobSummary** element is [**ActiveJobs**](activejobs.md), **JobSummary** contains a summary of information about one job that is currently active within the scan device.

If the parent element is [**JobHistory**](jobhistory.md), **JobSummary** contains a summary of information about a single, recently completed job within the scan device.

## <span id="see_also"></span>See also


[**ActiveJobs**](activejobs.md)

[**JobHistory**](jobhistory.md)

[**JobId**](jobid.md)

[**JobName**](jobname.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**JobState**](jobstate.md)

[**JobStateReasons**](jobstatereasons.md)

[**ScansCompleted**](scanscompleted.md)

 

 






