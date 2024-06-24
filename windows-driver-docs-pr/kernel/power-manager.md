---
title: Power Manager
description: Power Manager
keywords: ["power manager WDK kernel", "usage manager WDK power management", "power IRPs WDK kernel , power manager", "system-wide power policy WDK kernel", "power policy WDK kernel", "sleep power management WDK kernel", "hibernation power management WDK kernel", "shutdown power management WDK kernel"]
ms.date: 06/06/2024
---

# Power Manager





The power manager is responsible for managing power usage for the system. It administers the system-wide power policy and tracks the path of power IRPs through the system.

The power manager requests power operations by sending [**IRP\_MJ\_POWER**](./irp-mj-power.md) requests to drivers. A request can specify a new power state or can query whether a change in power state is feasible.

When :::no-loc text="sleep, hibernation":::, or :::no-loc text="shut down"::: is required, the power manager requests the appropriate power action by sending an **IRP\_MJ\_POWER** request to each leaf node in the device tree. The power manager considers the following:

-   System activity level

-   System battery level

-   :::no-loc text="Sleep, hibernation":::, or :::no-loc text="shut down"::: requests from applications

-   User actions, such as pressing the power button

-   Control panel settings

For more information, see [Windows Kernel-Mode Power Manager](windows-kernel-mode-power-manager.md).

 

