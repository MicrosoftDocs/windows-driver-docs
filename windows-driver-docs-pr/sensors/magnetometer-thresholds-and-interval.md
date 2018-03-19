---
title: Magnetometer thresholds and interval
description: This topic provides information about the magnetometer thresholds and interval.
ms.assetid: F245AD4C-F63C-48A7-9AEB-7414047E0627
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Magnetometer thresholds and interval


This topic provides information about the magnetometer thresholds and interval.

The following table shows the default thresholds for the magnetometer. The default interval for the magnetometer is 10 Hz. For more information about the types shown in the type column, see [MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

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
<th>Property key</th>
<th>Type</th>
<th>Required/Optional</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_SensorData_MagneticFieldStrengthX_Microteslas</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>5.0f</p></td>
<td><p>The x-axis magnetic field in microteslas.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_MagneticFieldStrengthY_Microteslas</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>5.0f</p></td>
<td><p>The y-axis magnetic field in microteslas.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_MagneticFieldStrengthZ_Microteslas</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>5.0f</p></td>
<td><p>The z-axis magnetic field in microteslas.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






