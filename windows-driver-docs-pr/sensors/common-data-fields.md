---
title: Common data fields
description: This topic shows the common data fields that are included in all sensor-specific data fields.
ms.date: 03/02/2023
ms.topic: reference
---

# Sensor data fields

*Sensor data fields* represent specific kinds of information that a sensor can provide. When reporting data, a value is said to be contained in a *data field*. A collection of related data fields comprise a *data report*. Data reports are packaged together within a SENSOR_COLLECTION_LIST structure. Each data report must contain at least one valid data field and a time stamp that identifies when the data report was created. Time stamps are represented by the PKEY_SensorData_Timestamp property key. Examples of data fields are the x, y, z acceleration values for an accelerometer. Each data field is identified by a **PROPERTYKEY** constant.

## Common data fields

The field type below is included in all sensor-specific data fields.

Clients can use the ReadFile function to retrieve information from these data fields.

For more information about the types shown in the type column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Description |
|---|---|---|---|
| PKEY_SensorData_Timestamp | VT_FILETIME | Required | The file time computed by the driver in UTC format. The class extension (CX) provides a helper function to convert ticks from boot to FILETIME so that remote systems don't have to synchronize to the system clock. |

## Related topics

- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
