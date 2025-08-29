---
title: Power Manager
description: Power manager
keywords: ["power manager WDK kernel", "usage manager WDK power management", "power IRPs WDK kernel , power manager", "system-wide power policy WDK kernel", "power policy WDK kernel", "sleep power management WDK kernel", "hibernation power management WDK kernel", "shutdown power management WDK kernel"]
ms.date: 05/08/2025
ms.topic: concept-article
---

# Power manager

The power manager is responsible for managing power usage for the system. It administers the system-wide power policy and tracks the path of power IRPs through the system.

The power manager requests power operations by sending [**IRP_MJ_POWER**](./irp-mj-power.md) requests to drivers. A request can specify a new power state or can query whether a change in power state is feasible.

When :::no-loc text="sleep, hibernation":::, or :::no-loc text="shut down"::: is required, the power manager requests the appropriate power action by sending an **IRP_MJ_POWER** request to each leaf node in the device tree. The power manager considers the following conditions:

- System activity level

- System battery level

- :::no-loc text="Sleep, hibernation":::, or :::no-loc text="shut down"::: requests from applications

- User actions, such as pressing the power button

- Control panel settings

For more information, see [Windows Kernel-Mode Power Manager](windows-kernel-mode-power-manager.md).
