---
title: Supporting PnP and Power Management in Bus Drivers
description: Supporting PnP and Power Management in Bus Drivers
ms.assetid: 35a3d734-7d7e-46ee-aba6-fc6a579d4394
keywords: ["PnP WDK KMDF , bus drivers", "Plug and Play WDK KMDF , bus drivers", "power management WDK KMDF , bus drivers", "bus drivers WDK KMDF", "child devices WDK KMDF", "bus enumeration WDK KMDF"]
---

# Supporting PnP and Power Management in Bus Drivers


Some devices are permanently plugged into the system, while others can be plugged in and unplugged while the system is running. *Bus drivers* must identify and report the devices that are connected to their bus, and they must discover and report the arrival and departure of devices in the system.

The devices that a bus driver identifies and reports are called the bus's *child devices*. The process of identifying and reporting child devices is called *bus enumeration*. During bus enumeration, the bus driver [creates device objects](creating-a-framework-device-object.md) for its child devices. For more information about bus enumeration, see [Enumerating the Devices on a Bus](enumerating-the-devices-on-a-bus.md).

Bus drivers are essentially function drivers, or rarely a filter driver, that also handle bus enumeration. A bus driver is typically the function driver for the bus adapter, but it is not the function driver for the child devices that are connected to the bus.

Bus drivers also have the same PnP and power management responsibilities that function drivers have. For information about these responsibilities, see [Supporting PnP and Power Management in Function Drivers](supporting-pnp-and-power-management-in-function-drivers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20PnP%20and%20Power%20Management%20in%20Bus%20Drivers%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




