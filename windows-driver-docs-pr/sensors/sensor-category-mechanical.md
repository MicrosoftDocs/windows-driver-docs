---
title: Sensor_category_mechanical
description: The SENSOR_CATEGORY_MECHANICAL category contains sensors that provide information related to mechanisms.
keywords: ["SENSOR_CATEGORY_MECHANICAL Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_MECHANICAL
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 01/11/2024
ms.topic: reference
---

# SENSOR_CATEGORY_MECHANICAL

The SENSOR_CATEGORY_MECHANICAL category contains sensors that provide information related to mechanisms.

## Platform-defined sensor types

This category includes the following platform-defined sensor types.

| Sensor type | Meaning |
|---|---|
| SENSOR_TYPE_BOOLEAN_SWITCH | Two-state switches (off or on). |
| SENSOR_TYPE_FORCE | Force sensors. |
| SENSOR_TYPE_MULTIVALUE_SWITCH | Multiple-position switches. |
| SENSOR_TYPE_PRESSURE | Pressure sensors. |
| SENSOR_TYPE_SCALE | Weight sensors. |
| SENSOR_TYPE_STRAIN | Strain sensors. |

## Platform-defined data fields

This category includes the following platform-defined data fields.

| Data type | Type | Meaning |
|---|---|---|
| SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL | **VT_R8** | Absolute pressure, in pascals. |
| SENSOR_DATA_TYPE_BOOL**EAN_SWITCH_STATE | **VT_BOOL** | State field for SENSOR_TYPE_BOOL**EAN_SWITCH. |
| SENSOR_DATA_TYPE_FORCE_NEWTONS | **VT_R8** | Force, in newtons. |
| SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL | **VT_R8** | Relative gauge pressure, in pascals. |
| SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE | **VT_R8** | State field for SENSOR_TYPE_MULTIVALUE_SWITCH. |
| SENSOR_DATA_TYPE_STRAIN | **VT_R8** | Strain. |
| SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS | **VT_R8** | Weight, in kilograms. |

> [!IMPORTANT]
> Each platform-defined mechanical data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR_DATA_TYPE_MECHANICAL_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Header** | sensors.h |
