---
title: About ISensorDriver
description: About ISensorDriver
ms.assetid: 2c51c235-e402-4f89-bff5-39af87d95e19
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# About ISensorDriver


The sensor driver must implement the [ISensorDriver](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nn-sensorsclassextension-isensordriver) interface. Through this interface, the driver provides information about which sensor types, properties, data fields, and events the sensor supports, as well as the actual property values and sensor data. The class extension calls callback methods to process I/O requests, to specify the list of properties the API layer requests, to manage client connections, and to subscribe to events.

## Method to Enumerate Sensors

The class extension will always first enumerate the available sensors for the device by calling [**ISensorDriver::OnGetSupportedSensorObjects**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedsensorobjects). For each sensor, your driver must return an [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) object that contains a string ID (unique for the device) and other required property values.

## Methods to Manage Client Connections

To notify the driver about client applications that connect and disconnect, the sensor class extension calls [**ISensorDriver::OnClientConnect**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientconnect) and [**ISensorDriver::OnClientDisconnect**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientdisconnect). These callback methods pass two parameters: a pointer to an [IWDFFile](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdffile) interface and a sensor ID. Your driver should use this interface pointer as a unique ID to represent each client application. The sensor ID contains a string that identifies the sensor to which the client wants to connect or disconnect. These values are useful because you might want to maintain a list of clients and the sensors to which they connect so that you can manage settings on the sensor. For example, you might have a heuristic for how to set the current report interval when given conflicting values from multiple clients. You can also use this information to make decisions about power management. For example, if no clients are connected, you can put the sensor hardware into a power-saving mode.

## Methods to Manage Event Subscribers

The sensor class extension calls methods to help client applications manage events. [**ISensorDriver::OnGetSupportedEvents**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedevents) retrieves a list of events that the driver can raise. [**ISensorDriver::OnClientSubscribeToEvents**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientsubscribetoevents) and [**ISensorDriver::OnClientUnsubscribeFromEvents**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientunsubscribefromevents) provide notifications to the driver when a particular application has requested to receive or cancel event notifications. Only connected clients can subscribe to or unsubscribe from events.

## Methods to Manage Data and Properties

Client applications can also retrieve sensor data as **data fields**, or **properties** which contain metadata about the sensor device. To retrieve lists of supported data fields or properties, the sensor class extension calls [**ISensorDriver::OnGetSupportedDataFields**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupporteddatafields) or [**ISensorDriver::OnGetSupportedProperties**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedproperties). To retrieve data field or property values, the class extension calls [**ISensorDriver::OnGetDataFields**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetdatafields) or [**ISensorDriver::OnGetProperties**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetproperties). For properties that can be set, the class extension calls [**ISensorDriver::OnSetProperties**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-onsetproperties) to provide the new property values.

## Methods to Manage WPD Commands

When the sensor class extension has received an I/O control command through [**ISensorClassExtension::ProcessIoControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-processiocontrol) for which it does not provide a handler, it calls [**ISensorDriver::OnProcessWpdMessage**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsclassextension/nf-sensorsclassextension-isensordriver-onprocesswpdmessage). This callback method signals the driver that a WPD command has not been processed and gives the driver an opportunity to process the command. This means that you can create custom WPD commands and provide custom handlers in your driver, to extend sensor platform functionality.

 

 




