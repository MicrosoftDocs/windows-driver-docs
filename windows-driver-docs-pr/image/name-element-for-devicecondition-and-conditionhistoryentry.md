---
title: Name Element for DeviceCondition and ConditionHistoryEntry element
description: The required Name element names the current error condition that is specified in a DeviceCondition or ConditionHistoryEntry element.
ms.assetid: 1ac530ed-dc31-4af0-a89b-0860a36bbfeb
keywords: ["Name Element for DeviceCondition and ConditionHistoryEntry element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Name
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Name Element for DeviceCondition and ConditionHistoryEntry element


The required **Name** element names the current error condition that is specified in a [**DeviceCondition**](devicecondition.md) or [**ConditionHistoryEntry**](conditionhistoryentry.md) element.

Usage
-----

```xml
<wscn:Name>
  text
</wscn:Name>
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
<td><p><span id="Calibrating"></span><span id="calibrating"></span><span id="CALIBRATING"></span>Calibrating</p></td>
<td><p>The scan device is calibrating its internal components to prepare to acquire images.</p></td>
</tr>
<tr class="even">
<td><p><span id="CoverOpen"></span><span id="coveropen"></span><span id="COVEROPEN"></span>CoverOpen</p></td>
<td><p>One of more covers on the scan device are open.</p></td>
</tr>
<tr class="odd">
<td><p><span id="InputTrayEmpty"></span><span id="inputtrayempty"></span><span id="INPUTTRAYEMPTY"></span>InputTrayEmpty</p></td>
<td><p>The automatic document feeder (ADF) input has no media.</p></td>
</tr>
<tr class="even">
<td><p><span id="InterlockOpen"></span><span id="interlockopen"></span><span id="INTERLOCKOPEN"></span>InterlockOpen</p></td>
<td><p>The interlock is open.</p></td>
</tr>
<tr class="odd">
<td><p><span id="InternalStorageFull"></span><span id="internalstoragefull"></span><span id="INTERNALSTORAGEFULL"></span>InternalStorageFull</p></td>
<td><p>The internal storage component that is currently being written to is full.</p></td>
</tr>
<tr class="even">
<td><p><span id="LampError"></span><span id="lamperror"></span><span id="LAMPERROR"></span>LampError</p></td>
<td><p>The scanner lamp is failing and image acquisition cannot proceed.</p></td>
</tr>
<tr class="odd">
<td><p><span id="LampWarming"></span><span id="lampwarming"></span><span id="LAMPWARMING"></span>LampWarming</p></td>
<td><p>The scanner lamp is warming to prepare to acquire images.</p></td>
</tr>
<tr class="even">
<td><p><span id="MediaJam"></span><span id="mediajam"></span><span id="MEDIAJAM"></span>MediaJam</p></td>
<td><p>Media is jammed in one of the input sources, so image acquisition failed.</p></td>
</tr>
<tr class="odd">
<td><p><span id="MultipleFeedError"></span><span id="multiplefeederror"></span><span id="MULTIPLEFEEDERROR"></span>MultipleFeedError</p></td>
<td><p>The ADF was fed more than one piece of media simultaneously.</p></td>
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
<td><p><a href="conditionhistoryentry.md" data-raw-source="[&lt;strong&gt;ConditionHistoryEntry&lt;/strong&gt;](conditionhistoryentry.md)"><strong>ConditionHistoryEntry</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="devicecondition.md" data-raw-source="[&lt;strong&gt;DeviceCondition&lt;/strong&gt;](devicecondition.md)"><strong>DeviceCondition</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

Some error names are valid for only certain [**Component**](component.md) elements.

You can both extend and subset the allowed values for this element.

## See also


[**Component**](component.md)

[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**DeviceCondition**](devicecondition.md)

 

 






