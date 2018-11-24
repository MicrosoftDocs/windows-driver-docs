---
title: Sensor types
description: Universal Sensor Type GUIDs
ms.assetid: AD1112ED-4EA8-429D-82E6-D1878447D5E3
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors/sensors%5D:%20sensor%20types%20%20RELEASE:%20%2802/19/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
