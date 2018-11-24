---
title: Supporting Devices that Have Wake-Up Capabilities
description: Supporting Devices that Have Wake-Up Capabilities
ms.assetid: 70b9d0af-c3d7-44dc-b11a-3274391508c5
keywords: ["power management WDK kernel , wake-up capabilities", "external wake signals WDK", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management", "IRP_MN_WAIT_WAKE", "restoring power WDK kernel", "IRPs WDK power management", "wait/wake IRPs WDK power management", "I/O request packets WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Supporting Devices that Have Wake-Up Capabilities





Drivers for devices that can respond to external wake signals must be able to handle [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) requests (*wait/wake IRPs*). The power policy owner for such a device must be able to send an **IRP\_MN\_WAIT\_WAKE** request.

Typically, whatever causes the device to assert the wake signal is also a normal service event for the device. For example, user input, which might cause a keyboard to wake up the system, is a normal event for the keyboard and its drivers.

The first topic of this section, [Overview of Wait/Wake Operation](overview-of-wait-wake-operation.md), contains information useful in writing any driver. The following additional topics provide detailed information about handling and sending wait/wake IRPs:

[Receiving a Wait/Wake IRP](receiving-a-wait-wake-irp.md)

[Sending a Wait/Wake IRP](sending-a-wait-wake-irp.md)

[Canceling a Wait/Wake IRP](canceling-a-wait-wake-irp.md)

 

 




