---
title: ScansCompleted element
description: The required ScansCompleted element specifies the number of images that are scanned.
ms.assetid: 71634b6b-1c61-46a0-8cde-01a975c09270
keywords: ["ScansCompleted element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScansCompleted
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScansCompleted element


The required **ScansCompleted** element specifies the number of images that are scanned.

Usage
-----

```xml
<wscn:ScansCompleted>
  text
</wscn:ScansCompleted>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. An integer value from 1 through 2147483648.

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
<td><p><a href="jobendstate.md" data-raw-source="[&lt;strong&gt;JobEndState&lt;/strong&gt;](jobendstate.md)"><strong>JobEndState</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobstatus.md" data-raw-source="[&lt;strong&gt;JobStatus&lt;/strong&gt;](jobstatus.md)"><strong>JobStatus</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="jobsummary.md" data-raw-source="[&lt;strong&gt;JobSummary&lt;/strong&gt;](jobsummary.md)"><strong>JobSummary</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

If a sheet of media is scanned multiple times, the WSD Scan Service must increment the **ScansCompleted** count every time. Each side of a media sheet is scanned in duplex mode, generating two scans in the **ScansCompleted** count.

The **ScansCompleted** count might not be known until the scanner has completed processing the job. The WSD Scan Service must update the **ScansCompleted** element when more exact information is available.

## See also


[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)

[**JobSummary**](jobsummary.md)

 

 






