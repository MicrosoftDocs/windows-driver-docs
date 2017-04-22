---
title: Driver update methods
author: windows-driver-content
ms.assetid: F809BCE4-9176-4503-9EC7-B80AC229ABB5
description: Update methods supported by the sensor driver.
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver update methods


A sensor driver supports internal methods that handle updates to the current report interval, change sensitivity, and so on. The pseudocode demonstrates this using the following methods:

-   DriverUpdateCRI(sensorID)
-   DriverUpdateCS(sensorID)
-   DriverUpdateLDA(sensorID)
-   DriverUpdateSensorState(sensorID, state, events)
-   DriverUpdateDatafields(sensorID)

## Sensor reporting-field updates


The **DriverUpdateCRI**, **DriverUpdateCS**, and **DriverUpdateLDA** methods demonstrate how a driver updates the current report interval, change sensitivity, and location data accuracy fields.

```ManagedCPlusPlus
DriverUpdateCRI(sensorID)
{
    if (true == flagCRI)
    {
        // Note that only the clients that have specified a CRI are considered
        // when determining which client has the lowest requested CRI
        Set selectedCRI of sensorID device to lowest of clientCRIs

        if (selectedCRI < effectiveMinCRI)
        {
            selectedCRI = effectiveMinCRI
        }
    }
    else //no client has specified a CRI
    {
        selectedCRI = defaultCRI
    }

    effectiveCRI = DriverUpdateSensorDeviceCRI(sensorID, selectedCRI)
}
```

```ManagedCPlusPlus
DriverUpdateCS(sensorID)
{
    for (each datafield supported by sensorID)
    {
        if (true == flagCS)
        {
            // Note that only the clients that have specified a CS are considered
            // when determining which client has the lowest requested CS
            Set selectedCS[n] of sensorID device to lowest of clientCS[n]
        }
        else //no client has specified a CS
        {
            selectedCS[n] = defaultCS[n]
        }
    }

    effectiveCS[] = DriverUpdateSensorDeviceCS(sensorID, selectedCS[])
}

```

```ManagedCPlusPlus
DriverUpdateLDA(sensorID)
{
    if (true == flagLDA)
    {
        // Note that only the clients that have specified an LDAare considered
        // when determining which client has the lowest (most accurate) requested LDA
        Set selectedLDA of sensorID device to lowest (most accurate) of clientLDAs
    }
    else //no client has specified a LDA
    {
        selectedLDA = defaultLDA
    }

    effectiveLDA = DriverUpdateSensorDeviceLDA(sensorID, selectedLDA)
}

```

## Sensor state updates


The **DriverUpdateSensorState** method demonstrates how a driver updates the sensor event reporting and power states.

```ManagedCPlusPlus
DriverUpdateSensorState(sensorID)
{
    if (clientCount == 0) // no clients
    {
        if (subscriberCount == 0) //no subscribers
        {
            selectedRS = reportingStateNoEvents
            selectedPS = powerStatePowerOff
        }
        else //has subscribers
        {
            //illegal state
            selectedRS = reportingStateNoEvents
            selectedPS = powerStatePowerOff
        }
    }
    else //has clients
    {
        if (subscriberCount == 0) //no subscribers
        {
            if (true == flagCRI)
            {
                selectedRS = reportingStateAllEvents
                selectedPS = powerStateFullPower
            }
            else
            {
                selectedRS = reportingStateNoEvents
                selectedPS = powerStateLowPower
            }
            else
            
        }
        else //has subscribers
        {
            selectedRS = reportingStateAllEvents
            selectedPS = powerStateFullPower
        }
    }

    effectiveRS = DriverUpdateSensorDeviceRS(sensorID, selectedRS)
    effectivePS = DriverUpdateSensorDevicePS(sensorID, selectedPS)
}
```

## Data field updates


The **DriverUpdateDatafields** method demonstrates how a driver updates its data fields.

```ManagedCPlusPlus
DriverUpdateDatafields(sensorID)
{
    if (effectiveRS == eventsOff)
    {
        if (sensor device is intelligent (ex. HID))
        {
            HIDSensorPollData(sensorID)

            // a poll response by the sensor device will happen asynchronously
            // the sensor device responds to this poll request by sending an
            // input packed, and this is received in the 
            // DriverHandleAsyncDataEvent() just as any other data packet
            // is received
        }
        else if (sensor device is simple (ex. SPB))
        {
            currentDatafields[] = SpbSensorPollData(sensorID)
            
            // ** TODO: Data is not updated asynchronously when polled
            // ** via SPB. Datafields[] must be assigned similarly to
            // ** DDIHandleAsyncDataEvent() when that logic has been
            // ** finalized. A shared helper method is likely best.
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
    else
    {
        // datafields are being updated by events
        // (i.e. DDIHandleAsyncDataEvent)
    }
}
```

## Related topics
[Sensor Driver Development Basics](sensor-driver-development-basics.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Driver%20update%20methods%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


