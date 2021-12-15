---
title: Magnetometer thresholds
description: This topic provides information about the magnetometer thresholds.
ms.date: 07/20/2018
---

# Magnetometer thresholds


This topic provides information about the magnetometer thresholds.

The following table shows the available thresholds values for the magnetometer. For more information about the types shown in the type column, see the [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

|Property key|Type|Required/Optional|Default value|Description|
|---|---|---|---|---|
|PKEY_SensorData_MagneticFieldStrengthX_Microteslas|VT_R4|Required|5.0f|Minimum amount of magnetic field change along the x-axis required to reach the threshold, measured in microteslas.|
|PKEY_SensorData_MagneticFieldStrengthY_Microteslas|VT_R4|Required|5.0f|Minimum amount of magnetic field change along the y-axis required to reach the threshold, measured in microteslas.|
|PKEY_SensorData_MagneticFieldStrengthZ_Microteslas|VT_R4|Required|5.0f|Minimum amount of magnetic field change along the z-axis required to reach the threshold, measured in microteslas.|

Magnetometer drivers must report a sample reading to the sensors class extension by calling [SensorsCxSensorDataReady](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensordataready) when either PKEY_SensorData_MagneticFieldStrengthX_Microteslas, PKEY_SensorData_MagneticFieldStrengthY_Microteslas, or PKEY_SensorData_MagneticFieldStrengthZ_Microteslas thresholds are met. Each threshold must be measured per-axis. Drivers must therefore call SensorsCxSensorDataReady whenever the threshold condition is met on any one of the axis.
When PKEY_SensorData_MagneticFieldStrengthX_Microteslas, or PKEY_SensorData_MagneticFieldStrengthY_Microteslas, or PKEY_SensorData_MagneticFieldStrengthZ_Microteslas is set to 0.0f, the driver must report sample readings to the sensors class extension at every interval. This mode is known as *sensor sample streaming*.

Magnetometer drivers must always report one sample reading immediately after the sensors class extension calls the [EvtSensorStart](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) callback irrespective of the threshold values. This sample is known as the known as *initial sample reading*.

## Related topics


[PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
