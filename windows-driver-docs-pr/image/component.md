---
title: Component element
description: The required Component element identifies the component that the current DeviceCondition or ConditionHistoryEntry element describes.
ms.assetid: 1204d8c6-40a2-4b0b-bf86-a739ae96f54a
keywords: ["Component element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Component
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Component element


The required **Component** element identifies the component that the current [**DeviceCondition**](devicecondition.md) or [**ConditionHistoryEntry**](conditionhistoryentry.md) element describes.

Usage
-----

```xml
<wscn:Component>
  text
</wscn:Component>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following values:

-   ADF
-   Film
-   MediaPath
-   Platen

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

You can both extend and subset the allowed values for this element.

## See also


[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**DeviceCondition**](devicecondition.md)

 

 






