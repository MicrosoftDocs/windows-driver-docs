---
title: Non-PnP Driver's Unload Routine
description: Non-PnP Driver's Unload Routine
ms.assetid: 5917648f-1e7e-4b39-9aa6-d6cdaac7a2cd
keywords: ["Unload routines WDK kernel , non-PnP drivers", "non-PnP Unload routine WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Non-PnP Driver's Unload Routine





Earlier drivers and high-level file system drivers, which do not handle PnP device-removal requests, must release resources, delete device objects, and detach from the device stack in their [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routines.

If it has not done so already, the first thing a legacy device driver should do in its *Unload* routine is to disable interrupts from the device. Otherwise, its ISR might be called to handle a device interrupt while the *Unload* routine is releasing resources in the device extension that the ISR needs to handle the interrupt. Even if its ISR runs successfully in these circumstances, the [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine that the ISR queues, and possibly other driver routines that run at IRQL &gt;= DISPATCH\_LEVEL, will execute before the *Unload* routine regains control, thereby increasing the likelihood that the *Unload* routine has deleted a resource that another driver routine references. See [Managing Hardware Priorities](managing-hardware-priorities.md) for more information.

After disabling interrupts, file system and legacy drivers must release resources and objects. For details, see the following two sections:

[Releasing Driver-Allocated Resources](releasing-driver-allocated-resources.md)

[Releasing Device and Controller Objects](releasing-device-and-controller-objects.md)

 

 




