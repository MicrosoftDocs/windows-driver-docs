---
title: Bluetooth Universal Windows driver model for Windows 10
description: In Windows 10, the Bluetooth transport driver interface for all devices is converged and uses the Universal Windows driver model.
ms.date: 09/14/2021
---

# Bluetooth Universal Windows driver model for Windows 10

In Windows 10, the Bluetooth transport driver interface for all devices is converged and uses the Universal Windows driver model. You can write a single driver that runs on all Windows device platforms.

The Bluetooth audio driver surface area is diverged for Windows 10 and allows the following two options:

* You can write a new audio Universal Windows driver that works for both desktop and mobile devices.
* An existing Windows Phone 8.1 Bluetooth audio driver will run on Windows 10 Mobile.

## How to write a Bluetooth Universal Windows driver

To write a Bluetooth Universal Windows driver, see [Getting Started with Universal Windows drivers](/windows-hardware/drivers), and follow the steps in the section titled *Building a Universal Windows driver* to build a Universal Windows driver using the Kernel Mode Driver (KMDF) template.

Then, see the Bluetooth design and reference sections for implementation guidance.

* [Bluetooth profile drivers](bluetooth-profile-drivers-overview.md)
* [Bluetooth Devices Reference](/windows/win32/api/_bltooth/)
