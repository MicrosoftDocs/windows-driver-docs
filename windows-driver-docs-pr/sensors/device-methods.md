---
title: Device methods
description: The sensor firmware supports several helper methods that perform tasks like supporting events and managing power.
ms.assetid: 4F1463B0-A307-4C70-A660-18AD876B3363
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device methods


The sensor firmware supports several helper methods that perform tasks like supporting events and managing power.

## Device methods for intelligent sensors


For intelligent sensors (like HID), the firmware includes support for methods that handle events and manage power. The pseudocode demonstrates these tasks using the **HIDSensorDeviceEvent** and **HIDDeviceManagePower** methods.

```cpp
HIDSensorDeviceEvent(sensorID) // Driver issues USB/HID “SEND_INPUT” command to the sensor
{
    // an event has occurred on the sensor device
    // this could be one of several things, not only just a data update event
    if (event == eventData) //ex data change exceeded effectiveCS[]
    {
        if (effectiveRS = reportingStateAllEvents)
        {
            Set sensorState = sensorStateReady
            Set sensorEvent = eventTypeCS (or data update as appropriate)
            Send async data to driver //received in driver by DDIHandleAsyncDataEvent()
        }
        else
        {
            //do nothing
        }
    }
    else if (event == eventStateChange)
    {
        // if this event is not a data update event
        // then no matter what the reporting state and
        // power state (as long as power is on)
        // of the device then send the event
        // to the driver
        Set sensorState = current sensor state
        Set sensorEvent = type for this event
        Send async data to driver //received in driver by DDIHandleAsyncDataEvent()
    }
}
```

```cpp
HIDDeviceManagePower(powerState)
{
    if (powerstate for all sensors is == powerStatePowerOff)
    {
        Turn the power off to all sensors
        Turn off power to the device
    }
    else if (powerState for any sensor is >= powerStateLowPower)
    {
        Turn on power to the device
        Turn on power to the sensor
        sensorState = sensorStateInitializing
        Send sensor state to sensor asynchronously using SEND_INPUT USB/HID command

        Initialize the sensor
        if (sensor is ready)
        {
            Set sensorState = sensorStateReady
            Send sensorState to sensor asynchronously using SEND_INPUT USB/HID command
        }
        else if (sensor is never is initialized and becomes ready)
        {
            Set sensorState = sensorStateError
            Send sensorstate to sensor asynchronously using SEND_INPUT USB/HID command
        }
    }
}
```

## Device methods for simple sensors


For simple sensors (like SPB), the firmware includes support for a method that handles events. The pseudocode demonstrates this task using the **SpbSensorDeviceEvent**.

```cpp
SpbSensorDeviceEvent(sensorID)
{
    // an interrupt has occurred on the sensor device
    // this could be one of several things, not only just a data update event
    if (event == eventData) //ex data change exceeded effectiveCS[]
    {
        if (effectiveRS = reportingStateAllEvents)
        {
            Acknowledge device interrupt
            Query data synchronously from the device via SPB

            Set sensorState = sensorStateReady
            Set sensorEvent = eventTypeCS (or data update as appropriate)

            Invoke DDIHandleAsyncDataEvent(sensorID)
        }
        else
        {
            //do nothing
        }
    }
    else if (event == eventStateChange)
    {
        // if this event is not a data update event
        // then no matter what the reporting state and
        // power state (as long as power is on)
        // of the device then send the event
        // to the driver. Note not all simple devices
        // will support state change eventing.

        Acknowledge device interrupt
        Query state synchronously from the device via SPB

        Set sensorState = current sensor state
        Set sensorEvent = type for this event
    }
}
```

 

 




