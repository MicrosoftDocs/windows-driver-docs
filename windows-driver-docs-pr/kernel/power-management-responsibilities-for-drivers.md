---
title: Power Management Responsibilities for Drivers
description: Power Management Responsibilities for Drivers
ms.assetid: c42a5b95-76f3-4975-b452-4858bbbe532e
keywords: ["power management WDK kernel , driver responsibilities", "driver power responsibilities WDk kernel", "conserving power WDK kernel", "power management WDK kernel , power states", "power states WDK kernel", "states WDK power management", "system power states WDK kernel , power management", "device power states WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Power Management Responsibilities for Drivers





Drivers that support power management are responsible for:

[Reporting device power capabilities](reporting-device-power-capabilities.md) during PnP enumeration.

[Setting device object flags for power management](setting-device-object-flags-for-power-management.md).

[Handling power IRPs](handling-power-irps.md) sent by the power manager or a driver.

[Powering up a device](powering-up-a-device.md) as soon as needed after system start-up or idle shutdown.

[Powering down a device](powering-down-a-device.md) at system shutdown time or putting it to sleep when idle.

[Enabling device wake-up](enabling-device-wake-up.md), if the device supports wake-up capabilities.

[Managing device performance states](managing-device-performance-states.md), if the device supports decreasing performance or features to reduce power consumption.

Not every driver in every device stack performs all of these tasks. Typically, the bus driver reports capabilities, sets flags, and manipulates the physical device, and the device power policy manager (usually the function driver) issues requests to put the device to sleep and to enable wake-up.

With few exceptions, drivers power on and power off their devices, and they enable devices for wake-up in response to power IRPs, that is, IRPs with the major code [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784). Power IRPs can be sent by the power manager and, in some cases, by a driver.

 

 




