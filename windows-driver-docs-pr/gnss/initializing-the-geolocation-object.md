---
title: Initializing the geolocation object
description: Geolocation.cpp contains an Initialize method that initializes the settable property keys and data-field keys for the simulated geolocation-sensor.
ms.assetid: 3803BD3B-9853-4AA4-A278-22F8D835B1ED
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing the geolocation object

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The object source file, geolocation.cpp, contains an **Initialize** method that initializes the settable property keys and data-field keys for the simulated geolocation-sensor. This method is invoked by the sensor manager at startup.

A property key (**PROPERTYKEY**) is a data structure consisting of a **GUID** and a **DWORD** that provide a unique identifier for the sensor property. In the case of the simulated geolocation-sensor, there are three settable property keys that correspond to: the device's change sensitivity, its current report interval, and the desired accuracy. These keys are defined in the file geolocation.cpp.

```cpp
const PROPERTYKEY g_SettableGeolocationProperties[] =
{
    SENSOR_PROPERTY_CHANGE_SENSITIVITY,         //[VT_UNKNOWN], IPortableDeviceValues
    SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL,    //[VT_UI4]
    SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY,  //[VT_UI4]
};
```

For more information about change sensitivity and the report interval, refer to the [Filtering data](https://msdn.microsoft.com/library/windows/hardware/hh706201) topic.

A data-field key is a **PROPERTYKEY** that the driver uses to identify each unique data field that it supports. In the case of the pseudo geolocation-sensor there are eight supported data fields that include data such as the timestamp of the reading, current latitude (in degrees), current longitude (in degrees), and so on. These keys are also defined in the file geolocation.cpp.

```cpp
const PROPERTYKEY g_SupportedGeolocationDataFields[] =
{
    SENSOR_DATA_TYPE_TIMESTAMP,                 //[VT_FILETIME]
    SENSOR_DATA_TYPE_LATITUDE_DEGREES,          //[VT_R8]
    SENSOR_DATA_TYPE_LONGITUDE_DEGREES,         //[VT_R8]
    SENSOR_DATA_TYPE_ERROR_RADIUS_METERS,       //[VT_R8]
    SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS, //[VT_R8]
    SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS, //[VT_R8]
    SENSOR_DATA_TYPE_SPEED_KNOTS,               //[VT_R8]
    SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES,      //[VT_R8]
};
```

The **CSensorManager::Start** method invokes **CGeolocation::Initialize** immediately after it creates the sensor Device Driver Interface (DDI). This work occurs in the module sensormanager.cpp.

The **Initialize** method, in turn, invokes an **InitializeGeolocation** method. This latter method invokes **CGeolocation::AddGeolocationSettablePropertyKeys** to initialize the property keys for the writeable properties supported by the pseudo-sensor. After adding the property keys, the **InitializeGeolocation** method invokes **CGeolocation::AddGeolocationDataFieldKeys** to initialize the data field keys for the supported data fields.

## Related topics
[Defining the geolocation object](defining-the-geolocation-object.md)  
[Filtering data](https://msdn.microsoft.com/library/windows/hardware/hh706201)  



