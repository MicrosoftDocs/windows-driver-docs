---
title: Orientation sensor thresholds
description: This topic provides information about the orientation sensor thresholds.
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Orientation sensor thresholds


This topic provides information about the orientation sensor thresholds.

The following table shows the available thresholds values for the orientation sensor. For more information about the types shown in the type column, see the [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

|Property key|Type|Required/Optional|Default value|Description|
|---|---|---|---|---|
|PKEY_SensorData_RotationAngle_Degrees|VT_R4|Required|10.0f|Minimum amount of orientation angle change around any axis required to reach the threshold, measured in degrees. This value should be calculated as the angle between two quaternions. Mathematically, this  expressed as: 2*cos-1 (dot product(q1, q2))|
|PKEY_SensorData_LinearAccelerationX_Gs|VT_R4|Optional|n/a|Minimum amount of acceleration increase or decrease along the x-axis required to reach the threshold, measured in g’s.|
|PKEY_SensorData_LinearAccelerationY_Gs|VT_R4|Optional|n/a|Minimum amount of acceleration increase or decrease along the y-axis required to reach the threshold, measured in g’s.|
|PKEY_SensorData_LinearAccelerationZ_Gs|VT_R4|Optional|n/a|Minimum amount of acceleration increase or decrease along the z-axis required to reach the threshold, measured in g’s.|
|PKEY_SensorData_CorrectedAngularVelocityX_DegreesPerSecond|VT_R4|Optional|n/a|Minimum amount of change of angular velocity around the x-axis required to reach the threshold, measured in degrees per second.|
|PKEY_SensorData_CorrectedAngularVelocityY_DegreesPerSecond|VT_R4|Optional|n/a|Minimum amount of change of angular velocity around the x-axis required to reach the threshold, measured in degrees per second.|
|PKEY_SensorData_CorrectedAngularVelocityZ_DegreesPerSecond|VT_R4|Optional|n/a|Minimum amount of change of angular velocity around the x-axis required to reach the threshold, measured in degrees per second.|

Orientation sensor drivers must report a sample reading to the sensors class extension by calling [SensorsCxSensorDataReady](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensordataready) when the PKEY_SensorData_RotationAngle_Degrees threshold is met.

When PKEY_SensorData_RotationAngle_Degrees is set to 0.0f, the driver must report sample readings to the sensors class extension at every interval. This mode is known as *sensor sample streaming*.

Orientation sensor drivers must always report one sample reading immediately after the sensors class extension calls the [EvtSensorStart](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) callback irrespective of the threshold values. This sample is known as the known as *initial sample reading*.

Orientation sensor drivers must report a sample reading to the sensors class extension when the respective thresholds are met.

If the driver supports any of the following additional optional datafields that measure readings per axis then, threshold for the corresponding axis must be exposed:
* PKEY_SensorData_LinearAccelerationX_Gs
* PKEY_SensorData_LinearAccelerationY_Gs
* PKEY_SensorData_LinearAccelerationZ_Gs
* PKEY_SensorData_CorrectedAngularVelocityX_DegreesPerSecond
* PKEY_SensorData_CorrectedAngularVelocityY_DegreesPerSecond
* PKEY_SensorData_CorrectedAngularVelocityZ_DegreesPerSecond

Drivers must therefore call SensorsCxSensorDataReady whenever the threshold condition is met on any one of the axis.

## Related topics


[PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
