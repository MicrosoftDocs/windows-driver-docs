---
title: Relative orientation sensor data fields
description: This topic provides information about the data fields that are specific to the relative orientation sensor.
ms.assetid: A48B75DD-5424-48CC-AC8B-251874414FCE
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Relative orientation sensor data fields


This topic provides information about the data fields that are specific to the relative orientation sensor.

The following table shows the data fields. For more information about the types shown in the type column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

|Property key|Type|Required/Optional|Description|
|--|--|--|--|
|PKEY_SensorData_Timestamp|VT_FILETIME|Required|Timestamp for sampled data. This is required for each sample that is reported by the sensor driver.|
|PKEY_SensorData_QuaternionW|VT_R4|Required|Real coefficient (as opposed to the imaginary portion of the complex number).|
|PKEY_SensorData_QuaternionX|VT_R4|Required|X-component of rotational axis vector.|
|PKEY_SensorData_QuaternionY|VT_R4|Required|X-component of rotational axis vector.|
|PKEY_SensorData_QuaternionZ|VT_R4|Required|X-component of rotational axis vector.|

 

## Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






