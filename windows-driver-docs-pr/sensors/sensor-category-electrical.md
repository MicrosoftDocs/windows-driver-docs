---
title: Sensor_category_electrical
description: The SENSOR_CATEGORY_ELECTRICAL category contains sensors that provide information about electrical systems.
keywords: ["SENSOR_CATEGORY_ELECTRICAL Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_ELECTRICAL
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 01/11/2024
ms.topic: reference
---

# SENSOR_CATEGORY_ELECTRICAL

The SENSOR_CATEGORY_ELECTRICAL category contains sensors that provide information about electrical systems.

## Platform-defined Sensor Types

This category includes the following platform-defined sensor types.

| Sensor type | Meaning |
|---|---|
| SENSOR_TYPE_CAPACITANCE | Capacitance sensors |
| SENSOR_TYPE_CURRENT | Current sensors |
| SENSOR_TYPE_ELECTRICAL_POWER | Electrical power sensors |
| SENSOR_TYPE_INDUCTANCE | Inductance sensors |
| SENSOR_TYPE_POTENTIOMETER | Potentiometers |
| SENSOR_TYPE_RESISTANCE | Resistance sensors |
| SENSOR_TYPE_VOLTAGE | Voltage sensors |

## Platform-defined Data Fields

This category includes the following platform-defined data fields.

| Data type | Type | Meaning |
|---|---|---|
| SENSOR_DATA_TYPE_CAPACITANCE_FARAD | VT_R8 | Capacitance in farads |
| SENSOR_DATA_TYPE_CURRENT_AMPS | VT_R8 | Current in amperes |
| SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS | VT_R8 | Electrical power in watts |
| SENSOR_DATA_TYPE_INDUCTANCE_HENRY | VT_R8 | Inductance in henries |
| SENSOR_DATA_TYPE_RESISTANCE_OHMS | VT_R8 | Resistance in ohms |
| SENSOR_DATA_TYPE_VOLTAGE_VOLTS | VT_R8 | Electrical potential in volts |

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Version** | Available in Windows 7 |
| **Header** | Sensors.h |
