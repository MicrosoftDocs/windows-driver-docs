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


[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Light%20sensor%20data%20fields%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





