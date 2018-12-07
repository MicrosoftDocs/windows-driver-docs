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
