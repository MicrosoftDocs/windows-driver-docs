---
title: Using the sensor class extension to handle events
author: windows-driver-content
description: The sensor class extension handles the event-linkage between a sensor driver and the Sensor API.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: A49489EF-1721-4F12-9793-6FBA76BA7976
---

# Using the sensor class extension to handle events


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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Using%20the%20sensor%20class%20extension%20to%20handle%20events%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


