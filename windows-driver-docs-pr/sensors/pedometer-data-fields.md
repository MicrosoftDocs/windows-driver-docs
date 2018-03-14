---
title: Pedometer data fields
description: This topic provides information about the data fields that are specific to the pedometer.
ms.assetid: 35E52085-9727-465D-B6EF-D95974423CD5
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Pedometer data fields


This topic provides information about the data fields that are specific to the pedometer.

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
<td><p>PKEY_SensorData_PedometerStepType</p></td>
<td><p>VT_UI4</p></td>
<td><p>Required</p></td>
<td><p>The step type, expressed as a [<strong>PEDOMETER_STEP_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn957077) value.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_PedometerStepCount</p></td>
<td><p>VT_UI4</p></td>
<td><p>Required</p></td>
<td><p>The number of steps detected.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_PedometerStepDuration_Ms</p></td>
<td><p>VT_I8</p></td>
<td><p>Required</p></td>
<td><p>The duration over which the pedometer counted steps. This value is expressed in milliseconds.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_PedometerReset</p></td>
<td><p>VT_BOOL</p></td>
<td><p>Required</p></td>
<td><p>Indicates that the pedometer has been reset.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

[**PEDOMETER\_STEP\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn957077)

 

 






