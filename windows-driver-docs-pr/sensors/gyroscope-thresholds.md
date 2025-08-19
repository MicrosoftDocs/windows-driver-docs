---
title: Gyroscope Thresholds
description: This topic provides information about the gyroscope thresholds.
ms.date: 01/11/2024
ms.topic: reference
---

# Gyroscope thresholds

This topic provides information about the gyroscope thresholds.

The following table shows the default thresholds for the gyroscope. For more information about the types shown in the type column, see the [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Default value | Description |
|---|---|---|---|---|
| PKEY_SensorData_AngularVelocityX_DegreesPerSecond | VT_R4 | Required | 0.1f | Minimum amount of change of angular velocity around the x-axis required to reach the threshold, measured in degrees per second. |
| PKEY_SensorData_AngularVelocityY_DegreesPerSecond | VT_R4 | Required | 0.1f | Minimum amount of change of angular velocity around the y-axis required to reach the threshold, measured in degrees per second. |
| PKEY_SensorData_AngularVelocityZ_DegreesPerSecond | VT_R4 | Required | 0.1f | Minimum amount of change of angular velocity around the z-axis required to reach the threshold, measured in degrees per second. |

Gyroscope drivers must report a sample reading to the sensors class extension by calling [SensorsCxSensorDataReady](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensordataready) when either PKEY_SensorData_AngularVelocityX_DegreesPerSecond, PKEY_SensorData_AngularVelocityY_DegreesPerSecond, or PKEY_SensorData_AngularVelocityZ_DegreesPerSecond thresholds are met. Each threshold must be measured per-axis. Drivers must therefore call SensorsCxSensorDataReady whenever the threshold condition is met on any one of the axis.
When PKEY_SensorData_AngularVelocityX_DegreesPerSecond, or PKEY_SensorData_AngularVelocityY_DegreesPerSecond, or PKEY_SensorData_AngularVelocityZ_DegreesPerSecond is set to 0.0f, the driver must report sample readings to the sensors class extension at every interval. This mode is known as *sensor sample streaming*.

Gyroscope drivers must always report one sample reading immediately after the sensors class extension calls the [EvtSensorStart](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) callback irrespective of the threshold values. This sample is known as the known as initial sample reading.

## Related topics

- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
