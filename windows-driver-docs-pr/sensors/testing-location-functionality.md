---
title: Testing Location Functionality
author: windows-driver-content
description: The Sensor Diagnostic Tool includes a separate Location tab that logs properties that are specific to location. These properties include Latitude, Longitude, and Civic Address.
ms.assetid: A96AF9C7-69FA-492C-941E-4E296488875C
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Testing Location Functionality


The Sensor Diagnostic Tool includes a separate Location tab that logs properties that are specific to location. These properties include Latitude, Longitude, and Civic Address.

**Note**  The Sensor Diagnostic Tool is acceptable for testing on Windows 8.1 and earlier operating systems. The tool is now deprecated for Windows 10, so for sensor driver testing and diagnostics on Windows 10 and later operating systems, please use the SensorInfo App from the Windows Store.

 

## Configuring the Sensor Diagnostic Tool to Capture Location Data


The following procedure describes how to configure the Sensor Diagnostic Tool to capture events for the Windows Location Provider.

1.  Expand the node for the Windows Location Provider in the left Sensors pane and check the **CONNECTED** and **SUBSCRIBED** boxes.
2.  Click the Windows Location Provider node.

After you click the node, the **Properties** and **Data** tabs in the right pane update with location data.

## Tracking Location Data


After you configure the Sensor Diagnostic Tool to capture location data (see the previous section in this topic), you can begin viewing specific properties and data by using the **Location** tab.

1.  Open the **Location** tab.
2.  To view latitude and longitude values, click the LatLong node in the left pane.
3.  To view a civic address, click the CivicAddress node in the left pane.

## Related topics
[The Sensor Diagnostic Tool](the-sensor-diagnostic-tool.md)  
[Testing Sensor Functionality](testing-sensor-functionality.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Testing%20Location%20Functionality%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


