---
title: Using the sensor class extension to handle events
description: The sensor class extension handles the event-linkage between a sensor driver and the Sensor API.
ms.assetid: A49489EF-1721-4F12-9793-6FBA76BA7976
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the sensor class extension to handle events

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The sensor class extension handles the event-linkage between a sensor driver and the Sensor API.

Sensor applications retrieve the simulated-sensor's data fields by registering to receive event notifications from the driver; or, by invoking a property to retrieve a data field. The sample driver supports both.

If an application registers for data-update events, the driver raises these events every time that data arrives from the sensor. The frequency of these event notifications correspond to the current report-interval property.

In addition to raising events when the driver simulates "new" data arriving from the sensor, the sample driver also raises an event when the sensor is ready to start to send data. This event is known as a state-change event.

The state supported by the sample driver corresponds to a constant found in the **SensorState** enumeration:

| Event-State Constant | Significance                                                   |
|----------------------|----------------------------------------------------------------|
| SENSOR\_STATE\_READY | Indicates that the sensor is connected and ready to send data. |

 

As noted earlier, the sensor class extension handles the event-linkage between the sample driver and the Sensor API. Each time the driver invokes the **ISensorClassExtension::PostStateChange** method, the class extension forwards the notification to the API. The sample driver invokes this method within **CSensorManager::SetState**. When the driver invokes the **ISensorClassExtension::PostEvent** method and supplies the property key for the data-updated event, the class extension forwards the notification to the Sensor API. The sample driver invokes this method within **CSensorManager::PostDataEvent**.

The two sensor manager methods ::**SetState** and ::**PostDataEvent** are invoked within the sample driver’s thread procedure for events **CSensorManager::\_SensorEventThreadProc**. The event handlers are maintained in a separate thread procedure to prevent the event activity from blocking synchronous procedures in the driver (such as callback functions).

## Related topics
[The Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md)  



