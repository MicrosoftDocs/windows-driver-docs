---
title: Relative Orientation Sensor Data Fields
description: This topic provides information about the data fields that are specific to the relative orientation sensor.
ms.date: 01/11/2024
---

# Relative orientation sensor data fields

This topic provides information about the data fields that are specific to the relative orientation sensor.

The following table shows the data fields. For more information about the types shown in the type column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

|Property key|Type|Required/Optional|Description|
|--|--|--|--|
|PKEY_SensorData_Timestamp|VT_FILETIME|Required|Timestamp for sampled data. This is required for each sample that is reported by the sensor driver.|
|PKEY_SensorData_QuaternionW|VT_R4|Required|Real coefficient (as opposed to the imaginary portion of the complex number).|
|PKEY_SensorData_QuaternionX|VT_R4|Required|X-component of rotational axis vector.|
|PKEY_SensorData_QuaternionY|VT_R4|Required|X-component of rotational axis vector.|
|PKEY_SensorData_QuaternionZ|VT_R4|Required|X-component of rotational axis vector.|

## Related topics

- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
