---
title: Internal helper methods
description: A sensor driver supports a number of internal helper methods that perform tasks like polling for data, setting properties, retrieving properties, updating the device state, and supporting events.
ms.assetid: BF5956FE-E1B6-476A-9B6E-86B400DE0A20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Internal helper methods


A sensor driver supports a number of internal helper methods that perform tasks like polling for data, setting properties, retrieving properties, updating the device state, and supporting events.

## Supporting device state updates for multi-sensor devices


A sensor driver supports methods that set the device state for a single device that contains multiple sensors. The pseudocode demonstrates this using the **DriverUpdateDeviceState** method.

```cpp
DriverUpdateDeviceState()
{
    if ((sensor device is intelligent (e.g. HID) ||
        (sensor device is simple (e.g. SPB))
    {

        // if no client is connected to any of the sensors on this device
        // then disconnect from the device
        flagConnected = false
        for (all sensors on device)
        {
            if (clientCount > 0)
            {
                flagConnected = true
            }
        }

        if (false == flagConnected)
        {
            Disconnect from device
            deviceState = deviceStateDisconnected
        }
        else
        {
            Connect to device
            deviceState = deviceStateConnected
        }
    }
    else if (sensor device is fusion)
    {
        //handle fusion sensor
    }
    else //is some other kind of sensor
    {
        //special action
    }
}
```

## Internal methods for intelligent sensors


If a sensor driver supports intelligent sensors (like HID), it may include support for methods that poll data, handle events, retrieve properties, set properties, and manage power. The pseudocode demonstrates these tasks using the **HIDSensorPollData**, **HIDSensorSetProperties**, and **HIDSensorGetProperties** methods.

```cpp
HIDSensorPollData(sensorID) // Driver issues USB/HID “GET_INPUT” command to the sensor device
{
    // the driver is making a request for polled data
    // if the sensor is in a READY state respond by sending
    // the data for this sensor asynchronously to the driver
    if (true == sensorReady)
    {
        sensorState = sensorStateReady
        sensorEvent = eventTypeDataPoll
    }
    else
    {
        Set sensorState = sensorStateNoData //or failure, or initializing, or not available as appropriate
        Set sensorEvent = eventTypeStateChange
    }

    Send async data to driver //received in driver by DDIHandleAsyncDataEvent()
}
```

```cpp
HIDSensorSetProperties(sensorID, requestedRS, requestedPS, requestedCRI, requestedCS[], requestedLDA) //SET_FEATURE
{
    if (requestedRS == reportingStateAllEvents) //reporting state
    {
        Set effectiveRS = reportingStateAllEvents
    }
    else
    {
        Set effectiveRS = reportingStateNoEvents
    }

    if (requestedPS == powerStateFullPower) //power state
    {
        Set effectivePS = powerStateFullPower
    }
    else if (requestedPS == powerStateLowPower)
    {
        Set effectivePS = powerStateLowPower
    }
    else
    {
        Set effectivePS = powerStatePowerOff
    }

    if (can support requestedCRI)
    {
        Set effectiveCRI = requestedCRI
    }
    else
    {
        Set effectiveCRI = value that can be supported
    }

    if (can support requestedCS[])
    {
        Set effectiveCS[] = requestedCS[]
    }
    else
    {
        Set effectiveCS[] = values that can be supported
    }

    if (requestedLDA == locDesiredAccuracyHigh) //location desired accuracy
    {
        Set effectiveLDA = locDesiredAccuracyHigh
    }
    else
    {
        Set effectiveLDA = locDesiredAccuracyDefault
    }


}
```

```cpp
HIDSensorGetProperties(sensorID, RS, PS, CRI, CS[], LDA) //Driver issues USB/HID “GET_FEATURE” command to the sensor
{
    buffer.effectiveRS
    buffer.effectivePS
    buffer.effectiveCRI
    buffer.effectiveCS[]
    buffer.effectiveLDA

    // The sensor device can optionally also override the following properties
    buffer.sensorCategory
    buffer.sensorType
    buffer.minCRI
    buffer.persistentUniqueID
    buffer.sensorManufacturer
    buffer.sensorModel
    buffer.serialNumber
    buffer.friendlyName
    buffer.sensorDescription
    buffer.connectionType

    Send buffer to Driver
}
```

## Internal methods for simple sensors


If a sensor driver supports simple sensors (like SPB), it may include support for methods that poll data. The pseudocode demonstrates this task using the **SpbSensorPollData** method.

```cpp
datafields[] SpbSensorPollData(sensorID)
{
    // the driver is making a request for polled data, respond
    // by returning the data for this sensor synchronously to the driver

    Query newDatafields[] synchronously from the device via SPB

    return newDatafields[]
}
```

## Related topics
[Sensor Driver Development Basics](sensor-driver-development-basics.md)



