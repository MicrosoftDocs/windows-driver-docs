---
title: Initializing the geolocation object
author: windows-driver-content
description: The object source file, geolocation.cpp, contains an Initialize method that initializes the settable property keys and data-field keys for the simulated geolocation-sensor. This method is invoked by the sensor manager at startup.
ms.assetid: 3803BD3B-9853-4AA4-A278-22F8D835B1ED
---

# Initializing the geolocation object


The object source file, geolocation.cpp, contains an **Initialize** method that initializes the settable property keys and data-field keys for the simulated geolocation-sensor. This method is invoked by the sensor manager at startup.

A property key (**PROPERTYKEY**) is a data structure consisting of a **GUID** and a **DWORD** that provide a unique identifier for the sensor property. In the case of the simulated geolocation-sensor, there are three settable property keys that correspond to: the device's change sensitivity, its current report interval, and the desired accuracy. These keys are defined in the file geolocation.cpp.

```ManagedCPlusPlus
const PROPERTYKEY g_SettableGeolocationProperties[] =
{
    SENSOR_PROPERTY_CHANGE_SENSITIVITY,         //[VT_UNKNOWN], IPortableDeviceValues
    SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL,    //[VT_UI4]
    SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY,  //[VT_UI4]
};
```

For more information about change sensitivity and the report interval, refer to the [Filtering data](https://msdn.microsoft.com/library/windows/hardware/hh706201) topic.

A data-field key is a **PROPERTYKEY** that the driver uses to identify each unique data field that it supports. In the case of the pseudo geolocation-sensor there are eight supported data fields that include data such as the timestamp of the reading, current latitude (in degrees), current longitude (in degrees), and so on. These keys are also defined in the file geolocation.cpp.

```ManagedCPlusPlus
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Initializing%20the%20geolocation%20object%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


