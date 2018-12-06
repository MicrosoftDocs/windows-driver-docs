---
title: JobCompletedTime element
description: The optional JobCompletedTime element specifies the time at which the scan job was completed.
ms.assetid: f29449bd-c618-400f-b37c-3df7d955936b
keywords: ["JobCompletedTime element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobCompletedTime
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobCompletedTime element


The optional **JobCompletedTime** element specifies the time at which the scan job was completed.

Usage
-----

```xml
<wscn:JobCompletedTime>
  text
</wscn:JobCompletedTime>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid value for the dateTime type. For more information about dateTime, see XML Schema Part 2: Datatypes Second Edition.**dateTimedateTime**

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
</tbody>
</table>

Remarks
-------

A scan job is *complete* when all processing has completed, either because scanning and document transfer completed successfully or because a fatal error was encountered.

The specified time refers to the internal clock of the scan device and does not need to be a real time clock.

## See also


[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)

 

 






