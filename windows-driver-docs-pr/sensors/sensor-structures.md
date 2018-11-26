---
title: Sensor Structures
description: Sensor Structures
ms.assetid: 94194998-8A56-48D3-9053-007526BF0ED2
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Sensor structures

This section contains information about the sensor structures that provide access to the various properties and features of the sensors.

## In this section

|Topic|Description|
|---|---|
|[SENSOR_VALUE_PAIR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_value_pair)|This structure pairs the property keys listed in the Sensor properties section with the data that each key represents.|
|[SENSOR_COLLECTION_LIST](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list)|This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor.|
|[SENSOR_PROPERTY_LIST](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_property_list)|This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor.|
|[SENSOR_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorscx/ns-sensorscx-_sensor_config)|This structure contains information that the sensor driver passes to the class extension about each sensor.|
|[SENSOR_CONTROLLER_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorscx/ns-sensorscx-_sensor_controller_config)|This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call.|
|SENSOR_DATA|This structure defines a base type that other sensors use to define sensor-specific data types.|
|SENSOR_DEVICE_CAPS|This structure describes the capabilities of a sensor component.|
|SENSOR_DATA_HEADER|This structure contains information about a sensor reading.|
|VEC3D|This structure holds a single data point for 3D positioning data.|
|QUATERNION|This structure is used to represent a 4-dimensional vector used for a simple 3-D rotation operation.|
|MATRIX3X3|This structure is used to represent a generic 3x3 matrix.|

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors/sensors%5D:%20Sensor%20Structures%20%20RELEASE:%20%282/19/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




