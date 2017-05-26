---
title: Testing Sensor Property Support
author: windows-driver-content
description: Use the Sensor Diagnostic Tool to test whether your driver and firmware support property retrieval.
ms.assetid: 6E8C2162-F7BD-4544-8869-00FA4E4925E0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Testing%20Sensor%20Property%20Support%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


