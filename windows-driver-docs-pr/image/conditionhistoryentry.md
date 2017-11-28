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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ConditionHistoryEntry%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





