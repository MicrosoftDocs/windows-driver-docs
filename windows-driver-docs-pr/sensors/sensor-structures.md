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
|[SENSOR_VALUE_PAIR](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_value_pair)|This structure pairs the property keys listed in the Sensor properties section with the data that each key represents.|
|[SENSOR_COLLECTION_LIST](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list)|This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor.|
|[SENSOR_PROPERTY_LIST](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_property_list)|This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor.|
|[SENSOR_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_config)|This structure contains information that the sensor driver passes to the class extension about each sensor.|
|[SENSOR_CONTROLLER_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config)|This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call.|
|SENSOR_DATA|This structure defines a base type that other sensors use to define sensor-specific data types.|
|SENSOR_DEVICE_CAPS|This structure describes the capabilities of a sensor component.|
|SENSOR_DATA_HEADER|This structure contains information about a sensor reading.|
|VEC3D|This structure holds a single data point for 3D positioning data.|
|QUATERNION|This structure is used to represent a 4-dimensional vector used for a simple 3-D rotation operation.|
|MATRIX3X3|This structure is used to represent a generic 3x3 matrix.|






