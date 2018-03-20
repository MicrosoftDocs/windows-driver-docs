---
title: Accelerometer thresholds and interval
description: This topic provides information about the accelerometer thresholds and interval.
ms.assetid: 7BB8B087-6CE5-4BD2-9286-350AE607B1D7
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Accelerometer thresholds and interval


This topic provides information about the accelerometer thresholds and interval.

The following table shows the default thresholds for the accelerometer. For more information about the types shown in the type column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Property key</strong></th>
<th><strong>Type</strong></th>
<th><strong>Required/Optional</strong></th>
<th><strong>Value</strong></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_SensorData_AccelerationX_Gs</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>0.1f</p></td>
<td><p>The x-axis acceleration in g’s.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_AccelerationY_Gs</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>0.1f</p></td>
<td><p>The y-axis acceleration in g’s.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_AccelerationZ_Gs</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>0.1f</p></td>
<td><p>The z-axis acceleration in g’s.</p></td>
</tr>
</tbody>
</table>

 

The default interval for the accelerometer is 50 Hz.

## <span id="related_topics"></span>Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






