---
title: Geomagnetic Orientation
description: This topic provides information about the data fields that are specific to the geomagnetic orientation sensor.
ms.assetid: C164E5A9-A664-4EE5-91CE-918233DFFB6D
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Geomagnetic orientation


This topic provides information about the data fields that are specific to the geomagnetic orientation sensor.

The following table shows the data fields. For more information about the types shown in the type column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

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
<th>Description/Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_SensorData_QuaternionW</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>Real coefficient (as opposed to the imaginary portion of the complex number).</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_QuaternionX</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>X-component of rotational axis vector.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_QuaternionY</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>Y-component of rotational axis vector.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_QuaternionZ</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>Z-component of rotational axis vector.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_DeclinationAngle_Degrees</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>Declination angle. If not supported, the class extension will compute this value.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_RotationAngle_Degrees</p></td>
<td><p>VT_R4</p></td>
<td><p>Required for Windows 10 Mobile</p>
<p>Optional for Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)</p></td>
<td><p>Rotation angle, in degrees.</p>
<p>Drivers that expose a Device Orientation sensor should use this property key for threshold keys.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






