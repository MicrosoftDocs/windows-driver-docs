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
<td><p>[<strong>JobCompletedState</strong>](jobcompletedstate.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobCompletedStateReasons</strong>](jobcompletedstatereasons.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobCompletedTime</strong>](jobcompletedtime.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobId</strong>](jobid.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobName</strong>](jobname.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobOriginatingUserName</strong>](joboriginatingusername.md)</p></td>
</tr>
<tr class="odd">
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
<td><p>[<strong>JobEndStateEvent</strong>](jobendstateevent.md)</p></td>
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

 

 






