---
title: Driver interface methods
ms.assetid: 675F4188-3B9A-421B-98EF-FE063B550231
description: Interface methods supported by the sensor driver.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver interface methods


A sensor driver must support the sensor platform's device-driver interface (DDI). The pseudocode demonstrates this using the following methods:

-   DDIOnClientConnect(sensorID, clientID)
-   DDIOnClientDisconnect(sensorID, clientID)
-   DDIOnClientSubscribeToEvents(sensorID, clientID)
-   DDIOnClientUnsubscribeFromEvents(sensorID, clientID)
-   DDIOnSetCRI(sensorID, requestedCRI)
-   DDIOnSetCS(sensorID, requestedCSs)
-   DDIOnSetLDA(sensorID, requestedLDA)
-   DDIOnGetProperties(sensorID, CRI, CS\[\], LDA)
-   DDIOnGetDatafields(sensorID, datafields\[\])
-   DDIHandleAsyncDataEvent(sensorID, inputReport)

## Client connections


The **DDIOnClientConnect** and **DDIOnClientDisonnect** methods demonstrate how a driver handles the connection and disconnection of a client.

```cpp
DDIOnClientConnect(sensorID, clientID)
{
    clientList[clientID] = clientEntry

    clientEntry.clientCRI = DONT_CARE
    clientEntry.clientCS[] = default[]
    clientEntry.clientLDA = default //location only
    clientList[clientID] = clientEntry
    clientCount++

    if (1 == clientCount)
    {
        DriverUpdateDeviceState()
        DriverUpdateSensorState(sensorID
        DriverUpdateDatafields(sensorID)
        effectiveRS = DriverUpdateRS(sensorID)
        effectivePS = DriverUpdatePS(sensorID)
}
    else //more than 1 client connected
    {
        //no additional initial action required
    }

    // Since a new client has connected, the effective CRI, CS[], and LDA must
    // be re-evaluated for all of the clients now connected
    effectiveCRI = DriverUpdateCRI(sensorID)
    effectiveCS[] = DriverUpdateCS(sensorID)
    effectiveLDA = DriverUpdateLDA(sensorID) //location only
    effectiveRS = DriverUpdateRS(sensorID)
    effectivePS = DriverUpdatePS(sensorID)
}
```

```cpp
DDIOnClientDisconnect(sensorID, clientID)
{
    delete clientList[clientID]
    clientCount--

    if (0 == clientCount)
    {
        DriverUpdateSensorState(sensorID)
        DriverUpdateDatafields(sensorID)
        DriverUpdateDeviceState()

        flagCRI = false
        flagCS = false
    }
    else //clients are still connected
    {
        // A client has NOT specified a CRI if
        // - the CRI has never been set by that client since having been connected
        // - the client has specified a CRI of ‘0’, which means to use the default
        if (no remaining client has specified CRI)
        {
            flagCRI = false
        }
        // A client has NOT specified a CS[] if
        // - the CS[] has never been set by that client since having been connected
        // If the client HAS specified a CS[], there is no way for the client to
        // instead revert to the default (as can be done with the CRI)
        if (no remaining client has specified CS[])
        {
            flagCS = false
        }
    }

    // Since an existing client has disconnected, the effective CRI, CS[], and LDA must
    // be re-evaluated for all of the clients now connected
    effectiveCRI = DriverUpdateCRI(sensorID)
    effectiveCS[] = DriverUpdateCS(sensorID)
    effectiveLDA = DriverUpdateLDA(sensorID) //location only
    effectiveRS = DriverUpdateRS(sensorID)
    effectivePS = DriverUpdatePS(sensorID)
}
```

## Client event subscriptions


The **DDIOnClientSubscribeToEvents** and **DDIOnClientUnsubscribeFromEvents** methods demonstrate how a driver handles event subscriptions.

```cpp
DDIOnClientSubscribeToEvents(sensorID, clientID)
{
    clientList[clientID].clientSubscribed = true
    subscriberCount++

    if (1 == subscriberCount)
    {
        DriverUpdateSensorState(sensorID, sensorStateActive, reportingStateAllEvents)
    }
    else //more than 1 subscriber connected
    {
        //no additional initial action required
    }

    effectiveRS = DriverUpdateRS(sensorID)
    effectivePS = DriverUpdatePS(sensorID)
}
```

```cpp
DDIOnClientUnsubscribeFromEvents(sensorID, clientID)
{
    delete clientList[clientID]
    subscriberCount--

    if (0 == subscriberCount)
    {
        DriverUpdateSensorState(sensorID
    }
    else //clients are still subscribed
    {
        effectiveRS = DriverUpdateRS(sensorID)
        effectivePS = DriverUpdatePS(sensorID)
    }
}
```

## Sensor reporting fields


The **DDIOnSetCRI**, **DDIOnSetCS**, and **DDIOnSetLDA** methods demonstrate how a driver sets the current report interval, change sensitivity, and location data accuracy fields.

