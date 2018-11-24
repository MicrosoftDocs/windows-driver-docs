---
title: Providing IoTimer Context Information
description: Providing IoTimer Context Information
ms.assetid: a92a7c3d-1602-430b-8ae1-c79bfc9ac7f9
keywords: ["IoTimer", "IoInitializeTimer"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Providing IoTimer Context Information





The *Context* pointer passed to [**IoInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff549344) identifies a context area where other driver routines, and the [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine itself, can maintain state about timed operations. The I/O manager passes the *Context* pointer whenever it calls the *IoTimer* routine.

Because an *IoTimer* routine is run at IRQL = DISPATCH\_LEVEL, its context area must be in resident, system-space memory. Most drivers that have *IoTimer* routines use the [device extension](device-extensions.md) of the associated device object as a *Context*-accessible area, but the context can instead be in a controller extension if the driver uses a [controller object](using-controller-objects.md) or in nonpaged pool allocated by the driver.

**Follow these guidelines for an** *IoTimer***routine's context area:**

-   If the *IoTimer* routine shares its context area with the driver's ISR, it must use [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call a [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine that accesses the context area in a multiprocessor-safe manner. For more information, see [Using Critical Sections](using-critical-sections.md).

-   If the *IoTimer* routine does not share its context area with an ISR, but does share it with another driver routine, the driver must protect the shared context area with an initialized executive spin lock, in order to access the context information in a multiprocessor-safe manner. For more information, see [Spin Locks](spin-locks.md).

 

 




