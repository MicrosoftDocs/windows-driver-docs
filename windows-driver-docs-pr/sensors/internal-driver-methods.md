---
title: Internal helper methods
description: A sensor driver supports a number of internal helper methods that perform tasks like polling for data, setting properties, retrieving properties, updating the device state, and supporting events.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: BF5956FE-E1B6-476A-9B6E-86B400DE0A20
---

# Internal helper methods


A sensor driver supports a number of internal helper methods that perform tasks like polling for data, setting properties, retrieving properties, updating the device state, and supporting events.

## Supporting device state updates for multi-sensor devices


A sensor driver supports methods that set the device state for a single device that contains multiple sensors. The pseudocode demonstrates this using the **DriverUpdateDeviceState** method.

```ManagedCPlusPlus
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

```ManagedCPlusPlus
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

```ManagedCPlusPlus
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

```ManagedCPlusPlus
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

```ManagedCPlusPlus
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Internal%20helper%20methods%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





