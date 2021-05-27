---
title: About ISensorDriver
description: About ISensorDriver
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# About ISensorDriver


The sensor driver must implement the [ISensorDriver](/windows-hardware/drivers/ddi/sensorsclassextension/nn-sensorsclassextension-isensordriver) interface. Through this interface, the driver provides information about which sensor types, properties, data fields, and events the sensor supports, as well as the actual property values and sensor data. The class extension calls callback methods to process I/O requests, to specify the list of properties the API layer requests, to manage client connections, and to subscribe to events.

## Method to Enumerate Sensors

The class extension will always first enumerate the available sensors for the device by calling [**ISensorDriver::OnGetSupportedSensorObjects**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedsensorobjects). For each sensor, your driver must return an [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues) object that contains a string ID (unique for the device) and other required property values.

## Methods to Manage Client Connections

To notify the driver about client applications that connect and disconnect, the sensor class extension calls [**ISensorDriver::OnClientConnect**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientconnect) and [**ISensorDriver::OnClientDisconnect**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientdisconnect). These callback methods pass two parameters: a pointer to an [IWDFFile](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile) interface and a sensor ID. Your driver should use this interface pointer as a unique ID to represent each client application. The sensor ID contains a string that identifies the sensor to which the client wants to connect or disconnect. These values are useful because you might want to maintain a list of clients and the sensors to which they connect so that you can manage settings on the sensor. For example, you might have a heuristic for how to set the current report interval when given conflicting values from multiple clients. You can also use this information to make decisions about power management. For example, if no clients are connected, you can put the sensor hardware into a power-saving mode.

## Methods to Manage Event Subscribers

The sensor class extension calls methods to help client applications manage events. [**ISensorDriver::OnGetSupportedEvents**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedevents) retrieves a list of events that the driver can raise. [**ISensorDriver::OnClientSubscribeToEvents**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientsubscribetoevents) and [**ISensorDriver::OnClientUnsubscribeFromEvents**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientunsubscribefromevents) provide notifications to the driver when a particular application has requested to receive or cancel event notifications. Only connected clients can subscribe to or unsubscribe from events.

## Methods to Manage Data and Properties

Client applications can also retrieve sensor data as **data fields**, or **properties** which contain metadata about the sensor device. To retrieve lists of supported data fields or properties, the sensor class extension calls [**ISensorDriver::OnGetSupportedDataFields**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupporteddatafields) or [**ISensorDriver::OnGetSupportedProperties**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedproperties). To retrieve data field or property values, the class extension calls [**ISensorDriver::OnGetDataFields**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetdatafields) or [**ISensorDriver::OnGetProperties**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetproperties). For properties that can be set, the class extension calls [**ISensorDriver::OnSetProperties**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-onsetproperties) to provide the new property values.

## Methods to Manage WPD Commands

When the sensor class extension has received an I/O control command through [**ISensorClassExtension::ProcessIoControl**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-processiocontrol) for which it does not provide a handler, it calls [**ISensorDriver::OnProcessWpdMessage**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-onprocesswpdmessage). This callback method signals the driver that a WPD command has not been processed and gives the driver an opportunity to process the command. This means that you can create custom WPD commands and provide custom handlers in your driver, to extend sensor platform functionality.

