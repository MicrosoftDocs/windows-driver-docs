---
title: Time element
description: The required Time element specifies the time at which a condition occurred.
ms.assetid: 1a10f6b4-1fcd-4697-9eb4-d58cca9c4a23
keywords: ["Time element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Time
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Time element


The required **Time** element specifies the time at which a condition occurred.

Usage
-----

```xml
<wscn:Time>
  text
</wscn:Time>
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
<tr class="even">
<td><p><a href="devicecondition.md" data-raw-source="[&lt;strong&gt;DeviceCondition&lt;/strong&gt;](devicecondition.md)"><strong>DeviceCondition</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The specified **Time** is according to the internal clock of the scanner.

## See also


[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**DeviceCondition**](devicecondition.md)

 

 






