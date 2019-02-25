---
title: Supporting PnP and Power Management in Bus Drivers
description: Supporting PnP and Power Management in Bus Drivers
ms.assetid: 35a3d734-7d7e-46ee-aba6-fc6a579d4394
keywords:
- PnP WDK KMDF , bus drivers
- Plug and Play WDK KMDF , bus drivers
- power management WDK KMDF , bus drivers
- bus drivers WDK KMDF
- child devices WDK KMDF
- bus enumeration WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting PnP and Power Management in Bus Drivers


Some devices are permanently plugged into the system, while others can be plugged in and unplugged while the system is running. *Bus drivers* must identify and report the devices that are connected to their bus, and they must discover and report the arrival and departure of devices in the system.

The devices that a bus driver identifies and reports are called the bus's *child devices*. The process of identifying and reporting child devices is called *bus enumeration*. During bus enumeration, the bus driver [creates device objects](creating-a-framework-device-object.md) for its child devices. For more information about bus enumeration, see [Enumerating the Devices on a Bus](enumerating-the-devices-on-a-bus.md).

Bus drivers are essentially function drivers, or rarely a filter driver, that also handle bus enumeration. A bus driver is typically the function driver for the bus adapter, but it is not the function driver for the child devices that are connected to the bus.

Bus drivers also have the same PnP and power management responsibilities that function drivers have. For information about these responsibilities, see [Supporting PnP and Power Management in Function Drivers](supporting-pnp-and-power-management-in-function-drivers.md).

 

 





