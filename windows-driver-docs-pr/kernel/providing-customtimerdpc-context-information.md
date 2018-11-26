---
title: Providing CustomTimerDpc Context Information
description: Providing CustomTimerDpc Context Information
ms.assetid: b4d711fb-63d4-45c6-8054-f934741ce340
keywords: ["timer objects WDK kernel , CustomTimerDpc routines", "CustomTimerDpc", "DeferredContext routine", "context information WDK synchronization", "timer objects WDK kernel , context information"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Providing CustomTimerDpc Context Information





The *DeferredContext* pointer passed to [**KeInitializeDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552130) points to a context area where other driver routines, and the *CustomTimerDpc* routine itself, can maintain state. The kernel passes the *DeferredContext* pointer in every call to the DPC routine.

Unlike an *IoTimer* routine, a *CustomTimerDpc* has no particular associations with a driver-created device object. However, a driver can associate a *CustomTimerDpc* routine with a driver-created device object by including a pointer to the device object in its context area.

The context area must be in resident, driver-allocated memory. Usually, this context area is in a device extension, but it can also be in nonpaged pool. If the driver uses a controller object, it can be in a controller extension. The contents of the context area are driver-determined.

If a *CustomTimerDpc* routine shares context information with the driver's ISR, the *CustomTimerDpc* routine must use [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call a *SynchCritSection* routine that accesses the shared context. For more information, see [Using Critical Sections](using-critical-sections.md).

If the *CustomTimerDpc* shares the context information with other non-ISR driver routines, the area at *DeferredContext* must be protected by an executive spin lock. For more information, see [Spin Locks](spin-locks.md).

 

 




