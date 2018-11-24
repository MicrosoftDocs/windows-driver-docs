---
title: ClearTime element
description: The required ClearTime element specifies the time at which a condition was cleared.
ms.assetid: 9b5fe054-f3fa-402a-8337-8fd181679080
keywords: ["ClearTime element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ClearTime
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ClearTime element


The required **ClearTime** element specifies the time at which a condition was cleared.

Usage
-----

```xml
<wscn:ClearTime>
  text
</wscn:ClearTime>
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
<td><p><a href="conditionhistoryentry.md" data-raw-source="[&lt;strong&gt;ConditionHistoryEntry&lt;/strong&gt;](conditionhistoryentry.md)"><strong>ConditionHistoryEntry</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The specified time is according to the internal clock of the scanner.

## See also


[**ConditionHistoryEntry**](conditionhistoryentry.md)

 

 






