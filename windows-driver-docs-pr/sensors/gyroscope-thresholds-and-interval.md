---
title: Gyroscope thresholds and interval
description: This topic provides information about the gyroscope thresholds and interval.
ms.assetid: 68B11108-CA1A-4A49-BC44-4E9FE09955A9
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Gyroscope thresholds and interval


This topic provides information about the gyroscope thresholds and interval.

The following table shows the default thresholds for the gyroscope. The default interval for the gyrometer is 10 Hz. For more information about the types shown in the type column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

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
<td><p>PKEY_SensorData_AngularVelocityX_DegreesPerSecond</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>0.1f</p></td>
<td><p>The gyrometric x-axis velocity in degrees per second.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_AngularVelocityY_DegreesPerSecond</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>0.1f</p></td>
<td><p>The gyrometric y-axis velocity in degrees per second.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_AngularVelocityZ_DegreesPerSecond</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>0.1f</p></td>
<td><p>The gyrometric z-axis velocity in degrees per second.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






