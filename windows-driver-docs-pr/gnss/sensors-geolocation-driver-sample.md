---
title: Geolocation driver sample for Windows 8.1
description: The geolocation sample driver for Windows 8.1 demonstrates a sensor driver for a Global Positioning System (GPS) device.
keywords:
- GPS
- geolocation driver
- GPS driver
- radio management API
- radio-state change
- sensor driver
- UMDF sensor driver
ms.date: 08/25/2021
---

# Geolocation driver sample for Windows 8.1

> [!IMPORTANT]
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The geolocation sample driver for Windows 8.1 demonstrates a sensor driver for a Global Positioning System (GPS) device. This driver does not connect to hardware; otherwise, it is fully compliant with best practices for building a UMDF sensor driver. Instead of sending real coordinates, this sample simulates a sensor that issues altitude, latitude, longitude, and other simulated GPS data. In addition, this sample issues a timestamp that is useful when testing and debugging.

This sample serves three purposes: First, it demonstrates the minimal functionality required by a UMDF sensor driver. Second, it provides a skeleton on which you can build a working driver. Third, it includes support for the Radio Management API that provides notifications of radio-state changes for devices like a GPS.

## Related topics

[The Sensor Diagnostic Tool](../sensors/the-sensor-diagnostic-tool.md)
  
[Writing a Location Sensor Driver](writing-a-location-sensor-driver.md)
