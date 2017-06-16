---
title: Handling Power IRPs
author: windows-driver-content
description: Handling Power IRPs
ms.assetid: 0fe4f27a-101d-41af-8f00-fb36da5dc793
keywords: ["power management WDK kernel , IRPs", "IRPs WDK power management", "power IRPs WDK kernel , about power IRPs", "IRP_MJ_POWER", "IRP_MN_QUERY_POWER", "IRP_MN_SET_POWER", "IRP_MN_WAIT_WAKE", "IRP_MN_POWER_SEQUENCE", "power states WDK kernel", "states WDK power management", "change power states WDK kernel", "conserving power WDK kernel", "sleep power management WDK kernel", "querying power state", "asleep devices WDK power management", "I/O request packets WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Power IRPs


## <a href="" id="ddk-handling-power-irps-kg"></a>


Drivers handle power IRPs in a [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine. All power management requests have the major IRP code [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) and one of the following minor codes:

[**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) — Queries to determine whether changing power state is feasible

[**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) — Requests a change from one power state to another

[**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) — Requests that a device be enabled to wake itself or the system

[**IRP\_MN\_POWER\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/ff551644) — Requests information to optimize power restoration to a particular device

Support for **IRP\_MN\_SET\_POWER** and **IRP\_MN\_QUERY\_POWER** is required. All drivers must be prepared to handle these IRPs.

Support for **IRP\_MN\_WAIT\_WAKE** is required for all drivers in the device stack for any device that can awaken in response to an external signal. A driver sends this IRP to enable the device for wake-up.

Support for **IRP\_MN\_POWER\_SEQUENCE** is optional. This IRP provides an optimization for devices that take a long time to restore power.

A power IRP can specify a system power operation or a device power operation. [Power IRPs for the system](power-irps-for-the-system.md) and [power IRPs for individual devices](power-irps-for-individual-devices.md) take slightly different paths through a device stack, as explained in the following sections.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Power%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


