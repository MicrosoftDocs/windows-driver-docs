---
title: Testing Sensor Data Retrieval
description: The Sensor Diagnostic Tool lets you test your driver and firmware support for data retrieval by invoking properties in the Sensor API.
ms.assetid: A4473253-D4AC-4374-9C5D-919B597FE2F0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing Sensor Data Retrieval


The Sensor Diagnostic Tool lets you test your driver and firmware support for data retrieval by invoking properties in the Sensor API.
 

## Configuring the Sensor Diagnostic Tool to retrieve a single sensor reading


The following procedure describes how to configure the diagnostic tool to retrieve an accelerometer reading.

1.  Expand the node for the accelerometer in the left Sensors pane. Check the **CONNECTED** box and uncheck the **SUBSCRIBED** box.
2.  Rotate the accelerometer and hold in place.
3.  Click the **Refresh Data/Execute** button and view the retrieved data in the Data section of the right pane.

The Data section of the right pane contains the updated data for your sensor. This data should correspond to the static position of the accelerometer.

## Configuring the Sensor Diagnostic Tool for synchronous polling


The following procedure describes how to configure the diagnostic tool to conduct synchronous polling of the accelerometer. In other words, this allows you to get a data reading from the sensor at a regular interval.

1.  Expand the node for the accelerometer in the left Sensors pane; check the **CONNECTED** box and uncheck the **SUBSCRIBED** box.
2.  In the **Automatic Data Request** textbox, enter your desired polling interval in milliseconds. (Note that an interval of zero disables synchronous polling.)

The Data section of the right pane will begin displaying the polled data. As you move the accelerometer, you should see new values in this pane.

You can log polled sensor data in a CSV file. See the [Testing Sensor Events](testing-sensor-events.md) topic and the "Logging Event Data to a CSV file" section for a description of how to do this.

You can specify which data should appear in the Data section of the tool with the **Datafield** dropdown that appears in the second row of controls in the right pane.

## Related topics
[Testing Sensor Functionality](testing-sensor-functionality.md)  
[Testing Sensor Property Support](testing-and-logging-sensor-data.md)  
[Testing Sensor Events](testing-sensor-events.md)  



