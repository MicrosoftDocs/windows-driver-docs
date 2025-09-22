---
title: Hinge Angle Sensor Thresholds
description: This topic provides information about the hinge angle sensor thresholds.
ms.date: 09/22/2025
ms.topic: reference
---

# Hingle angle thresholds

This topic provides information about the hinge angle sensor thresholds.

The following table lists the available thresholds values for the hinge angle sensor. For more information about the types shown in the type column, see the [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

|Property key|Type|Required/Optional|Default value|Description|
|---|---|---|---|---|
|PKEY_SensorData_HingeAngle|VT_R4|Required|10.0f|The minimum change in the interior hinge angle between two panels in a system required to reach the threshold, measured in degrees.|

Hinge angle sensor drivers must report a sample reading to the sensors class extension by calling [SensorsCxSensorDataReady](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensordataready) when PKEY_SensorData_HingeAngle threshold is met.

When PKEY_SensorData_HingeAngle is set to 0.0f, the driver must report sample readings to the sensors class extension at every interval. This mode is known as *sensor sample streaming*.

Hinge angle sensor drivers must always report one sample reading immediately after the sensors class extension calls the [EvtSensorStart](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) callback irrespective of the threshold values. This sample is known as the known as *initial sample reading*.

## Related topics

- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
