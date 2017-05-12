---
title: Testing Sensor Events
author: windows-driver-content
description: The Sensor Diagnostic Tool lets you test support for events in your driver and firmware.
ms.assetid: 92C067E0-3787-441E-8A2D-C48367ECE471
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Testing Sensor Events


The Sensor Diagnostic Tool lets you test support for events in your driver and firmware.
 

## Configuring the Sensor Diagnostic Tool to Capture Event Data


The following procedure describes how to configure the diagnostic tool to capture events for an accelerometer.

1.  Expand the node for the accelerometer in the left Sensors pane and make sure both the **CONNECTED** and **SUBSCRIBED** boxes are checked.
2.  In the **Events** menu make sure **Show Events** is checked.
3.  Select the Accelerometer node in the left pane.
4.  Rotate the device and view the event data in the right pane.

The following illustration shows the tool after it begins capturing accelerometer events.

![sensor diagnostic tool: capturing accelerometer events](images/sdt-events.png)


## Logging Event Data to an XML File


There are instances where you'll want to log your device's event data to a file rather than the tool's data pane. If this is necessary, follow these steps.

1.  Configure the Sensor Diagnostic Tool to capture event data (See the first section in this topic.)
2.  In the **Events** menu, choose the **Log Events** menu option.
3.  In the dialog that appears, specify the name of the log file and its location.
4.  Begin testing your device. For example, if it's an accelerometer, begin rotating, or moving, the sensor.

Your data will be logged to the file that you specified in step 3. XML logging is only supported for events, while CSV logging is enabled for both events and data retrieval.

## Logging Event Data to a CSV File


In addition to logging sensor data as XML, you can also log it in CSV files. If this is necessary, follow these steps. 

*Note:* You may need to run the program as an administrator for this to work properly.

1.  Configure the Sensor Diagnostic Tool to capture event data (See the first section in this topic.)
2.  In the **Sensors** menu, choose the **Enable CSV Logging** menu option.
3.  Begin testing your device. For example, if it's an accelerometer, begin rotating, or moving, the sensor.
4.  Once your tests are complete, uncheck the **Enable CSV Logging** menu option. This will stop logging and save your data to the output file. The files are placed into the same directory as the executable.

Your data will be logged to one or more CSV files. The tool creates a file for each connected sensor if a collection exists. CSV logging is supported for both events and data retrieval, while XML logging is only supported for events.

## Related topics
[Testing Sensor Functionality](testing-sensor-functionality.md)  
[Testing Sensor Data Retrieval](testing-sensor-properties.md)  
[Testing Sensor Property Support](testing-and-logging-sensor-data.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Testing%20Sensor%20Events%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


