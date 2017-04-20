---
title: Considerations for writing a sensor driver
author: windows-driver-content
description: Considerations for writing a sensor driver
ms.assetid: fec3cfe8-43ad-481a-833a-6f38d04bfdef
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Considerations for writing a sensor driver


You must consider the following key questions before you write a sensor driver. This process helps you make various design and implementation decisions.

-   Determine whether the driver supports multiple sensors or a single sensor. For example, your hardware device may contain a combination of sensors, but may use a single device driver.

-   Determine the level of interaction required on the device, and whether it will send events back to the platform. (Most drivers, and sensor solutions, will support events.) For an overview of sensor driver events, see [About Sensor Driver Events](about-sensor-driver-events.md).

-   Determine the category, sensor type, and data types for your driver. You can decide to use one of the platform-defined arrangements, or define your own. For an overview of how the platform organizes sensor information, see [About Sensor Constants](about-sensor-constants.md)

## Related topics
[The Sensors Geolocation Driver Sample](https://msdn.microsoft.com/library/windows/hardware/hh768273)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Considerations%20for%20writing%20a%20sensor%20driver%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


