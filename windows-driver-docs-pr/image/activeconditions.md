---
title: ActiveConditions element
description: The required ActiveConditions element is a collection of all of the currently active conditions or errors on the scan device.
ms.assetid: e66196af-d794-4ffe-99e5-c0f8ea4ffe74
keywords: ["ActiveConditions element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ActiveConditions
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ActiveConditions element


The required **ActiveConditions** element is a collection of all of the currently active conditions or errors on the scan device.

Usage
-----

``` syntax
<wscn:ActiveConditions>
  child elements
</wscn:ActiveConditions>
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
<td><p>[<strong>DeviceCondition</strong>](devicecondition.md)</p></td>
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
<td><p>[<strong>ScannerStatus</strong>](scannerstatus.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ActiveConditions** element is a list of [**DeviceCondition**](devicecondition.md) elements that describe all of the currently active conditions or errors in the device. Device conditions can vary in severity from informational to critical.

## <span id="see_also"></span>See also


[**DeviceCondition**](devicecondition.md)

[**ScannerStatus**](scannerstatus.md)

 

 






