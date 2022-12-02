---
title: Sensor Properties
description: The Sensor and Location platform defines constants that identify properties for sensors. Sensor manufacturers can also define their own properties.
topic_type:
- apiref
api_name:
- SENSOR_PROPERTY_ACCURACY
- SENSOR_PROPERTY_CHANGE_SENSITIVITY
- SENSOR_PROPERTY_CONNECTION_TYPE
- SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL
- SENSOR_PROPERTY_DESCRIPTION
- SENSOR_PROPERTY_DEVICE_PATH
- SENSOR_PROPERTY_FRIENDLY_NAME
- SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE
- SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY
- SENSOR_PROPERTY_MANUFACTURER
- SENSOR_PROPERTY_MIN_REPORT_INTERVAL
- SENSOR_PROPERTY_MODEL
- SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID
- SENSOR_PROPERTY_RANGE_MAXIMUM
- SENSOR_PROPERTY_RANGE_MINIMUM
- SENSOR_PROPERTY_RESOLUTION
- SENSOR_PROPERTY_SERIAL_NUMBER
- SENSOR_PROPERTY_STATE
- SENSOR_PROPERTY_TURN_ON_OFF_NMEA
- SENSOR_PROPERTY_TYPE
- WPD_FUNCTIONAL_OBJECT_CATEGORY
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 12/02/2022
---

# Sensor Properties

The Sensor and Location platform defines constants that identify properties for sensors. Sensor manufacturers can also define their own properties.

The platform defines the following **PROPERTYKEY** values for sensor properties. These properties are read-only unless otherwise noted.

Each platform-defined sensor property **PROPERTYKEY** is based on a common **GUID** named **SENSOR_PROPERTY_COMMON_GUID**: {7F8383EC-D3EC-495C-A8CF-B8BBE85C2920}.

> [!IMPORTANT]
> Do not use this base value to define your own property keys.

Values for properties designated as read/write can be specified by the client application. Values for properties designated as static must not change over time. Properties designated as required must be supported by the sensor.

