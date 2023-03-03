---
title: SENSOR_CATEGORY_SCANNER
description: The SENSOR_CATEGORY_SCANNER category contains sensors that provide information that is obtained by scanning.
keywords: ["SENSOR_CATEGORY_SCANNER Sensor Devices"]
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_SCANNER
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 03/02/2023
ms.topic: reference
---

# SENSOR_CATEGORY_SCANNER

The SENSOR_CATEGORY_SCANNER category contains sensors that provide information that is obtained by scanning.

## Platform-defined sensor types

This category includes the following platform-defined sensor types.

| Sensor type | Meaning |
|---|---|
| SENSOR_TYPE_BARCODE_SCANNER | Sensors that use optical scanning to read bar codes. |
| SENSOR_TYPE_RFID_SCANNER | Radio-frequency ID scanning sensors. |

## Platform-defined data fields

This category includes the following platform-defined data fields.

| Data type | Type | Meaning |
|---|---|---|
| SENSOR_DATA_TYPE_RFID_TAG_40_BIT | **VT_UI8** | 40-bit radio frequency ID tag value. |

> [!IMPORTANT]
> Each platform-defined scanner data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR_DATA_TYPE_SCANNER_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Header** | sensors.h |
