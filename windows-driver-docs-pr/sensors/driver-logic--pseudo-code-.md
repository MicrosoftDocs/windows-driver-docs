---
title: Sensor driver logic
description: This section describes key driver logic, or tasks, as pseudocode.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4B14C515-1B79-4B67-BA9A-365B2D6C0F07
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

```ManagedCPlusPlus
struct _inputReport
{
    reportID
    senstate
    eventType
    sensorData //this varies from sensor to sensor

} buffer, pbuffer
```

A sensor driver saves client data. The pseudocode uses the following data structure to save client data.

```ManagedCPlusPlus
struct clientEntry
{
    clientCRI
    clientCS[]
    clientLDA
    clientSubscribed
}

```

A sensor driver needs to represent the device state. The pseudocode uses the following enumeration to represent the device state.

```ManagedCPlusPlus
enum deviceState
{
    deviceStateDisconnected // driver is disconnected from the device
    deviceStateConnected //driver is connected to the device
}

```

A sensor driver needs to represent the device state. The pseudocode uses the following enumeration to represent the device state.

```ManagedCPlusPlus
enum deviceState
{
    deviceStateDisconnected // driver is disconnected from the device
    deviceStateConnected //driver is connected to the device
}

```

## Related topics


[Sensor Driver Development Basics](sensor-driver-development-basics.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Sensor%20driver%20logic%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





