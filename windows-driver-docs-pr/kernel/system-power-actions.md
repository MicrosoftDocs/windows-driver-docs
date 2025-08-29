---
title: System Power Actions
description: System Power Actions
keywords: ["system power actions WDK power management", "system power states WDK kernel , power actions", "power actions WDK power management", "POWER_ACTION"]
ms.date: 08/26/2025
ms.topic: reference
---

# System power actions

When the power manager sends an IRP to set or query the system power state, it specifies a system power state. It also specifies another parameter that gives information about the power state change. This parameter, passed at **Irp->Parameters.Power.ShutdownType**, is an enumerator of the POWER_ACTION type. The enumerator characterizes the system power state request, as shown in the following table.

| POWER_ACTION enumerator | System power state requested |
| --- | --- |
| **PowerActionNone** | S0 or no system power IRP active |
| **PowerActionSleep** | S1, S2, or S3 |
| **PowerActionHibernate** | S4 |
| **PowerActionShutdown** (Windows 2000 and later) | S5 |
| **PowerActionShutdownReset** | S5 |
| **PowerActionShutdownOff** | S5 |

When a driver receives a system query or set-power IRP for S5, it can check **ShutdownType** For more information about the requested shutdown. A driver can use this information to optimize its shutdown sequence when the machine is resetting instead of shutting off power indefinitely. Drivers of most devices retain power when the system resets. However, for certain devices, such as a video streaming device that performs direct memory access (DMA), a driver might choose to power down its device when the system is resetting, thus stopping any ongoing I/O.

When a device power policy owner sends a *device* power IRP to its device stack in response to a system power IRP, drivers can use the **ShutdownType** parameter to get information about the current *system* power IRP. In this case, the value of **ShutdownType** indicates the currently requested system power state, or it's **PowerActionNone** if a system request isn't outstanding. Drivers shouldn't rely on this information if the device IRP requests state D0.

For more information, see [System power transition context for IRP_MN_SET_POWER](irp-mn-set-power.md#system-power-transition-context-for-irp_mn_set_power).
