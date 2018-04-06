---
title: Activity sensor properties
description: The property keys for the activity sensor.
ms.assetid: 9C5DCE23-2690-4A22-8E38-D0571F997646
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Activity sensor properties


The property keys for the activity sensor.

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
<th>Access (R/O, R/W)</th>
<th>Required/Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_SensorData_SupportedActivityStates</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Required</p></td>
<td><p>The supported activity states.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_MinimumDetectionIntervals_Ms</p></td>
<td><p>VT_VECTOR | VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Required</p></td>
<td><p>The minimum time interval, expressed in milliseconds, for sampling activity data.</p></td>
</tr>
</tbody>
</table>

 

For more information about the data types shown in the **Type** column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


**Header:** Sensorsdef.h

## <span id="related_topics"></span>Related topics


[Other sensor properties](other-sensor-properties.md)

 

 






