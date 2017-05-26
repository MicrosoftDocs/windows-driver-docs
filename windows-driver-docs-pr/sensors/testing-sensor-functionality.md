---
title: Testing Sensor Functionality
author: windows-driver-content
description: You can use the Sensor Diagnostic Tool to test your sensor's functionality.
ms.assetid: 1AA232D9-D535-4168-926B-4667289EB7DB
keywords:
- testing sensors
- sensors, testing
- testing sensor functionality
- current report interval
- change sensitivity
- sensor events
- events, sensors
- testing sensor events
- testing sensor data retrieval
- testing sensor property support
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Testing Sensor Functionality


You can use the Sensor Diagnostic Tool to test your sensor's functionality. Use the tool to ensure that your driver and firmware correctly forwards data from the device, and correctly responds to requests from applications. In addition, you can use the tool to verify that your driver correctly supports changes to the current report interval and change sensitivity.
 

The Sensor platform (API and DDI) supports both event notifications and property retrieval.

-   A user can register to receive events (or notifications) from a device. The driver fires these events to all subscribers at the most restrictive subscriber's rate. Data can also be manually requested. For example, a game application can request to receive accelerometer event notifications twenty times a second, or subscribe to get updates whenever the driver fires events.
-   There are instances where an application retrieves sensor data by using a property rather than an event. For example, an application that controls brightness of a display may choose to only retrieve the current light level, after a human-presence sensor has detected the user's presence.

For a more complete description of events, change sensitivity (and their interrelationship), see the [Filtering data](filtering-data.md) topic. For information about using the Sensor Diagnostic Tool to test event handling, see the [Testing Sensor Events](testing-sensor-events.md) topic.

For information about using the Sensor Diagnostic tool to test property retrieval, see the [Testing Sensor Properties](testing-sensor-properties.md) topic.

## Related topics
[The Sensor Diagnostic Tool](the-sensor-diagnostic-tool.md)  
[Testing Sensor Events](testing-sensor-events.md)  
[Testing Sensor Properties](testing-sensor-properties.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Testing%20Sensor%20Functionality%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


