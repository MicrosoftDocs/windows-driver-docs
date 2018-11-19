---
title: Gyroscope thresholds
description: This topic provides information about the gyroscope thresholds.
ms.assetid: 68B11108-CA1A-4A49-BC44-4E9FE09955A9
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Gyroscope thresholds


This topic provides information about the gyroscope thresholds.

The following table shows the default thresholds for the gyroscope. For more information about the types shown in the type column, see the [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

|Property key|Type|Required/Optional|Default value|Description|
|---|---|---|---|---|
|PKEY_SensorData_AngularVelocityX_DegreesPerSecond|VT_R4|Required|0.1f|Minimum amount of change of angular velocity around the x-axis required to reach the threshold, measured in degrees per second.|
|PKEY_SensorData_AngularVelocityY_DegreesPerSecond|VT_R4|Required|0.1f|Minimum amount of change of angular velocity around the y-axis required to reach the threshold, measured in degrees per second.|
|PKEY_SensorData_AngularVelocityZ_DegreesPerSecond|VT_R4|Required|0.1f|Minimum amount of change of angular velocity around the z-axis required to reach the threshold, measured in degrees per second.|

Gyroscope drivers must report a sample reading to the sensors class extension by calling [SensorsCxSensorDataReady](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorscx/nf-sensorscx-sensorscxsensordataready) when either PKEY_SensorData_AngularVelocityX_DegreesPerSecond, PKEY_SensorData_AngularVelocityY_DegreesPerSecond, or PKEY_SensorData_AngularVelocityZ_DegreesPerSecond thresholds are met. Each threshold must be measured per-axis. Drivers must therefore call SensorsCxSensorDataReady whenever the threshold condition is met on any one of the axis.
When PKEY_SensorData_AngularVelocityX_DegreesPerSecond, or PKEY_SensorData_AngularVelocityY_DegreesPerSecond, or PKEY_SensorData_AngularVelocityZ_DegreesPerSecond is set to 0.0f, the driver must report sample readings to the sensors class extension at every interval. This mode is known as *sensor sample streaming*.

Gyroscope drivers must always report one sample reading immediately after the sensors class extension calls the [EvtSensorStart](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorscx/ns-sensorscx-_sensor_controller_config) callback irrespective of the threshold values. This sample is known as the known as initial sample reading.

## Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors/sensors%5D:%20Gyroscope%20thresholds%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





