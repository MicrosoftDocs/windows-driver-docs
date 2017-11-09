---
title: Name Element for DeviceCondition and ConditionHistoryEntry element
description: The required Name element names the current error condition that is specified in a DeviceCondition or ConditionHistoryEntry element.
MS-HAID:
- 'wsdss\_status\_37e44f99-d3d2-41dc-b055-f2fcb0406866.xml'
- 'image.name\_element\_for\_devicecondition\_and\_conditionhistoryentry'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1ac530ed-dc31-4af0-a89b-0860a36bbfeb
keywords: ["Name Element for DeviceCondition and ConditionHistoryEntry element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Name
api_type:
- Schema
---

# Name Element for DeviceCondition and ConditionHistoryEntry element


The required **Name** element names the current error condition that is specified in a [**DeviceCondition**](devicecondition.md) or [**ConditionHistoryEntry**](conditionhistoryentry.md) element.

Usage
-----

``` syntax
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
<td><p>[<strong>ConditionHistoryEntry</strong>](conditionhistoryentry.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DeviceCondition</strong>](devicecondition.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

Some error names are valid for only certain [**Component**](component.md) elements.

You can both extend and subset the allowed values for this element.

## <span id="see_also"></span>See also


[**Component**](component.md)

[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**DeviceCondition**](devicecondition.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Name%20Element%20for%20DeviceCondition%20and%20ConditionHistoryEntry%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





