---
title: JobHistory element
description: The required JobHistory element contains a list of JobSummary elements that describe the most recently completed jobs in the scan device.
ms.assetid: d1439e56-b2fe-4db8-b063-56537a3346c6
keywords: ["JobHistory element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobHistory
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# JobHistory element


The required **JobHistory** element contains a list of [**JobSummary**](jobsummary.md) elements that describe the most recently completed jobs in the scan device.

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
<td><p>[<strong>GetJobHistoryResponse</strong>](getjobhistoryresponse.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobHistory** element contains a [**JobSummary**](jobsummary.md) element for every job that the scanner recently completes. **JobHistory** is empty if the WSD Scan Service has no record of recently completed jobs. The Scan Service returns this list from [**GetJobHistoryResponse**](getjobhistoryresponse.md).

The amount of job history that the WSD Scan Service stores and returns is implementation-specific.

## See also


[**GetJobHistoryResponse**](getjobhistoryresponse.md)

[**JobSummary**](jobsummary.md)

 

 






