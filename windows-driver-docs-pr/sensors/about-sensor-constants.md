---
title: About Sensor Constants
description: About Sensor Constants
ms.assetid: 9c26e305-0d5c-4442-9bcf-a9cdc1778c6b
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# About Sensor constants


The Windows Sensor and Location Platform uses constants in a variety of ways. This section describes these constants and their usage.

The platform defines a variety of constants you can use in your sensor driver code. You can also define your own constants. You can find the definitions of platform-defined constants in the files Sensors.h and Sensorsdef.h.

## Sensor and data organization

The platform organizes sensors and their data in the following ways:

-   *Categories* represent broad classes of sensor devices. Categories provide a way to group sensors that are likely to provide similar types of information, or are otherwise related in some way. Each category is represented by a GUID constant. For example, sensors that report latitude and longitude coordinates belong to the location sensor category, which is represented by the [**SENSOR\_CATEGORY\_LOCATION**](sensor-category-loc.md) constant.

-   *Sensor types* represent specific kinds of sensors. Each sensor type fits into a particular category. Two sensors of different types can belong to the same category or two different categories. Each sensor type is represented by a GUID constant. For example, a global positioning system sensor would be identified by the SENSOR\_TYPE\_LOCATION\_GPS constant, while a sensor that provides the current location using an Internet IP address would be identified by the SENSOR\_TYPE\_LOCATION\_LOOKUP constant. However, both sensors would belong to the location sensor category.

-   *Data types* represent specific kinds of information that the sensor can provide. Sensor data types can contain the actual measurement value, such as altitude, information about the units used to express the data, for example meters, and reference points for the data, for example sea level. Each data type is represented by a **PROPERTYKEY** constant. For example, the data type that represents the x-axis acceleration in g's would be the SENSOR\_DATA\_TYPE\_ACCELERATION\_X\_G constant.

-   When reporting data, a value is said to be contained in a *data field*, and a collection of related data fields comprise a *data report*. Data reports are packaged together by using the [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) interface. Each data report must contain at least one valid data field and a time stamp that identifies when the data report was created. Time stamps are represented by the SENSOR\_DATA\_TYPE\_TIMESTAMP property key.


## Other constants

Your driver will need to use some other kinds of constants, as well. These constants include:

-   Sensor properties, such as SENSOR\_PROPERTY\_DESCRIPTION. These constants include WPD constants, such as WPD\_FUNCTIONAL\_OBJECT\_CATEGORY. Usually, these constants are used to describe your sensor, such as when called in [**ISensorDriver::OnGetSupportedSensorObjects**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedsensorobjects). You will also return property values through [**ISensorDriver::OnGetSupportedProperties**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedproperties) and [**ISensorDriver::OnGetProperties**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetproperties).

-   Some sensor properties are required to be provided by your driver, some properties can be set by client applications, and some must always return the same value. The [**Sensor Properties**](sensor-properties.md) reference section provides this information for each property. To understand which properties are required for a particular method, see the method documentation in the [Windows Sensor Reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_sensors/#functions) section.

-   [**Event constants**](about-sensor-driver-events.md), such as SENSOR\_EVENT\_STATE\_CHANGED. Event constants include GUIDS, which represent types of events, and PROPERTYKEYs, which represent event parameter types. You will use these constants when called by the class extension in [**ISensorDriver::OnGetSupportedEvents**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedevents), or when raising events through [**ISensorClassExtension::PostEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-postevent) or [**ISensorClassExtension::PostStateChange**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-poststatechange).

-   Icon constants. Your driver can specify a particular icon to represent the device in Windows. See [Specifying an Icon](specifying-an-icon.md).

-   The sensor platform defines the GUID_DEVINTERFACE_SENSOR constant, to identify the sensor device interface class. During its installation, a driver registers for at least one device interface class. The sensor class extension registers the sensor device interface class for you.



## Persistent unique identifier

The sensor property named SENSOR\_PROPERTY\_PERSISTENT\_UNIQUE\_ID requires special attention. The value for this property must be unique for each sensor on a device. At the same time, this value must remain consistent for a particular sensor each time the sensor platform uses it. For an example of how to create the persistent unique identifier in your driver code, see [Creating a Persistent Unique Identifier](creating-a-persistent-unique-identifier.md).

## Providing geolocation information

Sometimes it is important for users to know the physical location of a sensor, even if the sensor is not a location sensor. For example, the meaning of data that a weather station provides is closely tied to the location of the station.

To provide this type of geolocation data, any sensor can use appropriate data fields from the [**SENSOR\_CATEGORY\_LOCATION**](sensor-category-loc.md) category, even if the sensor is not a location sensor. Thus, a weather station could report its location by using the SENSOR\_DATA\_TYPE\_LATITUDE\_DEGREES and SENSOR\_DATA\_TYPE\_LONGITUDE\_DEGREES data-field constants. However, it is important not to report such sensors as belonging to the Location category, when called in [**ISensorDriver::OnGetProperties**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetproperties).

Windows treats a sensor with any of the location types as existing in the location category (SENSOR\_CATEGORY\_LOCATION). As a result, these sensors fall under the location permission model. You should not attempt to bypass the permission model for a location sensor (for example, surfacing a GPS sensor type as SENSOR\_TYPE\_LOCATION\_GPS but specifying a non-location category).

## Custom values

You can define custom values for categories, sensor types, data fields, properties, and events.

For guidelines and an example of how to define custom values for constants, see [Defining Custom Values for Constants](defining-custom-values-for-constants.md).

 

 




