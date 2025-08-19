---
title: Accelerometer Thresholds
description: This topic provides information about the accelerometer thresholds.
ms.date: 01/11/2024
ms.topic: reference
---

# Accelerometer thresholds

This topic provides information about the accelerometer thresholds.

The following table lists the available thresholds values for the accelerometer. For more information about the types shown in the type column, see the [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

|Property key|Type|Required/Optional|Default value|Description|
|---|---|---|---|---|
|PKEY_SensorData_AccelerationX_Gs|VT_R4|Required|0.1f|Minimum amount of acceleration increase or decrease along the x-axis required to reach the threshold, measured in g's.|
|PKEY_SensorData_AccelerationY_Gs|VT_R4|Required|0.1f|Minimum amount of acceleration increase or decrease along the y-axis required to reach the threshold, measured in g's.|
|PKEY_SensorData_AccelerationZ_Gs|VT_R4|Required|0.1f|Minimum amount of acceleration increase or decrease along the z-axis required to reach the threshold, measured in g's.|

Accelerometer drivers must report a sample reading to the sensors class extension by calling [SensorsCxSensorDataReady](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensordataready) when either PKEY_SensorData_AccelerationX_Gs, PKEY_SensorData_AccelerationY_Gs, or PKEY_SensorData_AccelerationZ_Gs thresholds are met. Each threshold must be measured per-axis. Drivers must therefore call SensorsCxSensorDataReady whenever the threshold condition is met on any one of the axis.
When PKEY_SensorData_AccelerationX_Gs, or PKEY_SensorData_AccelerationY_Gs, or PKEY_SensorData_AccelerationZ_Gs is set to 0.0f, the driver must report sample readings to the sensors class extension at every single interval. This mode is known as *sensor sample streaming*.

Accelerometer drivers must always report one sample reading immediately after the sensors class extension calls the [EvtSensorStart](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) callback irrespective of the threshold values. This sample is known as the known as *initial sample reading*.

>[!NOTE]
>The accelerometer driver must also report a sample reading to the sensor class extension when the PKEY_SensorData_Shake data field changes (if supported), irrespective of the thresholds being set.

## Related topics

- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
