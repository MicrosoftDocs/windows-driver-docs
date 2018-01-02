---
title: Severity element
description: The required Severity element specifies the severity level of the current DeviceCondition or ConditionHistoryEntry element.
ms.assetid: 51c08a50-0c2b-40d9-883e-32460c2024ad
keywords: ["Severity element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Severity
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Severity element


The required **Severity** element specifies the severity level of the current [**DeviceCondition**](devicecondition.md) or [**ConditionHistoryEntry**](conditionhistoryentry.md) element.

Usage
-----

``` syntax
<wscn:Severity>
  text
</wscn:Severity>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="Informational"></span><span id="informational"></span><span id="INFORMATIONAL"></span>Informational</p></td>
<td><p>This condition is purely for user information and has no noticeable effect on the image acquisition process.</p></td>
</tr>
<tr class="even">
<td><p><span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>Warning</p></td>
<td><p>This condition is not currently affecting processing, but the condition might become Critical if it is not attended to.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>Critical</p></td>
<td><p>The device cannot continue processing until this condition is resolved.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>[<strong>ConditionHistoryEntry</strong>](conditionhistoryentry.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DeviceCondition</strong>](devicecondition.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service determines the **Severity** level that is assigned to each error condition.

You can both extend and subset the allowed values for this element.

## <span id="see_also"></span>See also


[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**DeviceCondition**](devicecondition.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Severity%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





