---
title: Sending a Wait/Wake IRP
description: Sending a Wait/Wake IRP
ms.assetid: ed582644-af51-4841-be59-6a3deb6d9de5
keywords: ["power management WDK kernel , wake-up capabilities", "external wake signals WDK", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management", "IRP_MN_WAIT_WAKE", "wait/wake IRPs WDK power management , sending", "sending wait/wake IRPs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Sending a Wait/Wake IRP





The minor power IRP code [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) provides for waking a device or waking the system. Drivers of devices that can wake themselves or the system send **IRP\_MN\_WAIT\_WAKE** requests. The system sends **IRP\_MN\_WAIT\_WAKE** requests only to devices that always wake the system, such as the power-on switch.

A driver sends an **IRP\_MN\_WAIT\_WAKE** request for one of two reasons:

1.  Its device must be able to return to the working state from a sleep state in response to an external wake-up signal.

    For example, a modem's driver might send it a wait/wake IRP before setting it in power state D1 to conserve energy. The wait/wake IRP enables the modem to respond to an incoming call.

2.  Its device must be able to wake the system in response to a wake-up signal.

    When the system goes to sleep, the modem might remain in state D1 with an **IRP\_MN\_WAIT\_WAKE** pending. In this case, an incoming call would wake the system as well as the modem.

Whether a device is prepared to wake itself or the system, the actions its drivers must take are the same. The primary difference lies in how the device and system hardware respond to the initial wake-up signal. Driver behavior is the same in either case.

 

 




