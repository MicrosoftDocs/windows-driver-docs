---
title: Light sensor property
description: The property key for the light sensor.
ms.assetid: 87C58F14-E23D-4567-BBD5-AA42DF9371B0
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

For more information about the data type shown in the **Type** column, see [MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

**Remarks**

To use this property key to set the value of its related property, you can use the **InitPropVariantFromUInt32Vector** function. For example, to set the value for the SENSOR\_PROPERTY\_MIN\_DATA\_INTERVAL property using the PKEY\_Sensor\_MinimumDataInterval\_Ms property key, you would use the following syntax:

```ManagedCPlusPlus
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Light%20sensor%20property%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





