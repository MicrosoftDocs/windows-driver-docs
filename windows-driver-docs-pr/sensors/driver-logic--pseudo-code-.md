---
title: Sensor driver logic
description: This section describes key driver logic, or tasks, as pseudocode.
ms.assetid: 4B14C515-1B79-4B67-BA9A-365B2D6C0F07
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sensor driver logic


This section describes key driver logic, or tasks, as pseudocode. These tasks include the driver's support for the following client actions:

-   Client connects
-   Client subscribes to events
-   Client unsubscribes from events
-   Client disconnects

A client connects when a desktop application invokes the **ISensorCollection::GetAt** method. This method returns an **ISensor** interface for the desired sensor. When the application releases this interface, it disconnects the client.

A client subscribes to events when a desktop application invokes the **ISensorManager:SetEventSink** method. When the application releases the event sink returned by this method, the client unsubscribes from events.

## Abbreviations and variables


The pseudocode in this section uses the following abbreviations.

| Abbreviation | Explanation                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------|
| CRI          | Current report interval (specified in milliseconds)                                                       |
| CS           | Change sensitivity (values are dependent on sensor type)                                                  |
| CS\[\]       | Array of change sensitivities for all data fields (for example, a 3-axis accelerometer has three entries) |
| LDA          | Location desired accuracy (applies to location only)                                                      |
| RS           | Reporting state (indicates whether eventing is enabled or disabled)                                       |
| PS           | Power state (can be off, low, or high)                                                                    |



The pseudocode contains the following variables.

| Variable    | Description                                                                          |
|-------------|--------------------------------------------------------------------------------------|
| sensorID    | Unique identifier for a given sensor                                                 |
| clientID    | Unique identifier for a given client                                                 |
| flagCRI     | Set to True if at least one client has specified the current report interval         |
| flagCS      | Set to True if at least one client has specified the change sensitivity for a device |
| flagLDA     | Set to True if at least one client has specified the location desired accuracy       |
| deviceState | Indicates the driver is connected to the device                                      |



## Driver methods


A sensor driver must support both client and device initialization. The pseudocode demonstrates this using the following methods:

-   DriverClientInitialize
-   DeviceSensorInitialize

A sensor driver supports the platform's device-driver interface (DDI). The pseudocode demonstrates this using the following methods:

-   DDIOnClientConnect
-   DDIOnClientDisconnect
-   DDIOnClientSubscribeToEvents
-   DDIOnClientUnsubscribeFromEvents
-   DDIOnSetCRI
-   DDIOnSetCS
-   DDIOnSetLDA
-   DDIOnGetProperties
-   DDIOnGetDatafields
-   DDIHandleAsyncDataEvent

A sensor driver supports internal methods that handle updates to the current report interval, change sensitivity, and so on. The pseudocode demonstrates this using the following methods:

-   DriverUpdateCRI
-   DriverUpdateCS
-   DriverUpdateLDA
-   DriverUpdateSensorState
-   DriverUpdateDatafields

A sensor driver supports methods that update the sensor device. The pseudocode demonstrates this using the following methods:

-   DriverUpdateDeviceCRI
-   DriverUpdateDeviceCS
-   DriverUpdateDeviceLDA
-   DriverUpdateDeviceRS
-   DriverUpdateDevicePS

A sensor driver supports methods that interface with a device containing multiple sensors. The pseudocode demonstrates this using the following method:

-   DriverUpdateDeviceState

If a sensor driver supports HID sensors, it may support the following methods:

-   HIDSensorPollData
-   HIDSensorDeviceEvent
-   HIDSensorSetProperties
-   HIDSensorGetProperties

If a sensor driver supports HID sensors, it may support the following method for a device that contains multiple sensors:

-   HIDDeviceManagePower

If a sensor driver supports simple sensors (for example, I2C or SPI), it may support the following methods:

-   SpbSensorPollData
-   SpbSensorDeviceEvent

## Driver structures and enumerations


A HID driver supports input reports. The pseudocode uses the following data structure to represent a report.

```cpp
struct _inputReport
{
    reportID
    senstate
    eventType
    sensorData //this varies from sensor to sensor

} buffer, pbuffer
```

A sensor driver saves client data. The pseudocode uses the following data structure to save client data.

```cpp
struct clientEntry
{
    clientCRI
    clientCS[]
    clientLDA
    clientSubscribed
}
```

A sensor driver needs to represent the device state. The pseudocode uses the following enumeration to represent the device state.

```cpp
enum deviceState
{
    deviceStateDisconnected // driver is disconnected from the device
    deviceStateConnected //driver is connected to the device
}
```

A sensor driver needs to represent the device state. The pseudocode uses the following enumeration to represent the device state.

```cpp
enum deviceState
{
    deviceStateDisconnected // driver is disconnected from the device
    deviceStateConnected //driver is connected to the device
}
```

## Related topics
[Sensor Driver Development Basics](sensor-driver-development-basics.md)



