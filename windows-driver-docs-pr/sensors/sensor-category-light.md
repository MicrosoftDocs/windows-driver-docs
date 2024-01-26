---
title: Sensor_category_light
description: The SENSOR_CATEGORY_LIGHT category contains sensors that provide information about characteristics of light.
keywords: ["SENSOR_CATEGORY_LIGHT Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_LIGHT
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 01/11/2024
ms.topic: reference
---

# SENSOR_CATEGORY_LIGHT

The SENSOR_CATEGORY_LIGHT category contains sensors that provide information about characteristics of light.

## Platform-defined sensor types

This category includes the following platform-defined sensor types.

| Sensor type | Meaning |
|---|---|
| SENSOR_TYPE_AMBIENT_LIGHT | Ambient light sensors |

### Platform-defined data fields

This category includes the following platform-defined data fields.

| Data type | Type | Meaning |
|---|---|---|
| SENSOR_DATA_TYPE_LIGHT_CHROMACITY | **VT_VECTOR\|VT_UI1** | Chromaticity as a counted array of float values.</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, one-byte characters). This data field must contain each value as an IEEE four-byte real value (VT_R4). |
| SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX | **VT_R4** | Illuminance level, in lux.</br></br>Note that device drivers need to also handle this data field with a type of VT_UI4. (This requirement exists for light sensors manufactured before Windows 8.) |
| SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN | **VT_R4** | Color temperature, in kelvin. |

> [!IMPORTANT]
> Each platform-defined light data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR_DATA_TYPE_LIGHT_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Header** | sensors.h |
