---
title: Light sensor data fields
description: This topic provides information about the data fields that are specific to the light sensor.
ms.assetid: 96572A6A-CACC-4B79-B63C-5554C07F7C83
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# Light sensor data fields


This topic provides information about the data fields that are specific to the light sensor.

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
<td><p>PKEY_SensorData_LightLevel_Lux</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>The illuminance level in lux.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_LightTemperature_Kelvins</p></td>
<td><p>VT_R4</p></td>
<td><p>Optional</p></td>
<td><p>The light temperature in Kelvins.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_LightChromaticityX</p></td>
<td><p>VT_R4</p></td>
<td><p>Optional</p></td>
<td><p>The x color coordinate on the CIE 1931 chromaticity diagram.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_LightChromaticityY</p></td>
<td><p>VT_R4</p></td>
<td><p>Optional</p></td>
<td><p>The y color coordinate on the CIE 1931 chromaticity diagram.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_IsValid</p></td>
<td><p>VT_BOOL</p></td>
<td><p>Optional</p></td>
<td><p>This value must be set to FALSE when the ambient light sensor cannot currently return any valid sample. For example, this value may be set to FALSE when the sensor field of view is obstructed (such as when an object, or the user hand is in front of the sensor). This value should be set to TRUE when the ambient light sensor is able to accurately measure the ambient light. Proper hardware design should try to minimize the time and scenarios requiring this value to be set to FALSE as such scenario prevents the system from properly controlling brightness. On an ideal system, this value is always set to TRUE.</p></td>
</tr>
</tbody>
</table>

 

## Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






