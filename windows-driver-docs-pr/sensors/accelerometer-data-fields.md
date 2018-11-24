---
title: Accelerometer data fields
description: This topic provides information about the data fields that are specific to the accelerometer.
ms.assetid: 88333B6A-E262-4937-9349-156B00BA8CC4
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Accelerometer data fields


This topic provides information about the data fields that are specific to the accelerometer.

The following table shows the data fields. For more information about the types shown in the type column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

|Property key|Type|Required/Optional|Description|
| --- | --- | --- | --- |
|PKEY_SensorData_AccelerationX_Gs|VT_R4|Required|The x-axis acceleration in g’s.|
|PKEY_SensorData_AccelerationY_Gs|VT_R4|Required|The y-axis acceleration in g’s.|
|PKEY_SensorData_AccelerationZ_G|VT_R4|Required|The z-axis acceleration in g’s.|
|PKEY_SensorData_Shake|VT_BOOL|Optional|An indication that a shake has been detected by the accelerometer. This must be true if the data field is sent up.|

 

## Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






