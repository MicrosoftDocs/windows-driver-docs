---
title: Geolocation driver sample for Windows 8.1
author: windows-driver-content
description: The geolocation sample driver for Windows 8.1 demonstrates a sensor driver for a Global Positioning System (GPS) device.
ms.assetid: 2675DB47-B973-419C-930D-1F1B9D65E42D
keywords:
- GPS
- geolocation driver
- GPS driver
- radio management API
- radio-state change
- sensor driver
- UMDF sensor driver
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Geolocation driver sample for Windows 8.1

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The geolocation sample driver for Windows 8.1 demonstrates a sensor driver for a Global Positioning System (GPS) device. This driver does not connect to hardware; otherwise, it is fully compliant with best practices for building a UMDF sensor driver. Instead of sending real coordinates, this sample simulates a sensor that issues altitude, latitude, longitude, and other simulated GPS data. In addition, this sample issues a timestamp that is useful when testing and debugging.

This sample serves three purposes: First, it demonstrates the minimal functionality required by a UMDF sensor driver. Second, it provides a skeleton on which you can build a working driver. Third, it includes support for the Radio Management API that provides notifications of radio-state changes for devices like a GPS.

## Related topics
[The Sensor Diagnostic Tool](https://msdn.microsoft.com/library/windows/hardware/hh780319)  
[Writing a Location Sensor Driver](writing-a-location-sensor-driver.md)  
[Writing a Sensor Device Driver](https://msdn.microsoft.com/library/windows/hardware/ff545927)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Geolocation%20driver%20sample%20for%20Windows%208.1%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


