---
title: Supporting PnP and Power Management in Your Driver
description: Supporting PnP and Power Management in Your Driver
ms.assetid: d9cf987f-d994-4ea9-a467-4b1b8bcdc456
keywords:
- PnP WDK KMDF , about PnP in framework-based drivers
- Plug and Play WDK KMDF , about PnP in framework-based drivers
- power management WDK KMDF , about power management
- device objects WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting PnP and Power Management in Your Driver


By default, the framework handles all PnP and power management requests that the system sends to framework-based drivers. Additionally, by default, the framework delivers I/O requests to a function driver only if the driver's hardware is available and in its working (D0) state.

When writing a framework-based driver, you can use much of the framework's default behavior to easily support the PnP and power management capabilities of your device. However, if all of the drivers in your driver stack used only the framework's default PnP and power management behavior, your device probably would not work properly. For example, the device's function driver might have to enable the device when the device enters its working (D0) state.

Therefore, the framework device object provides a set of event callback functions and a set of object methods that enable framework-based drivers to participate in PnP and power management operations. These callback functions and object methods allow each driver in the stack to provide only the PnP and power management support that is necessary.

Typically, each of the various drivers in a driver stack is responsible for supporting a few PnP and power management operations. The operations that a driver must support depend on the type of driver that you are writing and the capabilities that the device provides. For more information about which operations your driver should support, see:

-   [Supporting PnP and Power Management in Software-only Drivers](supporting-pnp-and-power-management-in-software-only-drivers.md)
-   [Supporting PnP and Power Management in Function Drivers](supporting-pnp-and-power-management-in-function-drivers.md)

 

 





