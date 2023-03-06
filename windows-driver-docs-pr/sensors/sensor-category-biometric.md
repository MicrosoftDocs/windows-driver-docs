---
title: SENSOR_CATEGORY_BIOMETRIC
description: The SENSOR_CATEGORY_BIOMETRIC category contains sensors that provide information about living beings.
keywords: ["SENSOR_CATEGORY_BIOMETRIC Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_BIOMETRIC
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 03/02/2023
ms.topic: reference
---

# SENSOR_CATEGORY_BIOMETRIC

The SENSOR_CATEGORY_BIOMETRIC category contains sensors that provide information about living beings.

## Platform-defined Sensor Types

This category includes the following platform-defined sensor types.

| Sensor type | Meaning |
|---|---|
| SENSOR_TYPE_HUMAN_PRESENCE | Sensors that detect human presence |
| SENSOR_TYPE_HUMAN_PROXIMITY | Sensors that detect human proximity |
| SENSOR_TYPE_TOUCH | Touch sensors |

### Platform-defined Data Fields

This category includes the following platform-defined data fields.

| Data type | Type | Meaning |
|---|---|---|
| SENSOR_DATA_TYPE_HUMAN_PRESENCE | VT_BOOL | VARIANT_TRUE when a human is using the computer. |
| SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS | VT_R4 | Distance between a human and the computer, in meters. |
| SENSOR_DATA_TYPE_TOUCH_STATE | VT_BOOL | VARIANT_TRUE when the touch sensor is being touched, otherwise VARIANT_FALSE. |

> [!IMPORTANT]
> Each platform-defined biometric data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR_DATA_TYPE_BIOMETRIC_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Version** | Available in Windows 7 |
| **Header** | Sensors.h |
