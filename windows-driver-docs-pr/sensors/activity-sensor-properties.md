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

 

For more information about the data types shown in the **Type** column, see [MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


**Header:** Sensorsdef.h

## <span id="related_topics"></span>Related topics


[Other sensor properties](other-sensor-properties.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Activity%20sensor%20properties%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





