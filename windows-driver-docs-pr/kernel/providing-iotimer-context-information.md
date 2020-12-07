---
title: Providing IoTimer Context Information
description: Providing IoTimer Context Information
keywords: ["IoTimer", "IoInitializeTimer"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Providing IoTimer Context Information





The *Context* pointer passed to [**IoInitializeTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializetimer) identifies a context area where other driver routines, and the [*IoTimer*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_timer_routine) routine itself, can maintain state about timed operations. The I/O manager passes the *Context* pointer whenever it calls the *IoTimer* routine.

Because an *IoTimer* routine is run at IRQL = DISPATCH\_LEVEL, its context area must be in resident, system-space memory. Most drivers that have *IoTimer* routines use the [device extension](device-extensions.md) of the associated device object as a *Context*-accessible area, but the context can instead be in a controller extension if the driver uses a [controller object](./introduction-to-controller-objects.md) or in nonpaged pool allocated by the driver.

**Follow these guidelines for an** *IoTimer***routine's context area:**

-   If the *IoTimer* routine shares its context area with the driver's ISR, it must use [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) to call a [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine that accesses the context area in a multiprocessor-safe manner. For more information, see [Using Critical Sections](using-critical-sections.md).

-   If the *IoTimer* routine does not share its context area with an ISR, but does share it with another driver routine, the driver must protect the shared context area with an initialized executive spin lock, in order to access the context information in a multiprocessor-safe manner. For more information, see [Spin Locks](./introduction-to-spin-locks.md).

 

