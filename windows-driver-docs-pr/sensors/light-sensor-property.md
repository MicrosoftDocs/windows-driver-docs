---
title: Light sensor property
description: The property key for the light sensor.
ms.assetid: 87C58F14-E23D-4567-BBD5-AA42DF9371B0
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# Light sensor property


The property key for the light sensor.

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
<td><p>PKEY_LightSensor_ResponseCurve</p></td>
<td><p>VT_VECTOR | VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Required</p></td>
<td><p>The response curve of the light sensor.</p></td>
</tr>
<tr class="even">
<td><p>DEVPKEY_SensorData_LightLevel_AutoBrightnessPreferred</p></td>
<td><p>VT_BOOL</p></td>
<td><p>R/O</p></td>
<td><p>Optional</p></td>
<td><p>The light sensor is preferred for auto-brightness.</p></td>
</tr>
<tr class="odd">
<td><p>DEVPKEY_SensorData_LightLevel_ColorCapable</p></td>
<td><p>VT_BOOL</p></td>
<td><p>R/O</p></td>
<td><p>Optional. Required if supporting chromaticity and light temperature.</p></td>
<td><p>The light sensor supports light temperature and/or chromaticity x/y.</p></td>
</tr>
</tbody>
</table>

 

For more information about the data type shown in the **Type** column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

**Remarks**

To use this property key to set the value of its related property, you can use the **InitPropVariantFromUInt32Vector** function. For example, to set the value for the SENSOR\_PROPERTY\_MIN\_DATA\_INTERVAL property using the PKEY\_Sensor\_MinimumDataInterval\_Ms property key, you would use the following syntax:

```cpp
// Sensor Properties
     if (NT_SUCCESS(Status))
     {
         Status = InitSensorCollection(SENSOR_PROPERTIES_COUNT, &amp;m_pSensorProperties, SensorInstance);
         if (NT_SUCCESS(Status))
         {
               m_Interval = DEFAULT_ACCELEROMETER_REPORT_INTERVAL;
               ...
               ...
               m_pSensorProperties->List[SENSOR_PROPERTY_MIN_DATA_INTERVAL].Key = PKEY_Sensor_MinimumDataInterval_Ms;
               InitPropVariantFromUInt32(ACCELEROMETER_MIN_REPORT_INTERVAL, &amp;(m_pSensorProperties->List[SENSOR_PROPERTY_MIN_DATA_INTERVAL].Value));
               ...
         }
    }
```

For a complete example of sensor properties being set by using their related property keys, see the [client.cpp file](https://github.com/Microsoft/Windows-driver-samples/blob/master/sensors/ADXL345Acc/client.cpp) in the ADXL345Acc sample driver, and scroll down to the **NTSTATUS ADXL345AccDevice::Initialize(...)** routine.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


**Header:** Sensorsdef.h

## <span id="related_topics"></span>Related topics


[Other sensor properties](other-sensor-properties.md)

 

 






