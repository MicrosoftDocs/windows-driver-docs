---
title: About Sensor Constants
description: About Sensor Constants
MS-HAID:
- 'Sensor\_DG\_Overview\_21534314-e402-408c-a819-9b7e73bb832e.xml'
- 'sensors.about\_sensor\_constants'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9c26e305-0d5c-4442-9bcf-a9cdc1778c6b
---

# About Sensor Constants


The Windows Sensor and Location Platform uses constants in a variety of ways. This section describes these constants and their usage.

The platform defines a variety of constants you can use in your sensor driver code. You can also define your own constants. You can find the definitions of platform-defined constants in the file named Sensors.h. For detailed information about platform-defined sensor constants, see [Constants](https://msdn.microsoft.com/library/windows/hardware/ff545409).

### Sensor and Data Organization

The platform organizes sensors and their data in the following ways:

-   *Categories* represent broad classes of sensor devices. Categories provide a way to group sensors that are likely to provide similar types of information, or are otherwise related in some way. Each category is represented by a GUID constant. For example, sensors that report latitude and longitude coordinates belong to the location sensor category, which is representented by the [**SENSOR\_CATEGORY\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/dn265186) constant.

-   *Sensor types* represent specific kinds of sensors. Each sensor type fits into a particular category. Two sensors of different types can belong to the same category or two different categories. Each sensor type is represented by a GUID constant. For example, a global positioning system sensor would be identified by the SENSOR\_TYPE\_LOCATION\_GPS constant, while a sensor that provides the current location using an Internet IP address would be identified by the SENSOR\_TYPE\_LOCATION\_LOOKUP constant. However, both sensors would belong to the location sensor category.

-   *Data types* represent specific kinds of information that the sensor can provide. Sensor data types can contain the actual measurement value, such as altitude, information about the units used to express the data, for example meters, and reference points for the data, for example sea level. Each data type is represented by a **PROPERTYKEY** constant. For example, the data type that represents the x-axis acceleration in g's would be the SENSOR\_DATA\_TYPE\_ACCELERATION\_X\_G constant.

-   When reporting data, a value is said to be contained in a *data field*, and a collection of related data fields comprise a *data report*. Data reports are packaged together by using the [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) interface. Each data report must contain at least one valid data field and a time stamp that identifies when the data report was created. Time stamps are represented by the SENSOR\_DATA\_TYPE\_TIMESTAMP property key.

### Other Constants

Your driver will need to use some other kinds of constants, as well. These constants include:

-   Sensor properties, such as SENSOR\_PROPERTY\_DESCRIPTION. These constants include WPD constants, such as WPD\_FUNCTIONAL\_OBJECT\_CATEGORY. Usually, these constants are used to describe your sensor, such as when called in [**ISensorDriver::OnGetSupportedSensorObjects**](https://msdn.microsoft.com/library/windows/hardware/ff545633). You will also return property values through [**ISensorDriver::OnGetSupportedProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545630) and [**ISensorDriver::OnGetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545610).

-   Some sensor properties are required to be provided by your driver, some properties can be set by client applications, and some must always return the same value. The [**Sensor Properties**](https://msdn.microsoft.com/library/windows/hardware/ff545859) reference section provides this information for each property. To understand which properties are required for a particular method, see the method documentation in the [Windows Sensor Reference](https://msdn.microsoft.com/library/windows/hardware/ff545907) section.

-   [**Event constants**](https://msdn.microsoft.com/library/windows/hardware/ff545463), such as SENSOR\_EVENT\_STATE\_CHANGED. Event constants include GUIDS, which represent types of events, and PROPERTYKEYs, which represent event parameter types. You will use these constants when called by the class extension in [**ISensorDriver::OnGetSupportedEvents**](https://msdn.microsoft.com/library/windows/hardware/ff545623), or when raising events through [**ISensorClassExtension::PostEvent**](https://msdn.microsoft.com/library/windows/hardware/ff545519) or [**ISensorClassExtension::PostStateChange**](https://msdn.microsoft.com/library/windows/hardware/ff545523).

-   Icon constants. Your driver can specify a particular icon to represent the device in Windows. See [Specifying an Icon](specifying-an-icon.md).

### Persistent Unique Identifier

The sensor property named SENSOR\_PROPERTY\_PERSISTENT\_UNIQUE\_ID requires special attention. The value for this property must be unique for each sensor on a device. At the same time, this value must remain consistent for a particular sensor each time the sensor platform uses it. For an example of how to create the persistent unique identifier in your driver code, see [Creating a Persistent Unique Identifier](creating-a-persistent-unique-identifier.md).

### Providing Geolocation Information

Sometimes it is important for users to know the physical location of a sensor, even if the sensor is not a location sensor. For example, the meaning of data that a weather station provides is closely tied to the location of the station.

To provide this type of geolocation data, any sensor can use appropriate data fields from the [**SENSOR\_CATEGORY\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/dn265186) category, even if the sensor is not a location sensor. Thus, a weather station could report its location by using the SENSOR\_DATA\_TYPE\_LATITUDE\_DEGREES and SENSOR\_DATA\_TYPE\_LONGITUDE\_DEGREES data-field constants. However, it is important not to report such sensors as belonging to the Location category, when called in [**ISensorDriver::OnGetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545610).

Windows treats a sensor with any of the location types as existing in the location category (SENSOR\_CATEGORY\_LOCATION). As a result, these sensors fall under the location permissioning model. You should not attempt to bypass the permissioning model for a location sensor (for example, surfacing a GPS sensor type as SENSOR\_TYPE\_LOCATION\_GPS but specifying a non-locaiton category).

### Custom Values

You can define custom values for categories, sensor types, data fields, properties, and events.

For guidelines and an example of how to define custom values for constants, see [Defining Custom Values for Constants](defining-custom-values-for-constants.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20About%20Sensor%20Constants%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




