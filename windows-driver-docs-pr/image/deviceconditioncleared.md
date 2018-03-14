---
title: DeviceConditionCleared element
description: The required DeviceConditionCleared element contains information about a previously reported DeviceCondition condition that has been cleared.
ms.assetid: f4ed3d25-cee0-4532-84aa-d1cdd144ce2a
keywords: ["DeviceConditionCleared element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DeviceConditionCleared
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DeviceConditionCleared element


The required **DeviceConditionCleared** element contains information about a previously reported [**DeviceCondition**](devicecondition.md) condition that has been cleared.

Usage
-----

``` syntax
<wscn:DeviceConditionCleared>
  child elements
</wscn:DeviceConditionCleared>
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
<td><p>[<strong>ConditionClearTime</strong>](conditioncleartime.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ConditionId</strong>](conditionid.md)</p></td>
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
<td><p>[<strong>ScannerStatusConditionEvent</strong>](scannerstatusconditionevent.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **DeviceConditionCleared** element contains the [**ConditionId**](conditionid.md) and [**ConditionClearTime**](conditioncleartime.md) elements, which specify the condition identifier and time at which the condition was cleared, respectively. The WSD Scan Service sends the **DeviceConditionCleared** element to a client in a [**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md) event element.

## <span id="see_also"></span>See also


[**ConditionClearTime**](conditioncleartime.md)

[**ConditionId**](conditionid.md)

[**DeviceCondition**](devicecondition.md)

[**DeviceConditionCleared**](deviceconditioncleared.md)

[**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)

 

 






