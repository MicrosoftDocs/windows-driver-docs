---
title: When Should Code and Data Be Pageable
description: When Should Code and Data Be Pageable
ms.assetid: 2804f558-8c8c-43f4-b14e-8deaac9da286
keywords: ["memory management WDK kernel , pageable drivers", "pageable drivers WDK kernel , when should be pageable", "locked-on-demand code WDK kernel", "spin locks WDK memory", "resident code WDK pageable drivers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# When Should Code and Data Be Pageable?





You can make all or part of your driver pageable. Paging driver code can reduce the size of the driver's load image, thus freeing system space for other uses. It is most practical for drivers of sporadically used devices, such as modems and CD-ROMs, or for parts of drivers that are rarely called.

Driver code that does any of the following must be memory-resident. That is, this code must be either in a nonpaged section, or in a paged section that is locked in memory when the code runs.

-   Runs at or above IRQL = DISPATCH\_LEVEL.

-   Acquires spin locks.

-   Calls any of the kernel's object support routines, such as [**KeReleaseMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553140) or [**KeReleaseSemaphore**](https://msdn.microsoft.com/library/windows/hardware/ff553143), in which the *Wait* parameter is set to **TRUE**. If the kernel is called with *Wait* set to **TRUE**, the call returns with IRQL at DISPATCH\_LEVEL.

Driver code must be running at IRQL &lt; DISPATCH\_LEVEL when the code does anything that might cause a page fault. Code can cause a page fault if it does any of the following:

-   Accesses paged pool that is not locked in memory.

-   Calls a pageable routine.

-   Accesses unlocked user buffers in the context of the user thread.

Typically, you should make a section paged if the total amount of all the pageable code (or data) is at least 4 kilobytes (KB). Whenever possible, you should isolate purely pageable code (or data) into a separate section from code (or data) that can sometimes be pageable but must sometimes be locked. For example, combining purely pageable code and locked-on-demand code causes more system space to be locked down for the combined section than is necessary. However, if a driver has less than 4 KB of possibly pageable code (or data), you might combine that code (or data) with locked-on-demand code (or data) into one section, saving system space.

 

 




