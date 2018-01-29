---
title: About Sensor Constants
author: windows-driver-content
description: About Sensor Constants
ms.assetid: 9c26e305-0d5c-4442-9bcf-a9cdc1778c6b
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# About Sensor Constants


The Windows Sensor and Location Platform uses constants in a variety of ways. This section describes these constants and their usage.

The platform defines a variety of constants you can use in your sensor driver code. You can also define your own constants. You can find the definitions of platform-defined constants in the files Sensors.h and Sensorsdef.h. For detailed information about platform-defined sensor constants, see [Constants](https://msdn.microsoft.com/library/windows/hardware/ff545409).

### Sensor and Data Organization

The platform organizes sensors and their data in the following ways:

-   *Categories* represent broad classes of sensor devices. Categories provide a way to group sensors that are likely to provide similar types of information, or are otherwise related in some way. Each category is represented by a GUID constant. For example, sensors that report latitude and longitude coordinates belong to the location sensor category, which is represented by the [**SENSOR\_CATEGORY\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/dn265186) constant.

-   *Sensor types* represent specific kinds of sensors. Each sensor type fits into a particular category. Two sensors of different types can belong to the same category or two different categories. Each sensor type is represented by a GUID constant. For example, a global positioning system sensor would be identified by the SENSOR\_TYPE\_LOCATION\_GPS constant, while a sensor that provides the current location using an Internet IP address would be identified by the SENSOR\_TYPE\_LOCATION\_LOOKUP constant. However, both sensors would belong to the location sensor category.

-   *Data types* represent specific kinds of information that the sensor can provide. Sensor data types can contain the actual measurement value, such as altitude, information about the units used to express the data, for example meters, and reference points for the data, for example sea level. Each data type is represented by a **PROPERTYKEY** constant. For example, the data type that represents the x-axis acceleration in g's would be the SENSOR\_DATA\_TYPE\_ACCELERATION\_X\_G constant.

-   When reporting data, a value is said to be contained in a *data field*, and a collection of related data fields comprise a *data report*. Data reports are packaged together by using the [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) interface. Each data report must contain at least one valid data field and a time stamp that identifies when the data report was created. Time stamps are represented by the SENSOR\_DATA\_TYPE\_TIMESTAMP property key.

### Sensor categories

The following GUIDs associate each sensor category to the sensor class extension. These GUIDs can also be used to search for sensors in the system. They are defined in the file Sensorsdef.h.

| Name | Description | Syntax |
| --- | --- | --- |
| GUID_SensorCategory_All| This GUID identifies all of the sensors. | `DEFINE_GUID(GUID_SensorCategory_All, 0XC317C286, 0XC468, 0X4288, 0X99, 0X75, 0XD4, 0XC4, 0X58, 0X7C, 0X44, 0X2C);`|
| GUID_SensorCategory_Biometric | This GUID identifies the biometric sensor category. | `DEFINE_GUID(GUID_SensorCategory_Biometric, 0XCA19690F, 0XA2C7, 0X477D, 0XA9, 0X9E, 0X99, 0XEC, 0X6E, 0X2B, 0X56, 0X48);` |
| GUID_SensorCategory_Electrical | This GUID identifies the electrical sensor category. | `DEFINE_GUID(GUID_SensorCategory_Electrical, 0XFB73FCD8, 0XFC4A, 0X483C, 0XAC, 0X58, 0X27, 0XB6, 0X91, 0XC6, 0XBE, 0XFF);`|
| GUID_SensorCategory_Environmental| This GUID identifies the environmental sensor category. | `DEFINE_GUID(GUID_SensorCategory_Environmental, 0X323439AA, 0X7F66, 0X492B, 0XBA, 0X0C, 0X73, 0XE9, 0XAA, 0X0A, 0X65, 0XD5);`|
| GUID_SensorCategory_Light| This GUID identifies the light sensor category. | `DEFINE_GUID(GUID_SensorCategory_Light, 0X17A665C0, 0X9063, 0X4216, 0XB2, 0X02, 0X5C, 0X7A, 0X25, 0X5E, 0X18, 0XCE);`|
| GUID_SensorCategory_Location | This GUID identifies the location sensor category. | `DEFINE_GUID(GUID_SensorCategory_Location, 0XBFA794E4, 0XF964, 0X4FDB, 0X90, 0XF6, 0X51, 0X05, 0X6B, 0XFE, 0X4B, 0X44);`|
| GUID_SensorCategory_Mechanical| This GUID identifies the mechanical sensor category.| `DEFINE_GUID(GUID_SensorCategory_Mechanical, 0X8D131D68, 0X8EF7, 0X4656, 0X80, 0XB5, 0XCC, 0XCB, 0XD9, 0X37, 0X91, 0XC5);`|
| GUID_SensorCategory_Motion| This GUID identifies the motion sensor category. | `DEFINE_GUID(GUID_SensorCategory_Motion, 0XCD09DAF1, 0X3B2E, 0X4C3D, 0XB5, 0X98, 0XB5, 0XE5, 0XFF, 0X93, 0XFD, 0X46);`|
| GUID_SensorCategory_Orientation | This GUID identifies the orientation sensor category. | `DEFINE_GUID(GUID_SensorCategory_Orientation, 0X9E6C04B6, 0X96FE, 0X4954, 0XB7, 0X26, 0X68, 0X68, 0X2A, 0X47, 0X3F, 0X69);`|
| GUID_SensorCategory_Other | This GUID identifies a category for sensors that are supported, but do not fit into any of the predefined categories.| `DEFINE_GUID(GUID_SensorCategory_Other, 0x2C90E7A9, 0xF4C9, 0x4FA2, 0xAF, 0x37, 0x56, 0xD4, 0x71, 0xFE, 0x5A, 0x3D);`|
| GUID_SensorCategory_Scanner| This GUID identifies the scanner sensor category.| `DEFINE_GUID(GUID_SensorCategory_Scanner, 0XB000E77E, 0XF5B5, 0X420F, 0X81, 0X5D, 0X02, 0X70, 0XA7, 0X26, 0XF2, 0X70);`|
| GUID_SensorCategory_Unsupported| This GUID identifies a category for sensors that are unsupported.| `DEFINE_GUID(GUID_SensorCategory_Unsupported, 0x2BEAE7fA, 0x19B0, 0x48C5, 0xA1, 0xF6, 0xB5, 0x48, 0x0D, 0xC2, 0x06, 0xB0);`|

### Sensor Types

This section provides information about the GUIDs that are associated with each type of sensor. They are defined in the file Sensorsdef.h.

| Name | Description | Syntax |
| --- | --- | --- |
| GUID_SensorType_Accelerometer3D | This GUID identifies the accelerometer. |`DEFINE_GUID(GUID_SensorType_Accelerometer3D, 0XC2FB0F5F, 0XE2D2, 0X4C78, 0XBC, 0XD0, 0X35, 0X2A, 0X95, 0X82, 0X81, 0X9D);`|
| GUID_SensorType_ActivityDetection | This GUID identifies the activity detection sensor. | `DEFINE_GUID(GUID_SensorType_ActivityDetection, 0X9D9E0118, 0X1807, 0X4F2E, 0X96, 0XE4, 0X2C, 0XE5, 0X71, 0X42, 0XE1, 0X96);`|
| GUID_SensorType_AmbientLight | This GUID identifies the ambient light sensor. | `DEFINE_GUID(GUID_SensorType_AmbientLight, 0X97F115C8, 0X599A, 0X4153, 0X88, 0X94, 0XD2, 0XD1, 0X28, 0X99, 0X91, 0X8A);`|
| GUID_SensorType_Barometer | This GUID identifies the barometer |`DEFINE_GUID(GUID_SensorType_Barometer, 0X0E903829, 0XFF8A, 0X4A93, 0X97, 0XDF, 0X3D, 0XCB, 0XDE, 0X40, 0X22, 0X88);`|
| GUID_SensorType_Custom | This GUID identifies a custom sensor. | `DEFINE_GUID(GUID_SensorType_Custom, 0XE83AF229, 0X8640, 0X4D18, 0XA2, 0X13, 0XE2, 0X26, 0X75, 0XEB, 0XB2, 0XC3);`|
| GUID_SensorType_GeomagneticOrientation | This GUID identifies the geomagnetic orientation. | `DEFINE_GUID(GUID_SensorType_GeomagneticOrientation, 0XE77195F8, 0X2D1F, 0X4823, 0X97, 0X1B, 0X1C, 0X44, 0X67, 0X55, 0X6C, 0X9D);`|
| GUID_SensorType_GravityVector | This GUID identifies the gravity vector. | `DEFINE_GUID(GUID_SensorType_GravityVector, 0X03B52C73, 0XBB76, 0X463F, 0X95, 0X24, 0X38, 0XDE, 0X76, 0XEB, 0X70, 0X0B);`|
| GUID_SensorType_Gyrometer3D | This GUID identifies the gyrometer. | `DEFINE_GUID(GUID_SensorType_Gyrometer3D, 0X09485F5A, 0X759E, 0X42C2, 0XBD, 0X4B, 0XA3, 0X49, 0XB7, 0X5C, 0X86, 0X43);`|
| GUID_SensorType_Humidity | This GUID identifies the humidity sensor. | `DEFINE_GUID(GUID_SensorType_Humidity, 0X5C72BF67, 0XBD7E, 0X4257, 0X99, 0X0B, 0X98, 0XA3, 0XBA, 0X3B, 0X40, 0X0A);`|
| GUID_SensorType_LinearAccelerometer | This GUID identifies the linear accelerometer. | `DEFINE_GUID(GUID_SensorType_LinearAccelerometer, 0X038B0283, 0X97B4, 0X41C8, 0XBC, 0X24, 0X5F, 0XF1, 0XAA, 0X48, 0XFE, 0XC7)`|
| GUID_SensorType_Magnetometer3D | This GUID identifies the magnetometer. | `DEFINE_GUID(GUID_SensorType_Magnetometer3D, 0x55e5effb, 0x15c7, 0x40df, 0x86, 0x98, 0xa8, 0x4b, 0x7c, 0x86, 0x3c, 0x53);`|
| GUID_SensorType_Orientation | This GUID identifies the orientation sensor. | `DEFINE_GUID(GUID_SensorType_Orientation, 0XCDB5D8F7, 0X3CFD, 0X41C8, 0X85, 0X42, 0XCC, 0XE6, 0X22, 0XCF, 0X5D, 0X6E);`|
| GUID_SensorType_Pedometer | This GUID identifies the pedometer. | `DEFINE_GUID(GUID_SensorType_Pedometer, 0XB19F89AF, 0XE3EB, 0X444B, 0X8D, 0XEA, 0X20, 0X25, 0X75, 0XA7, 0X15, 0X99);`|
| GUID_SensorType_Proximity | This GUID identifies the proximity sensor. | `DEFINE_GUID(GUID_SensorType_Proximity, 0X5220DAE9, 0X3179, 0X4430, 0X9F, 0X90, 0X06, 0X26, 0X6D, 0X2A, 0X34, 0XDE);`|
| GUID_SensorType_RelativeOrientation | This GUID identifies the RelativeOrientation sensor. | `DEFINE_GUID(GUID_SensorType_RelativeOrientation, 0x40993b51, 0x4706, 0x44dc, 0x98, 0xd5, 0xc9, 0x20, 0xc0, 0x37, 0xff, 0xab);`|
| GUID_SensorType_SimpleDeviceOrientation | This GUID identifies the simple device orientation sensor. | `DEFINE_GUID(GUID_SensorType_SimpleDeviceOrientation, 0X86A19291, 0X0482, 0X402C, 0XBF, 0X4C, 0XAD, 0XDA, 0XC5, 0X2B, 0X1C, 0X39);`|
| GUID_SensorType_Temperature | This GUID identifies the temperature sensor.|`DEFINE_GUID(GUID_SensorType_Temperature, 0X04FD0EC4, 0XD5DA, 0X45FA, 0X95, 0XA9, 0X5D, 0XB3, 0X8E, 0XE1, 0X93, 0X06);`|





### Other Constants

Your driver will need to use some other kinds of constants, as well. These constants include:

-   Sensor properties, such as SENSOR\_PROPERTY\_DESCRIPTION. These constants include WPD constants, such as WPD\_FUNCTIONAL\_OBJECT\_CATEGORY. Usually, these constants are used to describe your sensor, such as when called in [**ISensorDriver::OnGetSupportedSensorObjects**](https://msdn.microsoft.com/library/windows/hardware/ff545633). You will also return property values through [**ISensorDriver::OnGetSupportedProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545630) and [**ISensorDriver::OnGetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545610).

-   Some sensor properties are required to be provided by your driver, some properties can be set by client applications, and some must always return the same value. The [**Sensor Properties**](https://msdn.microsoft.com/library/windows/hardware/ff545859) reference section provides this information for each property. To understand which properties are required for a particular method, see the method documentation in the [Windows Sensor Reference](https://msdn.microsoft.com/library/windows/hardware/ff545907) section.

-   [**Event constants**](about-sensor-driver-events.md), such as SENSOR\_EVENT\_STATE\_CHANGED. Event constants include GUIDS, which represent types of events, and PROPERTYKEYs, which represent event parameter types. You will use these constants when called by the class extension in [**ISensorDriver::OnGetSupportedEvents**](https://msdn.microsoft.com/library/windows/hardware/ff545623), or when raising events through [**ISensorClassExtension::PostEvent**](https://msdn.microsoft.com/library/windows/hardware/ff545519) or [**ISensorClassExtension::PostStateChange**](https://msdn.microsoft.com/library/windows/hardware/ff545523).

-   Icon constants. Your driver can specify a particular icon to represent the device in Windows. See [Specifying an Icon](specifying-an-icon.md).

-   The sensor platform defines the GUID_DEVINTERFACE_SENSOR constant, to identify the sensor device interface class. During its installation, a driver registers for at least one device interface class. The sensor class extension registers the sensor device interface class for you.



### Persistent Unique Identifier

The sensor property named SENSOR\_PROPERTY\_PERSISTENT\_UNIQUE\_ID requires special attention. The value for this property must be unique for each sensor on a device. At the same time, this value must remain consistent for a particular sensor each time the sensor platform uses it. For an example of how to create the persistent unique identifier in your driver code, see [Creating a Persistent Unique Identifier](creating-a-persistent-unique-identifier.md).

### Providing Geolocation Information

Sometimes it is important for users to know the physical location of a sensor, even if the sensor is not a location sensor. For example, the meaning of data that a weather station provides is closely tied to the location of the station.

To provide this type of geolocation data, any sensor can use appropriate data fields from the [**SENSOR\_CATEGORY\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/dn265186) category, even if the sensor is not a location sensor. Thus, a weather station could report its location by using the SENSOR\_DATA\_TYPE\_LATITUDE\_DEGREES and SENSOR\_DATA\_TYPE\_LONGITUDE\_DEGREES data-field constants. However, it is important not to report such sensors as belonging to the Location category, when called in [**ISensorDriver::OnGetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545610).

Windows treats a sensor with any of the location types as existing in the location category (SENSOR\_CATEGORY\_LOCATION). As a result, these sensors fall under the location permissioning model. You should not attempt to bypass the permissioning model for a location sensor (for example, surfacing a GPS sensor type as SENSOR\_TYPE\_LOCATION\_GPS but specifying a non-locaiton category).

### Custom Values

You can define custom values for categories, sensor types, data fields, properties, and events.

For guidelines and an example of how to define custom values for constants, see [Defining Custom Values for Constants](defining-custom-values-for-constants.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20About%20Sensor%20Constants%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


