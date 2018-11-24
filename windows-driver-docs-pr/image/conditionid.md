---
title: ConditionId element
description: The required ConditionId element uniquely identifies the device condition that was just cleared.
ms.assetid: 4b154fb3-625e-478d-9bb4-92fd7cae0530
keywords: ["ConditionId element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ConditionId
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ConditionId element


The required **ConditionId** element uniquely identifies the device condition that was just cleared.

Usage
-----

```xml
<wscn:ConditionId>
  text
</wscn:ConditionId>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. An integer value that is equivalent to the Id attribute of a previously reported DeviceCondition element.

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
<td><p><a href="deviceconditioncleared.md" data-raw-source="[&lt;strong&gt;DeviceConditionCleared&lt;/strong&gt;](deviceconditioncleared.md)"><strong>DeviceConditionCleared</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ConditionId** element must be the **Id** attribute of a **DeviceCondition** element that the WSD Scan Service previously reported through [**ScannerStatusConditionEvent**](scannerstatusconditionevent.md).

## See also


[**DeviceCondition**](devicecondition.md)

[**DeviceConditionCleared**](deviceconditioncleared.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)

 

 






