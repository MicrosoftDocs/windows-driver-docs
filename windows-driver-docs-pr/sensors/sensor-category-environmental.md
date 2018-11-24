---
title: SENSOR\_CATEGORY\_ENVIRONMENTAL
description: The SENSOR\_CATEGORY\_ENVIRONMENTAL category contains sensors that provide information about the surrounding environment or weather.
ms.assetid: 49839092-0792-4e89-bc3a-7defc4730937
keywords: ["SENSOR_CATEGORY_ENVIRONMENTAL Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_ENVIRONMENTAL
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# SENSOR\_CATEGORY\_ENVIRONMENTAL


The SENSOR\_CATEGORY\_ENVIRONMENTAL category contains sensors that provide information about the surrounding environment or weather.

### Platform-defined Sensor Types

This category includes the following platform-defined sensor types.

|Sensor type|Meaning|
|--|--|
|SENSOR_TYPE_ENVIRONMENTAL_ATMOSPHERIC_PRESSURE|Barometers.|
|SENSOR_TYPE_ENVIRONMENTAL_HUMIDITY|Hygrometers.|
|SENSOR_TYPE_ENVIRONMENTAL_TEMPERATURE|Thermometers.|
|SENSOR_TYPE_ENVIRONMENTAL_WIND_DIRECTION|Weather vanes.|
|SENSOR_TYPE_ENVIRONMENTAL_WIND_SPEED|Anemometers.|

 

### Platform-defined Data Fields

This category includes the following platform-defined data fields.

|Data type|Type|Meaning|
|--|--|--|
|SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR|VT_R4|Atmospheric pressure in atmospheres (bars).|
|SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS|VT_R4|Temperature in degrees Celsius.|
|SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT|VT_R4|Relative humidity as a percentage.|
|SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE|VT_R4|Wind direction relative to magnetic north, in degrees. North is represented as 0.0 (top of the x-axis), with values increasing in an anticlockwise rotation. The z-axis points upwards.|
|SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND|VT_R4|Wind speed in meters per second.|

 

>[!IMPORTANT]
> Each platform-defined environmental data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR\_DATA\_TYPE\_ENVIRONMENTAL\_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

 

## Requirements


| | |
|--|--|
|Minimum supported client|Windows 7|
|Minimum supported server|None supported|
|Version|Available in Windows 7.|
|Header|Sensors.h|


 

 





