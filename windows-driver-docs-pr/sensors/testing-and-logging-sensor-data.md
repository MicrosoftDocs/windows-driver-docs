---
title: Testing Sensor Property Support
description: Use the Sensor Diagnostic Tool to test whether your driver and firmware support property retrieval.
ms.assetid: 6E8C2162-F7BD-4544-8869-00FA4E4925E0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing Sensor Property Support


Use the Sensor Diagnostic Tool to test whether your driver and firmware support property retrieval. The tool invokes properties in the Sensor API to determine whether you support property retrieval.
 

## Configuring the Sensor Diagnostic Tool to Retrieve Sensor Properties


To configure the diagnostic tool, so that it can retrieve the properties for an accelerometer, do the following:

1.  Expand the node for the accelerometer in the left Sensors pane and check the **CONNECTED** box.
2.  Click the accelerometer node in the left Sensors pane.

The Properties section of the right pane contains the updated property data for your sensor. This data corresponds to the properties supported by your device.

The [Testing Sensor Events](testing-sensor-events.md) topic describes how to test whether your driver and firmware support change sensitivity and the current report interval. Refer to these sections to understand how you can use the tool to alter these settings while you test support for properties.

## Related topics
[Testing Sensor Functionality](testing-sensor-functionality.md)  
[Testing Sensor Data Retrieval](testing-sensor-properties.md)  
[Testing Sensor Events](testing-sensor-events.md)  



