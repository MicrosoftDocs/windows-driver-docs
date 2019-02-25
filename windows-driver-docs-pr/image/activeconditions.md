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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ActiveConditions element


The required **ActiveConditions** element is a collection of all of the currently active conditions or errors on the scan device.

Usage
-----

```xml
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
<td><p><a href="devicecondition.md" data-raw-source="[&lt;strong&gt;DeviceCondition&lt;/strong&gt;](devicecondition.md)"><strong>DeviceCondition</strong></a></p></td>
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
<td><p><a href="scannerstatus.md" data-raw-source="[&lt;strong&gt;ScannerStatus&lt;/strong&gt;](scannerstatus.md)"><strong>ScannerStatus</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ActiveConditions** element is a list of [**DeviceCondition**](devicecondition.md) elements that describe all of the currently active conditions or errors in the device. Device conditions can vary in severity from informational to critical.

## See also


[**DeviceCondition**](devicecondition.md)

[**ScannerStatus**](scannerstatus.md)

 

 






