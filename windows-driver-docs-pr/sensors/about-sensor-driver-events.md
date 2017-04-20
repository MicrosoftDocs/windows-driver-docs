---
title: About Sensor Driver Events
author: windows-driver-content
description: About Sensor Driver Events
ms.assetid: 1e747743-f701-4854-92be-7b55c39fee08
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# About Sensor Driver Events


Applications can receive information from sensors in two ways: synchronously, by requesting a particular property or data field, or asynchronously, by subscribing to an event that is raised by the sensor driver.

Sensor drivers can raise **state change events**, which notify applications about a transition in the device to a new operational condition, and other kinds of event notifications. Your driver should raise separate events for each sensor that your device provides.

**Note**  Do not use [**IWDFDevice::PostEvent**](https://msdn.microsoft.com/library/windows/hardware/ff558835) to raise sensor events. The sensor platform will not forward such events to the connected client programs.

 

### State Change Events

Sensor drivers raise state change events by calling the sensor class extension's [**ISensorClassExtension::PostStateChange**](https://msdn.microsoft.com/library/windows/hardware/ff545523) method. For example, a driver that has finished initializing a sensor will call this method to signal the new [**SensorState**](https://msdn.microsoft.com/library/windows/hardware/ff545708) value named SENSOR\_STATE\_READY.

### Other Events

Sensor drivers raise all other types of events by calling the sensor class extension's [**ISensorClassExtension::PostEvent**](https://msdn.microsoft.com/library/windows/hardware/ff545519) method. This method provides a generic, extensible way to raise sensor events unrelated to operating state. Each call to **PostEvent** contains a pointer to [IPortableDeviceValuesCollection](http://go.microsoft.com/fwlink/p/?linkid=131487). Each [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) object in this collection contains a **GUID** value for the SENSOR\_EVENT\_PARAMETER\_EVENT\_ID property, which identifies the event type, and optional data field values, which contain the event data. For example, a GPS driver that has new city data will use the SENSOR\_EVENT\_DATA\_UPDATED event ID and provide a string value for the SENSOR\_DATA\_TYPE\_CITY propertykey.

After your driver posts the event, the sensor class extension forwards the event and any associated data to the Sensor API.

You can find the definitions of platform-defined constants in the file named Sensors.h. For detailed information about platform-defined sensor constants, see [Constants](https://msdn.microsoft.com/library/windows/hardware/ff545409).

### Managing Sensor Driver Events

Before your driver accepts event requests, it should create a separate thread to generate and post events. By using a thread, you can help prevent frequent event procedures from blocking synchronous procedures, such as data request callbacks. For an example of a thread class that raises data-updated events, see [Raising Data-Updated Events](raising-events.md).

Your sensor should raise events only if at least one client application has requested event notifications. When an application requests event notifications, including for state-change events, the sensor class extension notifies the driver through [**ISensorDriver::OnClientSubscribeToEvents**](https://msdn.microsoft.com/library/windows/hardware/ff545589). This method provides an [IWDFFile](https://msdn.microsoft.com/library/windows/hardware/ff558912) pointer that identifies the application and a string that identifies the sensor for which the application is requesting event notifications. You can use the IWDFFile pointer as a unique identifier to help keep track of applications that have subscribed to events. Although your sensor cannot raise events destined for specific clients, you will probably need to keep track of which application set which values for certain properties, such as SENSOR\_PROPERTY\_CURRENT\_REPORT\_INTERVAL or SENSOR\_PROPERTY\_CHANGE\_SENSITIVITY.

For example, if multiple client applications set different values for SENSOR\_PROPERTY\_CURRENT\_REPORT\_INTERVAL, you could apply a rule that sets the event frequency to the shortest interval that has been requested. However, your sensor may need to adjust the interval each time a new client subscribes to events or an existing client unsubscribes. For more information about report intervals, including example code, see [Filtering Data](filtering-data.md).

### Sensor Events and Data Privacy

Like other data requests, requests for event notifications are made secure through use of the sensor class extension. The class extension allows location data only for the user that requests this data.

**Caution**  Make sure to use the sensor class extension to process all I/O requests for sensors. By doing this, you are less likely to reveal a user's private information.

 

For more information about data privacy, see [Privacy and Security in the Sensor and Location Platform](https://msdn.microsoft.com/library/windows/hardware/ff545686)

## Related topics
[**Sensor Properties**](https://msdn.microsoft.com/library/windows/hardware/ff545859)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20About%20Sensor%20Driver%20Events%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


