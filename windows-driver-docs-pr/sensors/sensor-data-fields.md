---
title: Sensor data fields
description: The sensor driver sets data fields that can be read by applications, using the ReadFile function to get information about the sensor driver.
ms.assetid: E430AC59-34AC-4F8E-9A42-350C7A42BBA8
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Sensor data fields

*Sensor data fields* represent specific kinds of information that a sensor can provide. When reporting data, a value is said to be contained in a *data field*. A collection of related data fields comprise a *data report*. Data reports are packaged together within a SENSOR_COLLECTION_LIST structure. Each data report must contain at least one valid data field and a time stamp that identifies when the data report was created. Time stamps are represented by the PKEY_SensorData_Timestamp property key. Examples of data fields are the x, y, z acceleration values for an accelerometer. Each data field is identified by a **PROPERTYKEY** constant.

## In this section

|Topic|Description|
|---|---|
|[Common data fields](common-data-fields.md)|This topic shows the common data fields that are included in all sensor-specific data fields.|
|[Accelerometer data fields](accelerometer-data-fields.md)|This topic provides information about the data fields that are specific to the accelerometer.|
|[Linear accelerometer data fields](linear-accelerometer-data-fields.md)|This topic provides information about the data fields that are specific to the linear accelerometer.|
|[Magnetometer data fields](magnetometer-data-fields.md)|This topic provides information about the data fields that are specific to the magnetometer.|
|[Geomagnetic Orientation](geomagnetic-orientation.md)|>This topic provides information about the data fields that are specific to the geomagnetic orientation sensor.|
|[Gravity vector data fields](gravity-vector-data-fields.md)|>This topic provides information about the data fields that are specific to the gravity vector.|
|[Gyroscope data fields](gyroscope-data-fields.md)|This topic provides information about the data fields that are specific to the gyroscope.|
|[Light sensor data fields](light-sensor-data-fields.md)|This topic provides information about the data fields that are specific to the light sensor.|
|[Orientation sensor data fields](device-orientation-sensor-data-fields.md)|This topic provides information about the data fields that are specific to the device orientation sensor.|
|[Proximity sensor data fields](proximity-sensor-data-fields.md)|This topic provides information about the data fields that are specific to the proximity sensor.|
|[Barometer data fields](barometer-sensor-data-fields.md)|This topic provides information about the data fields that are specific to the barometer sensor.|
|[Simple device orientation sensor data fields](simple-device-orientation-sensor-data-fields.md)|This topic provides information about the data fields that are specific to the simple device orientation sensor.|
|[Activity detection sensor data fields](activity-detection-sensor-data-fields.md)|This topic provides information about the data fields that are specific to the activity detection sensor.|
|[Pedometer data fields](pedometer-data-fields.md)|This topic provides information about the data fields that are specific to the pedometer.|
|[Relative orientation sensor data fields](relative-orientation-data-fields.md)|This topic provides information about the data fields that are specific to the relative orientation sensor.|
|[Custom sensor data fields](custom-sensor-data-fields.md)|This topic provides information about the data fields that can be used by a custom sensor.|

 

 

 





