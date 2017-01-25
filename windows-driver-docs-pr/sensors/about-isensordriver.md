---
title: About ISensorDriver
author: windows-driver-content
description: About ISensorDriver
MS-HAID:
- 'Sensor\_DG\_Overview\_868bd866-9d11-42c0-b7d4-3068fc665582.xml'
- 'sensors.about\_isensordriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2c51c235-e402-4f89-bff5-39af87d95e19
---

# About ISensorDriver


The sensor driver must implement the [ISensorDriver](https://msdn.microsoft.com/library/windows/hardware/ff545566) interface. Through this interface, the driver provides information about which sensor types, properties, data fields, and events the sensor supports, as well as the actual property values and sensor data. The class extension calls callback methods to process I/O requests, to specify the list of properties the API layer requests, to manage client connections, and to subscribe to events.

### Method to Enumerate Sensors

The class extension will always first enumerate the available sensors for the device by calling [**ISensorDriver::OnGetSupportedSensorObjects**](https://msdn.microsoft.com/library/windows/hardware/ff545633). For each sensor, your driver must return an [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) object that contains a string ID (unique for the device) and other required property values.

### Methods to Manage Client Connections

To notify the driver about client applications that connect and disconnect, the sensor class extension calls [**ISensorDriver::OnClientConnect**](https://msdn.microsoft.com/library/windows/hardware/ff545573) and [**ISensorDriver::OnClientDisconnect**](https://msdn.microsoft.com/library/windows/hardware/ff545580). These callback methods pass two parameters: a pointer to an [IWDFFile](https://msdn.microsoft.com/library/windows/hardware/ff558912) interface and a sensor ID. Your driver should use this interface pointer as a unique ID to represent each client application. The sensor ID contains a string that identifies the sensor to which the client wants to connect or disconnect. These values are useful because you might want to maintain a list of clients and the sensors to which they connect so that you can manage settings on the sensor. For example, you might have a heuristic for how to set the current report interval when given conflicting values from multiple clients. You can also use this information to make decisions about power management. For example, if no clients are connected, you can put the sensor hardware into a power-saving mode.

### Methods to Manage Event Subscribers

The sensor class extension calls methods to help client applications manage events. [**ISensorDriver::OnGetSupportedEvents**](https://msdn.microsoft.com/library/windows/hardware/ff545623) retrieves a list of events that the driver can raise. [**ISensorDriver::OnClientSubscribeToEvents**](https://msdn.microsoft.com/library/windows/hardware/ff545589) and [**ISensorDriver::OnClientUnsubscribeFromEvents**](https://msdn.microsoft.com/library/windows/hardware/ff545598) provide notifications to the driver when a particular application has requested to receive or cancel event notifications. Only connected clients can subscribe to or unsubscribe from events.

### Methods to Manage Data and Properties

Client applications can also retrieve sensor data as **data fields**, or **properties** which contain metadata about the sensor device. To retrieve lists of supported data fields or properties, the sensor class extension calls [**ISensorDriver::OnGetSupportedDataFields**](https://msdn.microsoft.com/library/windows/hardware/ff545620) or [**ISensorDriver::OnGetSupportedProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545630). To retrieve data field or property values, the class extension calls [**ISensorDriver::OnGetDataFields**](https://msdn.microsoft.com/library/windows/hardware/ff545607) or [**ISensorDriver::OnGetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545610). For properties that can be set, the class extension calls [**ISensorDriver::OnSetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545653) to provide the new property values.

### Methods to Manage WPD Commands

When the sensor class extension has received an I/O control command through [**ISensorClassExtension::ProcessIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff545536) for which it does not provide a handler, it calls [**ISensorDriver::OnProcessWpdMessage**](https://msdn.microsoft.com/library/windows/hardware/ff545644). This callback method signals the driver that a WPD command has not been processed and gives the driver an opportunity to process the command. This means that you can create custom WPD commands and provide custom handlers in your driver, to extend sensor platform functionality.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20About%20ISensorDriver%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


