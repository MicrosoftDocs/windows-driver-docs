---
title: JobStateReasons element
description: The required JobStateReasons element contains all additional information about why a job is in its current state.
ms.assetid: 52d6519e-2392-4fa4-bac0-f1bf60eccc99
keywords: ["JobStateReasons element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobStateReasons
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobStateReasons element


The required **JobStateReasons** element contains all additional information about why a job is in its current state.

Usage
-----

```xml
<wscn:JobStateReasons>
  child elements
</wscn:JobStateReasons>
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
<td><p><a href="jobstatereason.md" data-raw-source="[&lt;strong&gt;JobStateReason&lt;/strong&gt;](jobstatereason.md)"><strong>JobStateReason</strong></a></p></td>
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
<td><p><a href="jobstatus.md" data-raw-source="[&lt;strong&gt;JobStatus&lt;/strong&gt;](jobstatus.md)"><strong>JobStatus</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobsummary.md" data-raw-source="[&lt;strong&gt;JobSummary&lt;/strong&gt;](jobsummary.md)"><strong>JobSummary</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobStateReasons** element contains a list of [**JobStateReason**](jobstatereason.md) elements, each of which specifies one reason why a job is in its current state.

## See also


[**JobStateReason**](jobstatereason.md)

[**JobStatus**](jobstatus.md)

[**JobSummary**](jobsummary.md)

 

 






