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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# DeviceCondition element


The optional **DeviceCondition** element provides details about one of the scanner's currently active conditions.

Usage
-----

``` syntax
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
<td><p>[<strong>Component</strong>](component.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Name Elementfor DeviceCondition and ConditionHistoryEntry</strong>](name-element-for-devicecondition-and-conditionhistoryentry.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>Severity</strong>](severity.md)</p></td>
</tr>
<tr class="even">
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
<td><p>[<strong>ActiveConditions</strong>](activeconditions.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service specifies a unique identifier in the **Id** attribute for this **DeviceCondition** element. The client can use **Id**, along with the value of the [**Time**](time.md) element, to determine if an error condition is new or has gone away. The WSD Scan Service must not reuse the identifier for as long as possible. This delay ensures that clients can accurately keep track of individual **DeviceCondition** elements.

The WSD Scan Service informs a client about changes to the scanner's status by sending a [**ScannerStatusConditionEvent**](scannerstatusconditionevent.md) event. A client can directly query the scanner's state by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

## <span id="see_also"></span>See also


[**ActiveConditions**](activeconditions.md)

[**Component**](component.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Name Elementfor DeviceCondition and ConditionHistoryEntry**](name-element-for-devicecondition-and-conditionhistoryentry.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)

[**Severity**](severity.md)

[**Time**](time.md)

 

 






