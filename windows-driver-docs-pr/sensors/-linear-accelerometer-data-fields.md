---
title: Linear Accelerometer data fields
description: This topic provides information about the data fields that are specific to the linear accelerometer.
ms.assetid: FD869359-C1C2-4B2F-95F3-01234331DC54
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

#  Linear Accelerometer data fields


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This topic provides information about the data fields that are specific to the linear accelerometer.

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
<td><p>An indication that a shake has been detected by the linear accelerometer. This must be true if the data field is sent up.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






