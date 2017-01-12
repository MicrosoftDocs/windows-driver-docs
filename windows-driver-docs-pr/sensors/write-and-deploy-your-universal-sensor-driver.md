---
title: Write and deploy your universal sensor driver
description: This topic provides guidance on how to write and deploy your universal sensor driver, using the user mode driver framework (UMDF) version 2.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: FA888CB3-5B43-47CB-907D-76C6E6B6DE5D
---

# Write and deploy your universal sensor driver


This topic provides guidance on how to write and deploy your universal sensor driver, using the user mode driver framework (UMDF) version 2.

## Write a generic UMDF 2.0 driver


To build a generic UMDF 2.0 driver, see [Getting Started with Universal Windows Drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers), and follow the steps in the section titled **Building a Universal Windows driver**, to build a Universal Windows driver using the **User Mode Driver (UMDF V2)** template.

## Customize the generic UMDF 2.0 driver fies


When you develop and build this generic UMDF 2.0 driver, it will create quite a few boilerplate files, including the following:

-   Header files, including *Device.h* and *Driver.h*
-   Source files, including *Device.cpp* and *Driver.cpp*

When you customize this generic UMDF 2.0 driver, these are the goals you must keep in mind:

-   [Make the driver loadable](make-the-driver-loadable.md)
-   [Connect to hardware](connect-to-hardware.md)
-   [Read data from hardware](read-data-from-hardware.md)

For code snippets, with explanations about how to make these updates, see the topics in the preceding list.

After updating the generic files to customize them for your sensor, see the following topics:

-   [Review the INX file](review-and-revise-the-inf-file.md)
-   [Build the sensor driver](build-the-sensor-driver.md)
-   [Install the sensor driver](install-the-sensor-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Write%20and%20deploy%20your%20universal%20sensor%20driver%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




