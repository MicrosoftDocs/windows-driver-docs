---
title: About Sensor Driver Events
description: About Sensor Driver Events
ms.assetid: 1e747743-f701-4854-92be-7b55c39fee08
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# About Sensor Driver Events


Applications can receive information from sensors in two ways: synchronously, by requesting a particular property or data field, or asynchronously, by subscribing to an event that is raised by the sensor driver.

Sensor drivers can raise **state change events**, which notify applications about a transition in the device to a new operational condition, and other kinds of event notifications. Your driver should raise separate events for each sensor that your device provides.

**Note**  Do not use [**IWDFDevice::PostEvent**](https://msdn.microsoft.com/library/windows/hardware/ff558835) to raise sensor events. The sensor platform will not forward such events to the connected client programs.

 

## State Change Events

Sensor drivers raise state change events by calling the sensor class extension's [**ISensorClassExtension::PostStateChange**](https://msdn.microsoft.com/library/windows/hardware/ff545523) method. For example, a driver that has finished initializing a sensor will call this method to signal the new [**SensorState**](https://msdn.microsoft.com/library/windows/hardware/ff545708) value named SENSOR\_STATE\_READY.

## Event Constants

The sensor platform defines the following constants for driver events.

**Sensor Event Types**

The sensor platform defines the following sensor event types identifiers.

| Name | Description |
| --- | --- |
| SENSOR_EVENT_DATA_UPDATED | Indicates that new data is available.
| SENSOR_EVENT_PROPERTY_CHANGED| Indicates that a property value changed.|
| SENSOR_EVENT_STATE_CHANGED| Indicates a change of operational state, for example, from SENSOR_STATE_INITIALIZING to SENSOR_STATE_READY.|


**Sensor Event PROPERTYKEYs**

The sensor platform defines the following **PROPERTYKEYs** to identify the parameters for sensor events.

| Name | Description |
| --- | --- |
| SENSOR_EVENT_PARAMETER_EVENT_ID| Indicates that the GUID value in IPortableDeviceValues is an event type ID, such as SENSOR_EVENT_DATA_UPDATED.|
| SENSOR_EVENT_PARAMETER_STATE| Indicates that the unsigned integer value in IPortableDeviceValues is a sensor state, such as SENSOR_STATE_READY.<br>**Note** To raise a state change event, call [ISensorClass Extension::PostStateChange](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-poststatechange). You do not have to explicitly specify SENSOR_EVENT_PARAMETER_STATE to raise the event.|

## Other Events

Sensor drivers raise all other types of events by calling the sensor class extension's [**ISensorClassExtension::PostEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-postevent) method. This method provides a generic, extensible way to raise sensor events unrelated to operating state. Each call to **PostEvent** contains a pointer to [IPortableDeviceValuesCollection](http://go.microsoft.com/fwlink/p/?linkid=131487). Each [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) object in this collection contains a **GUID** value for the SENSOR\_EVENT\_PARAMETER\_EVENT\_ID property, which identifies the event type, and optional data field values, which contain the event data. For example, a GPS driver that has new city data will use the SENSOR\_EVENT\_DATA\_UPDATED event ID and provide a string value for the SENSOR\_DATA\_TYPE\_CITY property key.

After your driver posts the event, the sensor class extension forwards the event and any associated data to the Sensor API.

You can find the definitions of platform-defined constants in the file named Sensors.h. For detailed information about platform-defined sensor constants, see [Constants](about-sensor-constants.md).

## Managing Sensor Driver Events

Before your driver accepts event requests, it should create a separate thread to generate and post events. By using a thread, you can help prevent frequent event procedures from blocking synchronous procedures, such as data request callbacks. For an example of a thread class that raises data-updated events, see [Raising Data-Updated Events](raising-events.md).

Your sensor should raise events only if at least one client application has requested event notifications. When an application requests event notifications, including for state-change events, the sensor class extension notifies the driver through [**ISensorDriver::OnClientSubscribeToEvents**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientsubscribetoevents). This method provides an [IWDFFile](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdffile) pointer that identifies the application and a string that identifies the sensor for which the application is requesting event notifications. You can use the IWDFFile pointer as a unique identifier to help keep track of applications that have subscribed to events. Although your sensor cannot raise events destined for specific clients, you will probably need to keep track of which application set which values for certain properties, such as SENSOR\_PROPERTY\_CURRENT\_REPORT\_INTERVAL or SENSOR\_PROPERTY\_CHANGE\_SENSITIVITY.

For example, if multiple client applications set different values for SENSOR\_PROPERTY\_CURRENT\_REPORT\_INTERVAL, you could apply a rule that sets the event frequency to the shortest interval that has been requested. However, your sensor may need to adjust the interval each time a new client subscribes to events or an existing client unsubscribes. For more information about report intervals, including example code, see [Filtering Data](filtering-data.md).

### Sensor Events and Data Privacy

Like other data requests, requests for event notifications are made secure through use of the sensor class extension. The class extension allows location data only for the user that requests this data.

>[!CAUTION]
> Make sure to use the sensor class extension to process all I/O requests for sensors. By doing this, you are less likely to reveal a user's private information.

 

For more information about data privacy, see [Privacy and Security in the Sensor and Location Platform](https://docs.microsoft.com/windows-hardware/drivers/gnss/privacy-and-security-in-the-sensor-and-location-platform)

## Related topics
[**Sensor Properties**](https://docs.microsoft.com/windows-hardware/drivers/sensors/sensor-properties)



