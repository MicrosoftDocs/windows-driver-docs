---
title: Testing Location Functionality
description: The Sensor Diagnostic Tool includes a separate Location tab that logs properties that are specific to location.
ms.assetid: A96AF9C7-69FA-492C-941E-4E296488875C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing Location Functionality


The Sensor Diagnostic Tool includes a separate Location tab that logs properties that are specific to location. These properties include Latitude, Longitude, and Civic Address.

>[!NOTE]
> The Sensor Diagnostic Tool is acceptable for testing on Windows 8.1 and earlier operating systems. The tool is now deprecated for Windows 10, so for sensor driver testing and diagnostics on Windows 10 and later operating systems, please use the SensorInfo App from the Microsoft Store.



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



