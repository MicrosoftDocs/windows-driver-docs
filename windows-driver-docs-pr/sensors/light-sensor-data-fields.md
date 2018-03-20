---
title: Light sensor data fields
description: This topic provides information about the data fields that are specific to the light sensor.
ms.assetid: 96572A6A-CACC-4B79-B63C-5554C07F7C83
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






