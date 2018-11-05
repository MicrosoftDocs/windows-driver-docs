---
title: JobCompletedStateReasons element
description: The required JobCompletedStateReasons element is a collection of all additional information about how and why a scan job completed.
ms.assetid: 678384b4-a023-4c79-a68a-4a2cc3a04a0e
keywords: ["JobCompletedStateReasons element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobCompletedStateReasons
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobCompletedStateReasons element


The required **JobCompletedStateReasons** element is a collection of all additional information about how and why a scan job completed.

Usage
-----

```xml
<wscn:JobCompletedStateReasons>
  child elements
</wscn:JobCompletedStateReasons>
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
<td><p><a href="jobendstate.md" data-raw-source="[&lt;strong&gt;JobEndState&lt;/strong&gt;](jobendstate.md)"><strong>JobEndState</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobCompletedStateReasons** element contains zero or more [**JobStateReason**](jobstatereason.md) elements, each of which contains a reason for how or why the scan job completed. The WSD Scan Service sends the **JobCompletedStateReasons** element to the client through the [**JobEndStateEvent**](jobendstateevent.md) event element.

## See also


[**JobEndState**](jobendstate.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobStateReason**](jobstatereason.md)

 

 






