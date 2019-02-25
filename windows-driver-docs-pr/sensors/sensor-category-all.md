---
title: SENSOR\_CATEGORY\_ALL
description: The SENSOR\_CATEGORY\_ALL category represents the set of all platform-defined sensor categories.
ms.assetid: 9a4524d2-055c-46e0-9650-66e6f2872fbc
keywords: SENSOR_CATEGORY_ALL Sensor Devices
topic_type:
- apiref
api_name:
- SENSOR_CATEGORY_ALL
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# SENSOR\_CATEGORY\_ALL


The SENSOR\_CATEGORY\_ALL category represents the set of all platform-defined sensor categories.

## Platform-defined Property Keys

This category includes the following platform-defined data fields.

|Data type|Type|Meaning|
|--|--|--|
|SENSOR_DATA_TYPE_TIMESTAMP|VT_FILETIME|Required for all data reports. Marks each data report with the time the data report was created. Use Universal Coordinated Time (UTC).|
 

>[!IMPORTANT]
> Each platform-defined common data type **PROPERTYKEY** is based on a common **GUID** that is named SENSOR\_DATA\_TYPE\_COMMON\_GUID. As it is a reserved base value, do not use this **GUID** to define your own property keys.

 

## Requirements

| | |
|--|--|
|Minimum supported client|Windows 7|
|Minimum supported server|None supported|
|Version|Available in Windows 7.|
|Header|Sensors.h|
 

 





