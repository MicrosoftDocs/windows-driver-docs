---
title: Creating a persistent unique identifier for a universal drivers based sensor
description: Creating a persistent unique identifier for a universal drivers based driver
ms.assetid: B0131BC5-F76F-46B0-8BDE-4220D971AA29
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Creating a persistent unique identifier for a sensor


Your driver must create a *persistent unique identifier* (PUID) for each sensor. A PUID is a GUID value that is stored across sessions and uniquely identifies the object on the device. Your driver must return the PUID value when queried for the property named **DEVPKEY_Sensor_PersistentUniqueId**. If a device contains multiple sensors, each sensor must be assigned its own PUID. Applications can retrieve this ID by using the [Windows.Devices.Enumeration](https://docs.microsoft.com/uwp/api/Windows.Devices.Enumeration) WinRT APIs.

You should create a new PUID for each sensor, when the sensor first connects to the computer, and then store this value for later use.

Your driver should create or retrieve the PUID before calling the [SensorsCxSensorInitialize](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorscx/nf-sensorscx-sensorscxsensorinitialize) initialization routine. This function supplies a pointer to the [SENSOR_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorscx/ns-sensorscx-_sensor_config) structure that holds the sensor configuration. You can use this pointer to access a specific property store for each device.

## Related topics
[Sensors Driver ADXL345Acc Sample](http://go.microsoft.com/fwlink/p/?LinkId=617957)
<!--
http://go.microsoft.com/fwlink/p/?LinkId=617957: https://github.com/Microsoft/Windows-driver-samples/tree/master/sensors/ADXL345Acc
-->

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors/sensors%5D:%20Creating%20a%20persistent%20unique%20identifier%20for%20a%20sensor%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


