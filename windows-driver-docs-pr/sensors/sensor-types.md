---
title: Sensor types
description: Universal Sensor Type GUIDs
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Sensor types

This section provides information about sensor type GUIDs that are associated with each type of sensor. Sensor types represent specific kinds of sensors. Each sensor type can optionally fit into a particular category.

Sensor type GUIDs are defined in Sensorsdef.h.

| Name | Description |
| --- | --- |
| GUID_SensorType_Accelerometer3D | This GUID identifies the accelerometer. |
| GUID_SensorType_ActivityDetection | This GUID identifies the activity detection sensor. |
| GUID_SensorType_AmbientLight | This GUID identifies the ambient light sensor. |
| GUID_SensorType_Barometer | This GUID identifies the barometer |
| GUID_SensorType_Custom | This GUID identifies a custom sensor. |
| GUID_SensorType_GeomagneticOrientation | This GUID identifies the geomagnetic orientation. |
| GUID_SensorType_GravityVector | This GUID identifies the gravity vector. |
| GUID_SensorType_Gyrometer3D | This GUID identifies the gyrometer. |
| GUID_SensorType_Humidity | This GUID identifies the humidity sensor. |
| GUID_SensorType_LinearAccelerometer | This GUID identifies the linear accelerometer. |
| GUID_SensorType_Magnetometer3D | This GUID identifies the magnetometer. |
| GUID_SensorType_Orientation | This GUID identifies the orientation sensor. |
| GUID_SensorType_Pedometer | This GUID identifies the pedometer. |
| GUID_SensorType_Proximity | This GUID identifies the proximity sensor. |
| GUID_SensorType_RelativeOrientation | This GUID identifies the RelativeOrientation sensor. |
| GUID_SensorType_SimpleDeviceOrientation | This GUID identifies the simple device orientation sensor. |
| GUID_SensorType_Temperature | This GUID identifies the temperature sensor. |

>[!NOTE]
> Compass and Inclinometer sensors are not directly exposed through the Windows universal sensors DDI. Instead, these two sensors are automatically constructed by the sensor stack on top of the GUID_SensorType_Orientation sensor.
> Compass and Inclinometer will be visible to WinRT applications whenever a GUID_SensorType_Orientation sensor is present on the system. Similarly, the altimeter sensor is automatically constructed by the sensor stack on top of the GUID_SensorType_Barometer sensor.


