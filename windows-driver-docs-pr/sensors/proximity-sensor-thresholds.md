---
title: Proximity sensor thresholds
description: This topic provides information about the proximity sensor thresholds.
ms.assetid: AD93421B-4787-4E56-B01D-58027EFEAC2D
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Proximity sensor thresholds

There is no configurable threshold defined for proximity sensors.

Proximity sensor drivers must report a sample reading to the sensors class extension by calling [SensorsCxSensorDataReady](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensordataready) whenever the PKEY_SensorData_ProximityDetection value changes.
The proximity sensor drivers should never report in a row two proximity readings to the class extension unless PKEY_SensorData_ProximityDetection has changed.

That said, proximity sensor drivers must always report one sample reading immediately after the sensors class extension calls the [EvtSensorStart](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) callback. This sample is known as the known as *initial sample reading*.

## Related topics


[PROPVARIANT structure](https://go.microsoft.com/fwlink/p/?linkid=313395)



