---
title: Write and Deploy Your Universal Sensor Driver
description: This topic provides guidance on how to write and deploy your universal sensor driver, using the user mode driver framework (UMDF) version 2.
ms.date: 01/11/2024
---

# Write and deploy your universal sensor driver

This topic provides guidance on how to write and deploy your universal sensor driver, using the user mode driver framework (UMDF) version 2.

## Write a generic UMDF 2.0 driver

To build a generic UMDF 2.0 driver, see [Getting Started with Universal Windows Drivers](../develop/getting-started-with-windows-drivers.md), and follow the steps in the section titled [Building a Universal Windows driver](../develop/building-a-windows-driver.md), to build a Universal Windows driver using the **User Mode Driver (UMDF V2)** template.

## Customize the generic UMDF 2.0 driver files

When you develop and build this generic UMDF 2.0 driver, it will create quite a few boilerplate files, including the following:

- Header files, including *Device.h* and *Driver.h*
- Source files, including *Device.cpp* and *Driver.cpp*

When you customize this generic UMDF 2.0 driver, these are the goals you must keep in mind:

- [Make the driver loadable](make-the-driver-loadable.md)
- [Connect to hardware](connect-to-hardware.md)
- [Read data from hardware](read-data-from-hardware.md)

For code snippets, with explanations about how to make these updates, see the topics in the preceding list.

After updating the generic files to customize them for your sensor, see the following topics:

- [Review the INX file](review-and-revise-the-inf-file.md)
- [Build the sensor driver](build-the-sensor-driver.md)
- [Install the sensor driver](install-the-sensor-driver.md)
