---
title: Creating a persistent unique identifier for a universal drivers based sensor
description: Creating a persistent unique identifier for a universal drivers based driver
ms.date: 07/20/2018
---

# Creating a persistent unique identifier for a sensor


Your driver must create a *persistent unique identifier* (PUID) for each sensor. A PUID is a GUID value that is stored across sessions and uniquely identifies the object on the device. Your driver must return the PUID value when queried for the property named **DEVPKEY_Sensor_PersistentUniqueId**. If a device contains multiple sensors, each sensor must be assigned its own PUID. Applications can retrieve this ID by using the [Windows.Devices.Enumeration](/uwp/api/Windows.Devices.Enumeration) WinRT APIs.

You should create a new PUID for each sensor, when the sensor first connects to the computer, and then store this value for later use.

Your driver should create or retrieve the PUID before calling the [SensorsCxSensorInitialize](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensorinitialize) initialization routine. This function supplies a pointer to the [SENSOR_CONFIG](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_config) structure that holds the sensor configuration. You can use this pointer to access a specific property store for each device.

## Related topics
[Sensors Driver ADXL345Acc Sample](https://go.microsoft.com/fwlink/p/?LinkId=617957)
<!--
https://go.microsoft.com/fwlink/p/?LinkId=617957: https://github.com/Microsoft/Windows-driver-samples/tree/master/sensors/ADXL345Acc
-->
