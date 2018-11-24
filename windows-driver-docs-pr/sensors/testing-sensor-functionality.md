---
title: Testing Sensor Functionality
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
ms.date: 04/20/2017
ms.localizationpriority: medium
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



