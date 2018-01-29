---
title: Accelerometer data fields
description: This topic provides information about the data fields that are specific to the accelerometer.
ms.assetid: 88333B6A-E262-4937-9349-156B00BA8CC4
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Accelerometer data fields


This topic provides information about the data fields that are specific to the accelerometer.

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
<td><p>PKEY_SensorData_AccelerationX_Gs</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>The x-axis acceleration in g’s.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_AccelerationY_Gs</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>The y-axis acceleration in g’s.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorData_AccelerationZ_Gs</p></td>
<td><p>VT_R4</p></td>
<td><p>Required</p></td>
<td><p>The z-axis acceleration in g’s.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_Shake</p></td>
<td><p>VT_BOOL</p></td>
<td><p>Optional</p></td>
<td><p>An indication that a shake has been detected by the accelerometer. This must be true if the data field is sent up.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Accelerometer%20data%20fields%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





