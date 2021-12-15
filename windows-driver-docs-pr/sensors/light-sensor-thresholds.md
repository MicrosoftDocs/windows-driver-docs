---
title: Light sensor thresholds
description: This topic provides information about the light sensor thresholds.
ms.date: 07/20/2018
---

# Light sensor thresholds


This topic provides information about the light sensor thresholds.

The following table shows the driver's default thresholds for the light sensor. The default interval for the light sensor is 10 Hz. For more information about the types shown in the type column, see the [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

|Property key|Type|Required/Optional|Default value|Description|
|---|---|---|---|---|
|PKEY_SensorData_LightLevel_Lux|VT_R4|Required|0.25f|Minimum amount of change of illuminance required to reach the threshold, measured in percentages of lux. A value of 0.25f means 25% change in illuminance.|
|PKEY_SensorData_LightLevel_Lux_Threshold_AbsoluteDifference|VT_R4|Optional|1.0f|Minimum amount of change of illuminance required to reach the threshold, measured in lux. A value of 1.0f means 1 lux change in illuminance. <br>__Note:__ Implementing this threshold is highly recommended on portable devices as it helps reduce battery power consumption in low ambient light environments.|
|PKEY_SensorData_LightChromaticityX|VT_R4|Required if color is supported. Optional otherwise|0.01f|Minimum amount of change of the CIE 1931 x color coordinate required to reach the threshold, expressed as an absolute difference.|
|PKEY_SensorData_LightChromaticityY|VT_R4|Required if color is supported. Optional otherwise|0.01f|Minimum amount of change of the CIE 1931 y color coordinate required to reach the threshold, expressed as an absolute difference.|
|PKEY_SensorData_LightTemperature_Kelvins|VT_R4|Required if color is supported. Optional otherwise|50.0f|Minimum amount of change of the light temperature required to reach the threshold, measured in Kelvins.|

The light sensor must report new data samples *only if the LUX value changes*. This recommended reporting model ensures that the light sensor does not report new data samples repeatedly, when it is in a completely dark, zero (0) LUX environment.

If PKEY_SensorData_LightLevel_Lux_Threshold_AbsoluteDifference is not provided, ambient light sensor drivers must report a sample reading to the sensors class extension by calling [SensorsCxSensorDataReady](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensordataready) when PKEY_SensorData_LightLevel_Lux threshold is met. The PKEY_SensorData_LightLevel_Lux threshold is expressed as a percentage of difference in lux. For example, if this threshold value is set to 0.25f and the last sample reported to the sensor class extension was of 40 lux, the next sample to be reported should either be lower than 30 lux or greater than 50 lux (+/-25% of 40).
If PKEY_SensorData_LightLevel_Lux_Threshold_AbsoluteDifference is provided in addition to PKEY_SensorData_LightLevel_Lux, ambient light sensors must report a sample reading to the sensors class extension if __both__ thresholds are met. For example, if PKEY_SensorData_LightLevel_Lux_Threshold_AbsoluteDifference is set to 4.0 lux and PKEY_SensorData_LightLevel_Lux is set to 0.25 (i.e. 25%) and if the value of the last sample reading reported to the sensors class extension is 4 lux, the most restrictive threshold is PKEY_SensorData_LightLevel_Lux_Threshold_AbsoluteDifference. Therefore, the next sample reading to be reported should be 0 lux or 8 lux.
Comparatively, if PKEY_SensorData_LightLevel_Lux_Threshold_AbsoluteDifference is set to 4.0 lux and PKEY_SensorData_LightLevel_Lux is set to 0.25 (i.e. 25%) but the value of the last sample reading reported to the sensors class extension is 40 lux, the most restrictive threshold is PKEY_SensorData_LightLevel_Lux. In this case, the next sample reading to be reported should be 30 lux or 50 lux.
PKEY_SensorData_LightLevel_Lux_Threshold_AbsoluteDifference is never set without PKEY_SensorData_LightLevel_Lux.

When the sensor driver reports Chromaticity x and Chromaticity y color components, ambient light sensor drivers must also support PKEY_SensorData_LightChromaticityX, PKEY_SensorData_LightChromaticityY, and PKEY_SensorData_LightTemperature_Kelvins thresholds.
The ambient light sensor driver reports a sample reading to the sensors class extension when either the PKEY_SensorData_LightChromaticityX, the PKEY_SensorData_LightChromaticityY, or the PKEY_SensorData_LightTemperature_Kelvins threshold is met.

Ambient light sensor drivers must always report one sample reading immediately after the sensors class extension calls the [EvtSensorStart](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config) callback irrespective of the threshold values. This sample is known as the initial sample reading.

>**Note**   The ambient light sensor driver must also report a sample reading to the sensor class extension when IsValid data field changes, irrespective of the thresholds being set.

When PKEY_SensorData_LightLevel_Lux_Threshold_AbsoluteDifference and PKEY_SensorData_LightLevel_Lux are set to 0.0f, the driver must report sample readings to the sensors class extension at every interval.
When PKEY_SensorData_LightChromaticityX __or__ PKEY_SensorData_LightChromaticityY __or__ PKEY_SensorData_LightTemperature_Kelvins is set to 0.0f, the driver must report sample readings to the sensors class extension at every interval.
Reporting a sensor sample at every interval is known as *sensor sample streaming*.

>[!NOTE]
> In thresholding mode, do not report consecutive samples that have PKEY\_SensorData\_IsValid set to FALSE. In other words, in thresholding mode, only send the first sample in which PKEY\_SensorData\_IsValid was switched to FALSE.
 

## Related topics


[PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