| Property key name and PID | Type | Description |
|---|---|---|
| **SENSOR_PROPERTY_ACCURACY**</br>(PID = 17) | **VT_UNKNOWN** | Read only. [IPortableDeviceValues](/windows/win32/wpd_sdk/iportabledevicevalues) object that contains sensor data type names and their associated accuracies. Accuracy values represent possible variation from true values. Accuracy values are expressed by using the same units as the data field, except when otherwise documented. |
| **SENSOR_PROPERTY_CHANGE_SENSITIVITY**</br>(PID = 14) | **VT_UNKNOWN** | Read/write. **IPortableDeviceValues** object that contains sensor data type names and their associated change sensitivity values. Change sensitivity values provide requests about the amount by which the data field should change before the SENSOR_EVENT_DATA_UPDATED event is raised.</br></br>Sensitivity values are expressed by using the same units as the data field, except where otherwise documented.</br></br>For some sensors, the change sensitivity is interpreted as an actual value. For example, a change sensitivity value of 2 for SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS represents a sensitivity of plus or minus 2 degrees Celsius.</br></br>For other sensors, like the ambient light sensor (ALS), the change sensitivity is interpreted as a percent. So, a change sensitivity of 2 for SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX represents plus or minus 2% of LUX.</br></br>You can set this value to request a particular change sensitivity, but multiple applications could be using the same sensor. Therefore, sensors determine the true change sensitivity, based on their internal logic. For example, the sensor might always use the smallest change sensitivity that is requested by any of the applications.</br></br>If an application sets this property to VT_NULL, the device driver should reset SENSOR_PROPERTY_CHANGE_SENSITIVITY to its default value. |
| **SENSOR_PROPERTY_CONNECTION_TYPE**</br>(PID = 11) | **VT_UI4** | Read only. [SensorConnectionType](/windows/win32/api/sensorsapi/ne-sensorsapi-sensorconnectiontype) value that contains the current connection type. |
| **SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL**</br>(PID = 13) | **VT_UI4** | Read/write. The current elapsed time for sensor data report generation, in milliseconds.</br></br>Setting a value of zero signals the driver to return either: the default report interval, or, the smallest report interval. If there is only one client connected, the driver should return the default report interval. If multiple clients are connected, the driver should return the smallest interval requested by any of those clients.</br></br>Applications can set this value to request a particular report interval, but multiple applications could be using the same driver. Therefore, drivers determine the true report interval, based on internal logic. For example, the driver might always use the shortest report interval that is requested by any caller.</br></br>For an example of how to use this property, see [Using Sensor API Events](/windows/desktop/SensorsAPI/using-sensor-api-events). |
| **SENSOR_PROPERTY_DESCRIPTION**</br>(PID = 10) | **VT_LPWSTR** | Read only. The sensor description string. |
| **SENSOR_PROPERTY_DEVICE_PATH**</br>(PID = 15) | **VT_LPWSTR** | Read only. Uniquely identifies the device instance with which the sensor is associated. You can use this property to determine whether a device contains multiple sensors.</br></br>Device drivers do not have to support this property because the platform provides this value to applications without querying drivers. |
| **SENSOR_PROPERTY_FRIENDLY_NAME**</br>(PID = 9) | **VT_LPWSTR** | Read only. Required, static. The friendly name for the device. |
| **SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE**</br>(PID = 16) | **VT_VECTOR\|VT_UI1** | Read only. A counted array that contains pairs of values that provide a mapping between ambient light levels and offsets. These values are expressed as percentages. The adaptive brightness feature in Windows applies these values to the user's current display brightness preference.</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters). This property actually contains each value as a 4-byte unsigned integer (VT_UI4). For information about working with arrays, see [Retrieving Vector Types](/windows/desktop/SensorsAPI/retrieving-vector-types). |
| **SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY**</br>(PID = 19) | **VT_UI4** | Read/write. A value from the [LOCATION_DESIRED_ACCURACY](/windows/win32/api/sensorsapi/ne-sensorsapi-location_desired_accuracy) enumeration that indicates the type of accuracy handling requested by a client application.</br></br>**LOCATION_DESIRED_ACCURACY_DEFAULT** (0) indicates that the sensor should use the accuracy for which it can optimize power use and other cost considerations.</br></br>**LOCATION_DESIRED_ACCURACY_HIGH** (1) indicates that the sensor should deliver the most accurate report possible. This includes using services that might charge money, or consuming higher levels of battery power or connection bandwidth. |
| **SENSOR_PROPERTY_MANUFACTURER**</br>(PID = 6) | **VT_LPWSTR** | Read only. Required, static. The manufacturer's name. |
| **SENSOR_PROPERTY_MIN_REPORT_INTERVAL**</br>(PID = 12) | **VT_UI4** | Read only. Required, static. The minimum interval that the hardware supports for sensor data report generation, in milliseconds. |
| **SENSOR_PROPERTY_MODEL**</br>(PID = 7) | **VT_LPWSTR** | Read only. Required, static. The sensor model name. |
| **SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID**</br>(PID = 5) | **VT_CLSID** | Read only. Required, static. A GUID that identifies the sensor. This value must be unique for each sensor on a device, or across devices of the same model as enumerated on the computer. This property contains the same value obtained by calling [ISensor::GetID](/windows/desktop/api/sensorsapi/nf-sensorsapi-isensor-getid). |
| **SENSOR_PROPERTY_RANGE_MAXIMUM**</br>(PID = 21) | **VT_UNKNOWN** | Read only. **IPortableDeviceValues** object that contains sensor data field names and their associated maximum values. |
| **SENSOR_PROPERTY_RANGE_MINIMUM**</br>(PID = 20) | **VT_UNKNOWN** | Read only. **IPortableDeviceValues** object that contains sensor data field names and their associated minimum values. |
| **SENSOR_PROPERTY_RESOLUTION**</br>(PID = 18) | **VT_UNKNOWN** | Read only. **IPortableDeviceValues** object that contains sensor data field names and their associated resolutions. Resolution values represent sensitivity to change in the data field.</br></br>Resolution values are expressed by using the same units as the data field, except when otherwise documented. |
| **SENSOR_PROPERTY_SERIAL_NUMBER**</br>(PID = 8) | **VT_LPWSTR** | Read only. Required, static. The sensor serial number. |
| **SENSOR_PROPERTY_STATE**</br>(PID = 3) | **VT_UI4** | Read only. Required.</br></br>[SensorState](/windows/win32/api/sensorsapi/ne-sensorsapi-sensorstate) value that contains the current sensor state.</br></br> **Note**  To update this property, raise a state-changed event by calling [ISensorClassExtension::PostStateChange](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-poststatechange).</br></br> |
| **SENSOR_PROPERTY_TURN_ON_OFF_NMEA**</br>(PID = 3) | **VT_UI4** | Read/write. If TRUE, an NMEA sentence will be included in data reports. If False, NMEA sentence is not included. |
| **SENSOR_PROPERTY_TYPE**</br>(PID = 2) | **VT_CLSID** | Read only. Required, static. A **GUID** that identifies the sensor type. Platform-defined sensor types are defined in Sensors.h. |

The following Windows Portable Devices (WPD) property must be supported by all sensors.

| Property key | Type | Description |
|---|---|---|
| **WPD_FUNCTIONAL_OBJECT_CATEGORY** | **VT_CLSID** | Read only. Required, static. Defines the sensor category. |

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Header** | sensors.h |

## See also

- **[GetProperties](/windows/desktop/api/sensorsapi/nf-sensorsapi-isensor-getproperties)**
- **[GetProperty](/windows/desktop/api/sensorsapi/nf-sensorsapi-isensor-getproperty)**
- [IPortableDeviceValues](/windows/win32/wpd_sdk/iportabledevicevalues)
- **[SetProperties](/windows/desktop/api/sensorsapi/nf-sensorsapi-isensor-setproperties)**
