---
title: Supporting the accelerometer properties
description: The source file, SensorDdi.cpp, contains three arrays of PROPERTYKEY structures that define the properties supported by the accelerometer device.
ms.assetid: A1196CFD-9A90-479A-859E-6F9850867AC6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting the accelerometer properties


The source file, SensorDdi.cpp, contains three arrays of PROPERTYKEY structures that define the properties supported by the accelerometer device.

The first array contains the general sensor properties. These include strings like the manufacturer's name, the device model, its serial number and so on. In addition, there are values like the minimum and maximum range, the sensor resolution, and the minimum supported report interval.

```cpp
const PROPERTYKEY g_SupportedAccelerometerProperties[] =
{
    WPD_OBJECT_ID,
    SENSOR_PROPERTY_TYPE,
    SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID,
    SENSOR_PROPERTY_MANUFACTURER,
    SENSOR_PROPERTY_MODEL,
    SENSOR_PROPERTY_SERIAL_NUMBER,
    SENSOR_PROPERTY_FRIENDLY_NAME,
    SENSOR_PROPERTY_DESCRIPTION,
    SENSOR_PROPERTY_CONNECTION_TYPE,
    SENSOR_PROPERTY_RANGE_MINIMUM,
    SENSOR_PROPERTY_RANGE_MAXIMUM,
    SENSOR_PROPERTY_RESOLUTION,
    SENSOR_PROPERTY_STATE,
    SENSOR_PROPERTY_MIN_REPORT_INTERVAL,
    WPD_FUNCTIONAL_OBJECT_CATEGORY,
};
```

The second array contains three specific device properties: the minimum and maximum range as well as the sensor resolution.

```cpp
const PROPERTYKEY g_SupportedPerDataFieldProperties[] =
{
    SENSOR_PROPERTY_RANGE_MINIMUM,
    SENSOR_PROPERTY_RANGE_MAXIMUM,
    SENSOR_PROPERTY_RESOLUTION,
};
```

The third array contains the accelerometer's change sensitivity and the current report interval.

```cpp
const PROPERTYKEY g_SettableAccelerometerProperties[] =
{
    SENSOR_PROPERTY_CHANGE_SENSITIVITY,
    SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL,
};
```

## Related topics
[SpbAccelerometer driver sample](spbaccelerometer-driver-sample.md)



