---
title: Considerations for writing a sensor driver
description: Considerations for writing a sensor driver
ms.date: 04/20/2017
---

# Considerations for writing a sensor driver


You must consider the following key questions before you write a sensor driver. This process helps you make various design and implementation decisions.

-   Determine whether the driver supports multiple sensors or a single sensor. For example, your hardware device may contain a combination of sensors, but may use a single device driver.

-   Determine the level of interaction required on the device, and whether it will send events back to the platform. (Most drivers, and sensor solutions, will support events.) For an overview of sensor driver events, see [About Sensor Driver Events](about-sensor-driver-events.md).

-   Determine the category, sensor type, and data types for your driver. You can decide to use one of the platform-defined arrangements, or define your own. For an overview of how the platform organizes sensor information, see [About Sensor Constants](about-sensor-constants.md)

## Related topics
[The Sensors Geolocation Driver Sample](../gnss/sensors-geolocation-driver-sample.md)
