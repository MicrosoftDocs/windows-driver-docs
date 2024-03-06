---
title: Driver Initialization Methods
description: Methods supported by the sensor driver to initialize a device.
ms.date: 01/11/2024
---

# Driver initialization methods

A sensor driver must support both client and device initialization. The pseudocode demonstrates this using the following methods:

- DriverClientInitialize()
- DeviceSensorInitialize()

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

- [Introduction to the Sensor and Location Platform in Windows](./index.md)
- [Sensor Driver Logic](./driver-logic--pseudo-code-.md)
