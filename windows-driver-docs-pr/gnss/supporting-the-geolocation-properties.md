---
title: Supporting the geolocation properties
description: The source file, geolocation.cpp, contains three arrays of PROPERTYKEY structures that define the properties supported by the simulated sensor.
ms.assetid: 0D25D58F-1023-4470-9F7D-E62544B87A42
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting the geolocation properties

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The source file, geolocation.cpp, contains three arrays of PROPERTYKEY structures that define the properties supported by the simulated sensor.

The first array defines the read-only and read-write properties supported by the simulated sensor.

```cpp
const PROPERTYKEY g_SupportedGeolocationProperties[] =
{
    SENSOR_PROPERTY_TYPE,                       //[VT_CLSID]
    SENSOR_PROPERTY_STATE,                      //[VT_UI4]
    SENSOR_PROPERTY_MIN_REPORT_INTERVAL,        //[VT_UI4]
    SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL,    //[VT_UI4]
    SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID,       //[VT_CLSID]
    SENSOR_PROPERTY_MANUFACTURER,               //[VT_LPWSTR]
    SENSOR_PROPERTY_MODEL,                      //[VT_LPWSTR]
    SENSOR_PROPERTY_SERIAL_NUMBER,              //[VT_LPWSTR]
    SENSOR_PROPERTY_FRIENDLY_NAME,              //[VT_LPWSTR]
    SENSOR_PROPERTY_DESCRIPTION,                //[VT_LPWSTR]
    SENSOR_PROPERTY_CONNECTION_TYPE,            //[VT_UI4]
    SENSOR_PROPERTY_CHANGE_SENSITIVITY,         //[VT_UNKNOWN], IPortableDeviceValues
    SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY,  //[VT_UI4]
    WPD_FUNCTIONAL_OBJECT_CATEGORY,             //[VT_CLSID]
};
```

The sample driver uses these values when retrieving a property (or properties) in response to an application request. The method that retrieves property values is **CGeolocation::GetPropertyValuesForGeolocationObject**.

The second array defines optional properties.

```cpp
const PROPERTYKEY g_OptionalSupportedGeolocationProperties[] =
{
    SENSOR_PROPERTY_RANGE_MAXIMUM,              //[VT_UNKNOWN], IPortableDeviceValues
    SENSOR_PROPERTY_RANGE_MINIMUM,              //[VT_UNKNOWN], IPortableDeviceValues
    SENSOR_PROPERTY_ACCURACY,                   //[VT_UNKNOWN], IPortableDeviceValues
    SENSOR_PROPERTY_RESOLUTION,                 //[VT_UNKNOWN], IPortableDeviceValues
};
```

The third array defines the writeable, or settable, properties supported by the pseudo sensor.

```cpp
const PROPERTYKEY g_SettableGeolocationProperties[] =
{
    SENSOR_PROPERTY_CHANGE_SENSITIVITY,         //[VT_UNKNOWN], IPortableDeviceValues
    SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL,    //[VT_UI4]
    SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY,  //[VT_UI4]
};
```

The sample driver also uses these values when updating a writeable property (or properties). The method that updates property values is **CGeolocation::UpdateGeolocationPropertyValues**.

## Related topics
[The Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md)  



