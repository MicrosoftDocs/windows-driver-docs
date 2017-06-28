---
title: Architecture Overview for Sensor Drivers
author: windows-driver-content
description: Sensor device drivers are COM objects that are implemented by using the Windows User Mode Driver Framework (UMDF)
ms.assetid: 6d1b15ea-ba27-4bde-8000-d31f014ab47d
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Architecture Overview for Sensor Drivers


Sensor device drivers are COM objects that are implemented by using the Windows User Mode Driver Framework (UMDF). Sensor drivers use Windows Portable Devices (WPD) interfaces and other types as helper objects. Both UMDF and WPD are documented in the Windows Driver Kit documentation. For more information about UMDF drivers, see [User-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff561365). For more information about WPD types, see [Portable Devices](https://msdn.microsoft.com/library/windows/hardware/ff597901).

A sensor driver uses a special **class extension** object. The sensor class extension, a standard COM object, provides a standard implementation for handling I/O requests for sensor device drivers. Sensor drivers create the class extension object in the driver's process and then use the device driver interface (DDI) to forward I/O requests to and receive events from the class extension. The following diagram shows the relationship between a sensor, its driver, and the sensor class extension. (The sensor driver creates a new instance of the class extension for each sensor device.)

![umdf-based sensor driver that uses the sensor class extension](images/sensordriver-cxt.jpg)

For more information about the class extension object, see [About the Sensor Class Extension](about-the-sensor-class-extension.md).

**Important**  Sensor drivers must be free threaded and thread safe.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Architecture%20Overview%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


