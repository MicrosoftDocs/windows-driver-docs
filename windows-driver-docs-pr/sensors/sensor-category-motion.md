---
title: SENSOR_CATEGORY_MOTION
description: The SENSOR_CATEGORY_MOTION category contains sensors that provide information that is related to physical movement.
keywords: ["SENSOR_CATEGORY_MOTION Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_MOTION
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 03/02/2023
ms.topic: reference
---

# SENSOR_CATEGORY_MOTION

The SENSOR_CATEGORY_MOTION category contains sensors that provide information that is related to physical movement. Accelerometers measure acceleration of the sensor, including gravitational acceleration. Motion detectors, such as human movement detection in a security system, sense moving objects. Gyrometers sense changes in angular velocity. Speedometers measure velocity.

## Platform-defined Sensor Types

This category includes the following platform-defined sensor types.

| Sensor type | Meaning |
|---|---|
| SENSOR_TYPE_ACCELEROMETER_1D | One-axis accelerometers. |
| SENSOR_TYPE_ACCELEROMETER_2D | Two-axis accelerometers. |
| SENSOR_TYPE_ACCELEROMETER_3D | Three-axis accelerometers. |
| SENSOR_TYPE_GYROMETER_1D | One-axis gyrometers. |
| SENSOR_TYPE_GYROMETER_2D | Two-axis gyrometers. |
| SENSOR_TYPE_GYROMETER_3D | Three-axis gyrometers. |
| SENSOR_TYPE_MOTION_DETECTOR | Motion detectors, such as those used in security systems. |
| SENSOR_TYPE_SPEEDOMETER | Rate-of-motion sensors. |

## Platform-defined Data Fields

This category includes the following platform-defined data fields.

| Data type | Type | Meaning |
|---|---|---|
| SENSOR_DATA_TYPE_ACCELERATION_X_G | **VT_R8** | X-axis acceleration, in gs. |
| SENSOR_DATA_TYPE_ACCELERATION_Y_G | **VT_R8** | Y-axis acceleration, in gs. |
| SENSOR_DATA_TYPE_ACCELERATION_Z_G | **VT_R8** | Z-axis acceleration, in gs. |
| SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND | **VT_R8** | Gyrometric x-axis acceleration, in degrees per second. squared. |
| SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND | **VT_R8** | Gyrometric y-axis acceleration, in degrees per second squared. |
| SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND | **VT_R8** | Gyrometric z-axis acceleration, in degrees per second squared. |
| SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND | **VT_R8** | Gyrometric x-axis velocity, in degrees per second. |
| SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND | **VT_R8** | Gyrometric y-axis velocity, in degrees per second. |
| SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND | **VT_R8** | Gyrometric z-axis velocity, in degrees per second. |
| SENSOR_DATA_TYPE_MOTION_STATE | **VT_BOOL** | **VARIANT_TRUE** if motion is detected, otherwise **VARIANT_FALSE**. |
| SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND | **VT_R8** | Speed in meters per second. |

> [!IMPORTANT]
> Each platform-defined motion data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR_DATA_TYPE_MOTION_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Header** | sensors.h |
