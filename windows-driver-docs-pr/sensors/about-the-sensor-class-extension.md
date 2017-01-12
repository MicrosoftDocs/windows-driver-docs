---
title: About the Sensor Class Extension
description: About the Sensor Class Extension
MS-HAID:
- 'Sensor\_DG\_Overview\_ac0d731d-47e8-41a8-9cdf-631be87b3c7b.xml'
- 'sensors.about\_the\_sensor\_class\_extension'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4b55e5fe-2947-4511-ba2d-479d5fd83ebe
---

# About the Sensor Class Extension


To make it easier to write a device driver that exposes a sensor to Windows (and to the sensor and location platform in particular), Windows includes a sensor driver class extension. A required component for sensor device drivers, this COM object provides a simple set of interfaces that enable programmers to implement a sensor driver without writing lots of boilerplate code. Additionally, this class extension provides the following benefits:

-   Helps to ensure that user privacy is well protected because the class extension enforces appropriate access control restrictions for sensors that handle personal information.

-   Provides a standard way to retrieve data from the driver and to raise event notifications through the API layers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20About%20the%20Sensor%20Class%20Extension%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




