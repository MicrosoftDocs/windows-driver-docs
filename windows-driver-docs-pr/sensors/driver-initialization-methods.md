---
title: Driver initialization methods
ms.assetid: CA8F6308-501D-47BC-902E-3259949A1D57
description: Methods supported by the sensor driver to initialize a device.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver initialization methods


A sensor driver must support both client and device initialization. The pseudocode demonstrates this using the following methods:

-   DriverClientInitialize()
-   DeviceSensorInitialize()

## Client Initialization


The client initialization method has the following form.

```cpp
DriverClientInitialize(sensorID)
{
    // the following properties can be set from the API
    CRI = defaultCRI
    CS[] = defaultCS[]
    LDA = default[LDA]

    // the following properties cannot be set from the API
    // the driver provides defaults for these properties
    // the defaults can be overridden by the device
    sensorCategory = defaultSensorCategory
    sensorType = defaultSensorType
    minCRI = defaultMinCRI
    persistentUniqueID = defaultPersistentUniqueID
    sensorManufacturer = defaultSensorManufacturer
    sensorModel = defaultSensorModel
    serialNumber = defaultSerialNumber
    friendlyName = defaultFriendlyName
    sensorDescription = defaultDescription
    connectionType = defaultConnectionType

    // the following values are internal to the driver
    clientCount = 0
    subscriberCount = 0

    flagCRI = false
    flagCS = false
    flagLDA = false

    deviceState = deviceStateDisconnected
}
```

## Related topics
[Sensor Driver Development Basics](sensor-driver-development-basics.md)



