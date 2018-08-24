---
title: ConditionHistoryEntry element
description: The required ConditionHistoryEntry element provides details about one of the past conditions on the scanner.
ms.assetid: 2a5d52c2-6389-4afe-be6c-4645d62ccda0
keywords: ["ConditionHistoryEntry element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ConditionHistoryEntry wscn Id "..."
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ConditionHistoryEntry element


The required **ConditionHistoryEntry** element provides details about one of the past conditions on the scanner.

Usage
-----

``` syntax
<wscn:ConditionHistoryEntry wscn:Id="..."
  Id = "xs:string">
  child elements
</wscn:ConditionHistoryEntry wscn:Id="...">
```

Attributes
----------

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong><strong>Id</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Required. An integer from 1 through 2147483648.</p></td>
</tr>
</tbody>
</table>

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
<td><p>[<strong>ClearTime</strong>](cleartime.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Component</strong>](component.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>Name forParents DeviceCondition and ConditionHistoryEntry</strong>](name-element-for-devicecondition-and-conditionhistoryentry.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Severity</strong>](severity.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>Time</strong>](time.md)</p></td>
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
<td><p>[<strong>ConditionHistory</strong>](conditionhistory.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service specifies a unique identifier in the **Id** attribute for this **ConditionHistoryEntry** element. The client can use **Id**, along with the value of the [**Time**](time.md) element, to determine if an error condition is new or has gone away. The WSD Scan Service must not reuse the identifier for as long as possible. This delay ensures that clients can accurately keep track of individual **ConditionHistoryEntry** elements.

You cannot extend the allowed values for **Id**.

## <span id="see_also"></span>See also


[**ClearTime**](cleartime.md)

[**Component**](component.md)

[**ConditionHistory**](conditionhistory.md)

[**DeviceCondition**](devicecondition.md)

[**Name forParents DeviceCondition and ConditionHistoryEntry**](name-element-for-devicecondition-and-conditionhistoryentry.md)

[**Severity**](severity.md)

[**Time**](time.md)

 

 






