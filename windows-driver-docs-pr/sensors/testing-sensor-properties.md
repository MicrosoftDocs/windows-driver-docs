---
title: Testing Sensor Data Retrieval
author: windows-driver-content
description: The Sensor Diagnostic Tool lets you test your driver and firmware support for data retrieval by invoking properties in the Sensor API.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: A4473253-D4AC-4374-9C5D-919B597FE2F0
---

# Testing Sensor Data Retrieval


The Sensor Diagnostic Tool lets you test your driver and firmware support for data retrieval by invoking properties in the Sensor API.

**Note**  The Sensor Diagnostic Tool is acceptable for testing on Windows 8.1 and earlier operating systems. The tool is now deprecated for Windows 10, so for sensor driver testing and diagnostics on Windows 10 and later operating systems, please use the SensorInfo App from the Windows Store.

 

## Configuring the Sensor Diagnostic Tool to retrieve a single sensor reading


The following procedure describes how to configure the diagnostic tool to retrieve an accelerometer reading.

1.  Expand the node for the accelerometer in the left Sensors pane and check the **CONNECTED** box.
2.  Rotate the accelerometer and hold in place.
3.  Click the **Refresh Data/Execute** button and view the retrieved data in the Data section of the right pane.

The Data section of the right pane contains the updated data for your sensor. This data should correspond to the static position of the accelerometer.

## Configuring the Sensor Diagnostic Tool for synchronous polling


The following procedure describes how to configure the diagnostic tool to conduct synchronous polling of the accelerometer.

1.  Expand the node for the accelerometer in the left Sensors pane; check the **CONNECTED** box and uncheck the **SUBSCRIBED** box.
2.  In the **Automatic Data Request** textbox, enter your desired polling interval in milliseconds. (Note that an interval of zero disables synchronous polling.)

The Data section of the right pane will begin displaying the polled data. As you move the accelerometer, you should see new values in this pane.

You can log polled sensor data in a CSV file. See the [Testing Sensor Events](testing-sensor-events.md) topic and the "Logging Event Data to a CSV file" section for a description of how to do this.

You can specify which data should appear in the Data section of the tool with the **Datafield** dropdown that appears in the second row of controls in the right pane.

## Related topics
[Testing Sensor Functionality](testing-sensor-functionality.md)  
[Testing Sensor Property Support](testing-and-logging-sensor-data.md)  
[Testing Sensor Events](testing-sensor-events.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Testing%20Sensor%20Data%20Retrieval%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


