---
title: Magnetometer data fields
description: This topic provides information about the data fields that are specific to the magnetometer.
ms.assetid: 5DA5566A-FECA-47ED-8338-686A548687CC
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Magnetometer data fields


This topic provides information about the data fields that are specific to the magnetometer.

The following table shows the data fields. For more information about the types shown in the type column, see [MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

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
<td><p>PKEY_SensorData_MagneticFieldStrengthX_Microteslas</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>The x-axis magnetic field in microteslas. This is calibrated to account for the magnetic effects of the device chassis.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_MagneticFieldStrengthY_Microteslas</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>The y-axis magnetic field in microteslas. This is calibrated to account for the magnetic effects of the device chassis.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_MagneticFieldStrengthZ_Microteslas</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>The z-axis magnetic field in microteslas. This is calibrated to account for the magnetic effects of the device chassis.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_MagnetometerAccuracy</p></td>
<td><p>VT_UI4</p></td>
<td><p>Required</p></td>
<td><p>The accuracy of the magnetometer sensor. For more information about valid values, see [<strong>MAGNETOMETER_ACCURACY</strong>](https://msdn.microsoft.com/library/windows/hardware/dn957070).</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[**MAGNETOMETER\_ACCURACY**](https://msdn.microsoft.com/library/windows/hardware/dn957070)

[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






