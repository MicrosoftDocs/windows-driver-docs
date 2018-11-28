---
title: Sensor DDSI Functions
description: The sensor device driver software interface (DDSI) functions represent the interface a sensor driver uses to interact with the class extension.
ms.assetid: 3DB30155-8DBE-4AE9-A0CC-8089DC255E32
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Sensor DDSI functions

The sensor device driver software interface (DDSI) functions represent the interface a sensor driver uses to interact with the class extension. These functions are implemented by the class extension.

## In this section

|Topic|Description|
|---|---|
|SensorsCxDeviceInitConfig|This function configures the sensor device.|
|SensorsCxDeviceInitialize|This function initializes the sensor in the class extension.|
|SensorsCxSensorCreate|This function creates an instance of a sensor in the class extension.|
|SensorsCxSensorInitialize|This function sets the enumeration properties of a sensor.|
|SensorsCxSensorDataReady|This function notifies the class extension that the driver has retrieved data.|
|SensorsCxStateChange|Used to initialize a state change.|
|SensorsCxDeviceGetSensorList|This function returns a list of sensor instances associated with a WDFDEVICE.|



--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors/sensors%5D:%20Sensor%20DDSI%20Functions%20%20RELEASE:%20%282/19/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
