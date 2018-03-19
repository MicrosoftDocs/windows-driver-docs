---
title: Activity detection sensor data fields
description: This topic provides information about the data fields that are specific to the activity detection sensor.
ms.assetid: D123C082-9E20-44C2-A9F2-DAC0E09F61B7
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Activity detection sensor data fields


This topic provides information about the data fields that are specific to the activity detection sensor.

The following table shows the data fields. For more information about the data types shown in the **Type** column, see [MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Property key</th>
<th>Type</th>
<th>Required/Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_SensorData_CurrentActivityState</p></td>
<td><p>VT_UI4</p></td>
<td><p>Required</p></td>
<td><p>An indication of the current activity state, expressed as a value of type [<strong>ACTIVITY_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn957014).</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_CurrentActivityStateConfidence_Percentage</p></td>
<td><p>VT_UI2</p></td>
<td><p>Required</p></td>
<td><p>Confidence level of the sensor in indicating the current activity state.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_SubscribedActivityStates</p></td>
<td><p>VT_UI4</p></td>
<td><p>Required</p>
<p>Required</p></td>
<td><p>An indication of the subscribed activity state, expressed as a value of type [<strong>ACTIVITY_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn957014).</p>
<p></p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_ActivityStream</p></td>
<td><p>VT_BOOL</p></td>
<td><p>Required</p></td>
<td><p>Boolean value that is set to TRUE, if an activity stream is available.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_ConfidenceThreshold_Percentage</p></td>
<td><p>VT_UI2</p></td>
<td><p>Required</p></td>
<td><p>A threshold value for the sensor's confidence level.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[**ACTIVITY\_STATE**](https://msdn.microsoft.com/library/windows/hardware/dn957014)

[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