```cpp
/////////////////////////////////////////////////////////////////////////////////////////////
//
// DDIOnSetCRI
//
// Note that setting the CRI has an effect on the reportingState at the device because by setting
// the CRI the client implies it wants event-driven data constantly available in the datafields
// even though that client has not subscribed to events.
//
/////////////////////////////////////////////////////////////////////////////////////////////
DDIOnSetCRI(sensorID, clientID, requestedCRI) //OnSetProperties
{
    if (requestedCRI == DONT_CARE)
    {
        if (clientList[clientID].clientCRI != DONT_CARE)
        {
             clientList[clientID].clientCRI = DONT_CARE
        }
        // A client has NOT specified a CRI if
        // - the CRI has never been set by that client since having been connected
        // - the client has specified a CRI of ‘0’, which means to use the default
        if (no remaining client has specified CRI)
        {
            flagCRI = false
        }
    }
    else
    {
        //this sets the value of CRI to a definite value
        clientList[clientID].clientCRI = requestedCRI
        flagCRI = true
    }

    DriverUpdateCRI(sensorID)
    DriverUpdateSensorState(sensorID)
}
```

```cpp
/////////////////////////////////////////////////////////////////////////////////////////////
//
// DDIOnSetCS
//
// Note that setting the CS for any datafield only has an effect on the CS at the device and
// has no explicit effect on either the reporting state (eventing) or the power state.
// However, the device may wish to take into account the CS setting when managing power
//
/////////////////////////////////////////////////////////////////////////////////////////////
DDIOnSetCS(sensorID, clientID, requestedCS[]) //OnSetProperties
{
    for (each datafield n supported by sensorID)
    {
        if (requestedCS[n] == DONT_CARE)
        {
            if (clientList[clientID].clientCS[n] != DONT_CARE)
            {
                 clientList[clientID].clientCS[n] = DONT_CARE
            }
            // A client has NOT specified a CS for datafield n if
            // - the CS[n] has never been set by that client since having been connected
            // - the client has specified a CS[n] of type ‘VT_NULL’, which means to use the default
            if (no remaining client has specified CRI)
            {
                flagCS = false
            }
        }
        else
        {
            //this sets the value of CS[n] to a definite value
            clientList[clientID].clientCS[n] = requestedCS
            flagCS = true
        }
    }

    DriverUpdateCS(sensorID)
}
```

```cpp
DDIOnSetLDA(sensorID, clientID, requestedLDA) //OnSetProperties, location only
{
    clientList[clientID].clientLDA = requestedLDA

    DriverUpdateLDA(sensorID)
}
```

## Property and datafield retrieval


The **DDIOnGetProperties** and **DDIOnGetDatafields** methods demonstrate how a driver retrieves properties and datafields.

```cpp
DDIOnGetProperties(sensorID, CRI, CS[], LDA)
{
    // the following properties can be set from the API
    CRI = effectiveCRI
    CS[] = effectiveCS[]
    LDA = effective[LDA]

    // the following properties cannot be set from the API
    // the driver provides defaults for these properties
    // the defaults can be overridden by the device
    sensorCategory = effectiveSensorCategory
    sensorType = effectiveSensorType
    minCRI = effectiveMinCRI
    persistentUniqueID = effectivePersistentUniqueID
    sensorManufacturer = effectiveSensorManufacturer
    sensorModel = effectiveSensorModel
    serialNumber = effectiveSerialNumber
    friendlyName = effectiveFriendlyName
    sensorDescription = effectiveDescription
    connectionType = effectiveConnectionType
}
```

```cpp
DDIOnGetDatafields(sensorID, datafields[])
{
    if (((false == flagCRI) && (0 == subscriberCount)) || (false == initalDataReceived))
    {
        //poll sensorID device for data
        DriverUpdateDatafields(sensorID)

        //wait for poll response for no more than pollResponseTimeLimit
        if (response received from poll)
        {
            datafields[] = currentDatafields[]
        }
        Else //no response was received within pollResponseTimeLimit mS
        {
            if (true == initialDataReceived)
            {
                datafields[] = currentDatafields[] //not updated
            }
            else
            {
                datafields[] = currentDatafields[] //are VT_EMPTY
            }
        }
    }
    else
    {
        datafields[] = currentDatafields[] //updated at effectiveCRI rate
    }
}
```

## Supporting asynchronous events


The **DDIHandleAsyncDataEvent** method demonstrates how a driver supports asynchronous events.

```cpp
DDIHandleAsyncDataEvent(sensorID, buffer)
{
    if (buffer.sensorDeviceState == sensorStateReady)
    {
        if (buffer.sensorDeviceEvent == eventTypeCS)
        {
            initialDataReceived = true
        }
        else if (buffer.sensorDeviceEvent == eventTypeDataPoll)
        {
            initialDataReceived = true
            pollResponseReceived = true
        }

        currentDatafields[] = buffer[]
        SetState(sensorStateReady)
        Fire Event
    }
    else
    {
        Set received initial data = false
        SetState(buffer.sensorDeviceState) //something other than ready
        currentDatafields[] = VT_EMPTY
    }
}
```

## Related topics
[Sensor Driver Development Basics](sensor-driver-development-basics.md)



