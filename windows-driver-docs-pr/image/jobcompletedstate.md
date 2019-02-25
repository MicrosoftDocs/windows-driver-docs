---
title: JobCompletedState element
description: The required JobCompletedState element specifies a job's final job state.
ms.assetid: 41dc029b-2315-465a-8490-1f4e50db0188
keywords: ["JobCompletedState element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobCompletedState
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobCompletedState element


The required **JobCompletedState** element specifies a job's final job state.

Usage
-----

```xml
<wscn:JobCompletedState>
  text
</wscn:JobCompletedState>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following values from the [**JobState**](jobstate.md) element:

-   Aborted
-   Canceled
-   Completed
-   Terminating

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
</tbody>
</table>

Remarks
-------

The WSD Scan Service sends a **JobCompletedState** element to the client within the [**JobEndStateEvent**](jobendstateevent.md) event element.

## See also


[**JobEndState**](jobendstate.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobState**](jobstate.md)

 

 






