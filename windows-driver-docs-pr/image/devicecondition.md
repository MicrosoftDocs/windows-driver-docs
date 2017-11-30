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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DeviceCondition%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





