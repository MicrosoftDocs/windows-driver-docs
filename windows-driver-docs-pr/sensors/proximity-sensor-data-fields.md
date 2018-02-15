---
title: Proximity sensor data fields
description: This topic provides information about the data fields that are specific to the proximity sensor.
ms.assetid: 03B561DB-FAF2-4404-AA49-6A0DA139AA11
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Proximity sensor data fields


This topic provides information about the data fields that are specific to the proximity sensor.

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
<td><p>PKEY_SensorData_ProximityDetection</p></td>
<td><p>VT_BOOL</p></td>
<td><p>Required</p></td>
<td><p>An indication that an object is within proximity of the sensor.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorData_ProximityDistanceMillimeters</p></td>
<td><p>VT_UI4</p></td>
<td><p>Optional</p></td>
<td><p>Distance to the detected object, in millimeters.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


If a sensor supports the **PKEY\_SensorData\_ProximityDistanceMillimeters** data field, then in response to a call from [EvtSensorGetDataFieldProperties](https://msdn.microsoft.com/library/windows/hardware/dn957029) for the **PKEY\_SensorData\_ProximityDistanceMillimeters** data field, the sensor must report the following data field *properties*:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Data field property</th>
<th>Type</th>
<th>Required/Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_SensorDataField_RangeMinimum</p></td>
<td><p>VT_R4 (float)</p></td>
<td><p>Required</p></td>
<td><p>Indicates the lower boundary (inclusive) of the sensor’s effective detection range in millimeters.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorDataField_RangeMaximum</p></td>
<td><p>VT_R4 (float)</p></td>
<td><p>Required</p></td>
<td><p>Indicates the upper boundary (inclusive) of the sensor’s effective detection range in millimeters.</p></td>
</tr>
</tbody>
</table>

 

**Note**  The effective detection range is a straight-line distance from the sensor to the object. This distance is measured along the axis in which the sensor is pointing, and it's inclusive of the actual boundaries.

 

If the driver fails to report these data-field properties, Apps will still be able to detect the proximity sensor via the WinRT API. However, these Apps will not know the supported-range of the sensor, and might decide not to use the sensor.

## <span id="related_topics"></span>Related topics


[EvtSensorGetDataFieldProperties](https://msdn.microsoft.com/library/windows/hardware/dn957029)

[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Proximity%20sensor%20data%20fields%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





