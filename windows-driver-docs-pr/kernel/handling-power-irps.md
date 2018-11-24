---
title: Handling Power IRPs
description: Handling Power IRPs
ms.assetid: 0fe4f27a-101d-41af-8f00-fb36da5dc793
keywords: ["power management WDK kernel , IRPs", "IRPs WDK power management", "power IRPs WDK kernel , about power IRPs", "IRP_MJ_POWER", "IRP_MN_QUERY_POWER", "IRP_MN_SET_POWER", "IRP_MN_WAIT_WAKE", "IRP_MN_POWER_SEQUENCE", "power states WDK kernel", "states WDK power management", "change power states WDK kernel", "conserving power WDK kernel", "sleep power management WDK kernel", "querying power state", "asleep devices WDK power management", "I/O request packets WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Power IRPs





Drivers handle power IRPs in a [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine. All power management requests have the major IRP code [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) and one of the following minor codes:

[**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) — Queries to determine whether changing power state is feasible

[**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) — Requests a change from one power state to another

[**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) — Requests that a device be enabled to wake itself or the system

[**IRP\_MN\_POWER\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/ff551644) — Requests information to optimize power restoration to a particular device

Support for **IRP\_MN\_SET\_POWER** and **IRP\_MN\_QUERY\_POWER** is required. All drivers must be prepared to handle these IRPs.

Support for **IRP\_MN\_WAIT\_WAKE** is required for all drivers in the device stack for any device that can awaken in response to an external signal. A driver sends this IRP to enable the device for wake-up.

Support for **IRP\_MN\_POWER\_SEQUENCE** is optional. This IRP provides an optimization for devices that take a long time to restore power.

A power IRP can specify a system power operation or a device power operation. [Power IRPs for the system](power-irps-for-the-system.md) and [power IRPs for individual devices](power-irps-for-individual-devices.md) take slightly different paths through a device stack, as explained in the following sections.

 

 




