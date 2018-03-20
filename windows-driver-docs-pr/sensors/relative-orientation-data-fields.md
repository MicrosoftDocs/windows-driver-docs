---
title: Relative orientation sensor data fields
description: This topic provides information about the data fields that are specific to the relative orientation sensor.
ms.assetid: A48B75DD-5424-48CC-AC8B-251874414FCE
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Relative orientation sensor data fields


This topic provides information about the data fields that are specific to the relative orientation sensor.

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
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_SensorData_Timestamp</p></td>
<td><p>VT_FILETIME</p></td>
<td><p>Required</p></td>
<td><p>Timestamp for sampled data. This is required for each sample that is reported by the sensor driver.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_QuaternionW</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>Real coefficient (as opposed to the imaginary portion of the complex number).</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_QuaternionX</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>X-component of rotational axis vector.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_QuaternionY</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>X-component of rotational axis vector.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_QuaternionZ</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>X-component of rotational axis vector.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






