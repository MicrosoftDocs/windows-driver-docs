---
title: DeviceCondition element
description: The optional DeviceCondition element provides details about one of the scanner's currently active conditions.
ms.assetid: 5e68462f-afa9-40d4-843a-7d15fb7c98e3
keywords: ["DeviceCondition element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DeviceCondition wscn Id "..."
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DeviceCondition element


The optional **DeviceCondition** element provides details about one of the scanner's currently active conditions.

Usage
-----

```xml
<wscn:DeviceCondition wscn:Id="..."
  Id = "xs:string">
  child elements
</wscn:DeviceCondition wscn:Id="...">
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
<td><p><a href="component.md" data-raw-source="[&lt;strong&gt;Component&lt;/strong&gt;](component.md)"><strong>Component</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="name-element-for-devicecondition-and-conditionhistoryentry.md" data-raw-source="[&lt;strong&gt;Name Elementfor DeviceCondition and ConditionHistoryEntry&lt;/strong&gt;](name-element-for-devicecondition-and-conditionhistoryentry.md)"><strong>Name Elementfor DeviceCondition and ConditionHistoryEntry</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="severity.md" data-raw-source="[&lt;strong&gt;Severity&lt;/strong&gt;](severity.md)"><strong>Severity</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="time.md" data-raw-source="[&lt;strong&gt;Time&lt;/strong&gt;](time.md)"><strong>Time</strong></a></p></td>
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
<td><p><a href="activeconditions.md" data-raw-source="[&lt;strong&gt;ActiveConditions&lt;/strong&gt;](activeconditions.md)"><strong>ActiveConditions</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service specifies a unique identifier in the **Id** attribute for this **DeviceCondition** element. The client can use **Id**, along with the value of the [**Time**](time.md) element, to determine if an error condition is new or has gone away. The WSD Scan Service must not reuse the identifier for as long as possible. This delay ensures that clients can accurately keep track of individual **DeviceCondition** elements.

The WSD Scan Service informs a client about changes to the scanner's status by sending a [**ScannerStatusConditionEvent**](scannerstatusconditionevent.md) event. A client can directly query the scanner's state by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

## See also


[**ActiveConditions**](activeconditions.md)

[**Component**](component.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Name Elementfor DeviceCondition and ConditionHistoryEntry**](name-element-for-devicecondition-and-conditionhistoryentry.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)

[**Severity**](severity.md)

[**Time**](time.md)

 

 






