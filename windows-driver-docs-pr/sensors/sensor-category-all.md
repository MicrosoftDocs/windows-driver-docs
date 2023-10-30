---
title: SENSOR_CATEGORY_ALL
description: The SENSOR_CATEGORY_ALL category represents the set of all platform-defined sensor categories.
keywords: SENSOR_CATEGORY_ALL Sensor Devices
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_ALL
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 03/02/2023
ms.topic: reference
---

# SENSOR_CATEGORY_ALL

The SENSOR_CATEGORY_ALL category represents the set of all platform-defined sensor categories.

## Platform-defined Property Keys

This category includes the following platform-defined data fields.

| Data type | Type | Meaning |
|---|---|---|
| SENSOR_DATA_TYPE_TIMESTAMP | VT_FILETIME | Required for all data reports. Marks each data report with the time the data report was created. Use Universal Coordinated Time (UTC). |

> [!IMPORTANT]
> Each platform-defined common data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR_DATA_TYPE_COMMON_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Version** | Available in Windows 7 |
| **Header** | Sensors.h |
