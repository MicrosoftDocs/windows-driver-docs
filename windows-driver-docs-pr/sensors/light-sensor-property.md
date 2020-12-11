---
title: Light sensor property
description: The property key for the light sensor.
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# Light sensor property

The property key for the light sensor.

| Property key | Type | Access (R/O, R/W) | Required/Optional | Description |
| --- | --- | --- | --- | --- |
| PKEY_LightSensor_ResponseCurve | VT_VECTOR | R/O | Required | The response curve of the light sensor. |
| DEVPKEY_SensorData_LightLevel_AutoBrightnessPreferred | VT_BOOL | R/O | Optional | The light sensor is preferred for auto-brightness. |
| DEVPKEY_SensorData_LightLevel_ColorCapable | VT_BOOL | R/O | Optional | Required if supporting chromaticity and light temperature. The light sensor supports light temperature and/or chromaticity x/y. |

For more information about the data type shown in the **Type** column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

## Remarks

To use this property key to set the value of its related property, you can use the **InitPropVariantFromUInt32Vector** function. For example, to set the value for the SENSOR\_PROPERTY\_MIN\_DATA\_INTERVAL property using the PKEY\_Sensor\_MinimumDataInterval\_Ms property key, you would use the following syntax:

```cpp
// Sensor Properties
     if (NT_SUCCESS(Status))
     {
         Status = InitSensorCollection(SENSOR_PROPERTIES_COUNT, &m_pSensorProperties, SensorInstance);
         if (NT_SUCCESS(Status))
         {
               m_Interval = DEFAULT_ACCELEROMETER_REPORT_INTERVAL;
               ...
               ...
               m_pSensorProperties->List[SENSOR_PROPERTY_MIN_DATA_INTERVAL].Key = PKEY_Sensor_MinimumDataInterval_Ms;
               InitPropVariantFromUInt32(ACCELEROMETER_MIN_REPORT_INTERVAL, &(m_pSensorProperties->List[SENSOR_PROPERTY_MIN_DATA_INTERVAL].Value));
               ...
         }
    }
```

For a complete example of sensor properties being set by using their related property keys, see the [client.cpp file](https://github.com/Microsoft/Windows-driver-samples/blob/master/sensors/ADXL345Acc/client.cpp) in the ADXL345Acc sample driver, and scroll down to the **NTSTATUS ADXL345AccDevice::Initialize(...)** routine.

**Header:** Sensorsdef.h
