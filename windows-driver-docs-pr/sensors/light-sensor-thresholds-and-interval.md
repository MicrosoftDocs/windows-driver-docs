---
title: Light sensor thresholds and interval
description: This topic provides information about the light sensor thresholds and interval.
ms.assetid: A120601A-A5CE-4778-94A9-97E71B721E9B
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Light sensor thresholds and interval


This topic provides information about the light sensor thresholds and interval.

The following table shows the driver's default thresholds for the light sensor. The default interval for the light sensor is 10 Hz. For more information about the types shown in the type column, see [MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

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
<td><p>PKEY_SensorData_LightLevel_Lux</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>0.25</p></td>
<td><p>The illuminance level in lux, expressed as a percentage value.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_LightLevel_Lux_Threshold_AbsoluteDifference</p></td>
<td><p>VT_R4</p></td>
<td><p>Optional</p></td>
<td><p>1</p></td>
<td><p>The illuminance level in lux, expressed as an absolute difference.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_LightChromaticityX</p></td>
<td><p>VT_R4</p></td>
<td><p>Optional</p></td>
<td><p>0.01</p></td>
<td><p>The CIE 1931 x color coordinate, expressed as an absolute difference.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_LightChromaticityY</p></td>
<td><p>VT_R4</p></td>
<td><p>Optional</p></td>
<td><p>0.01</p></td>
<td><p>The CIE 1931 y color coordinate, expressed as an absolute difference.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_LightTemperature_Kelvins</p></td>
<td><p>VT_R4</p></td>
<td><p>Optional</p></td>
<td><p>50</p></td>
<td><p>The light temperature in Kelvins, expressed as an absolute difference.</p></td>
</tr>
</tbody>
</table>

 

**Note**  It is very important to note that the light sensor should report new data samples *only if the LUX value changes*. This recommended reporting model ensures that the light sensor does not report new data samples repeatedly, when it is in a completely dark, zero (0) LUX environment.

 

**Note**  If the light sensor reports chromaticity or kelvins, the corresponding threshold(s) are required.

 

**Note**  The overall lux threshold will only be met if both absolute and percentage lux thresholds are met (provided that an absolute lux threshold is provided).

 

**Note**   A change in the IsValid value must be reported, regardless of light sensor data exceeding their respective thresholds.

 

**Note**  In thresholding mode, do not report consecutive samples that have PKEY\_SensorData\_IsValid set to FALSE. In other words, in thresholding mode, only send the first sample in which PKEY\_SensorData\_IsValid was switched to FALSE.

 

## <span id="related_topics"></span>Related topics


[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Light%20sensor%20thresholds%20and%20interval%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





