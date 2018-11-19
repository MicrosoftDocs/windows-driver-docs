---
title: Sensor Constants
description: Sensor Constants
ms.assetid: F3ED56C2-56AF-44FA-9ED8-7A16F1711AC7
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Sensor constants


The Windows Universal Sensor uses constants in a variety of ways. This section describes these constants and their usage.

The platform defines a variety of constants you can use in your universal sensor driver code. You can also define your own constants. You can find the definitions of platform-defined constants in the Sensorsdef.h file.

## Sensor and data organization

The platform organizes sensors and their data in the following ways:

-   [Sensor types](sensor-types.md) represent specific kinds of sensors. Each sensor type can optionally fit into a particular category.

-   [Sensor Data Fields](sensor-data-fields.md) represent specific kinds of information that the sensor can provide. When reporting data, a value is said to be contained in a *data field*, and a collection of related data fields comprise a *data report*. Each data field is identified by a **PROPERTYKEY** constant.

-   [Sensor thresholds](sensor-thresholds-v2.md) represent properties to configure sensor data filtering. Sensor hardware or drivers only report sensor samples to the sensor class extension when the threshold conditions are met or exceeded.

-   [Sensor Properties](sensor-properties2.md) contain data that characterize the driver that is installed on the Windows device.

-   [Sensor Categories](sensor-categories.md) represent broad classes of sensor devices. Categories provide a way to group sensors that are likely to provide similar types of information, or are otherwise related in some way. Each category is represented by a GUID constant. Two sensors of different types can belong to the same category or two different categories. Each sensor type is represented by a GUID constant. For example, an accelerometer and a gyroscope may both be classified under the GUID_SensorCategory_Motion category, while an abient light sensor may be classified under the GUID_SensorCategory_Light category.


## Other constants

Your driver may need to use other kinds of constants, such as icon constants. Your driver can specify a particular icon to represent the device in Windows. See [Specifying an Icon](specifying-an-icon.md).


## Persistent unique identifier

The sensor property named DEVPKEY_Sensor_PersistentUniqueId requires special attention. The value for this property must be unique for each sensor on a device. At the same time, this value must remain consistent for a particular sensor each time the sensor platform uses it. For an example of how to create the persistent unique identifier in your driver code, see [Creating a Persistent Unique Identifier](creating-a-persistent-unique-identifier-v2.md).

### Custom values

You can define custom values for categories, sensor types, data fields, and properties

For guidelines and an example of how to define custom values for constants, see [Defining Custom Values for Constants](defining-custom-values-for-constants-v2.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors/sensors%5D:%20About%20Sensor%20Constants%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


