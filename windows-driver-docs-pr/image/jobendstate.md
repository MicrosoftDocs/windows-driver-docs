---
title: JobEndState element
description: The required JobEndState element describes the final state of the current scan job.
ms.assetid: c69b5988-ca0d-441f-9b65-e5692a17ccb3
keywords: ["JobEndState element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobEndState
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobEndState element


The required **JobEndState** element describes the final state of the current scan job.

Usage
-----

```xml
<wscn:JobEndState>
  child elements
</wscn:JobEndState>
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
<td><p><a href="jobcompletedstate.md" data-raw-source="[&lt;strong&gt;JobCompletedState&lt;/strong&gt;](jobcompletedstate.md)"><strong>JobCompletedState</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobcompletedstatereasons.md" data-raw-source="[&lt;strong&gt;JobCompletedStateReasons&lt;/strong&gt;](jobcompletedstatereasons.md)"><strong>JobCompletedStateReasons</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="jobcompletedtime.md" data-raw-source="[&lt;strong&gt;JobCompletedTime&lt;/strong&gt;](jobcompletedtime.md)"><strong>JobCompletedTime</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobid.md" data-raw-source="[&lt;strong&gt;JobId&lt;/strong&gt;](jobid.md)"><strong>JobId</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="jobname.md" data-raw-source="[&lt;strong&gt;JobName&lt;/strong&gt;](jobname.md)"><strong>JobName</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="joboriginatingusername.md" data-raw-source="[&lt;strong&gt;JobOriginatingUserName&lt;/strong&gt;](joboriginatingusername.md)"><strong>JobOriginatingUserName</strong></a></p></td>
</tr>
<tr class="odd">
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
<td><p><a href="jobendstateevent.md" data-raw-source="[&lt;strong&gt;JobEndStateEvent&lt;/strong&gt;](jobendstateevent.md)"><strong>JobEndStateEvent</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobEndState** element contains child elements that describe various aspects about the end state of a scan job. The WSD Scan Service sends a **JobEndState** element to a client through the [**JobEndStateEvent**](jobendstateevent.md) element.

## See also


[**JobCompletedState**](jobcompletedstate.md)

[**JobCompletedStateReasons**](jobcompletedstatereasons.md)

[**JobCompletedTime**](jobcompletedtime.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobId**](jobid.md)

[**JobName**](jobname.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**ScansCompleted**](scanscompleted.md)

 

 






