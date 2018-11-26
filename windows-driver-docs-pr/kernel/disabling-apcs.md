---
title: Disabling APCs
description: Disabling APCs
ms.assetid: 0578df31-1467-4bad-ba62-081d61278deb
keywords: ["asynchronous procedure calls WDK kernel", "APCs WDK kernel", "disabling APCs", "critical regions WDK kernel", "guarded regions WDK kernel", "raising current IRQLs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Disabling APCs


The system provides three mechanisms to disable APCs for the current thread:

-   **Critical regions.** When a thread is inside a critical region, its user APCs and normal kernel APCs are not executed. Special kernel APCs are still executed. For more information about these APC types, see [Types of APCs](types-of-apcs.md).

-   **Guarded regions.** When a thread is inside a guarded region, none of its APCs are executed.

-   **Raising the current IRQL to APC\_LEVEL or higher.** A thread that is executing at IRQL &gt;= APC\_LEVEL executes with all APCs disabled.

Note that these settings apply to the current thread and do not affect the behavior of any other thread.

Some driver support routines must be called with particular kinds of APCs disabled. For example, routines that acquire an executive resource (such as [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)) must be called with normal kernel APCs disabled. Other routines must be called with particular kinds of APCs enabled. For example, any routine that relies on an I/O completion routine (such as [**IoVolumeDeviceToDosName**](https://msdn.microsoft.com/library/windows/hardware/ff550422)) must be called with special kernel APCs enabled. The documentation for each routine specifies if the routine has any particular restrictions on the state of APC execution.

A driver can explicitly enter a critical or guarded region by calling the appropriate routine. For more information, see [Critical Regions and Guarded Regions](critical-regions-and-guarded-regions.md). A driver can also explicitly raise the current IRQL to APC\_LEVEL by calling [**KeRaiseIrql**](https://msdn.microsoft.com/library/windows/hardware/ff553079). The driver must subsequently lower the IRQL to its original value by calling [**KeLowerIrql**](https://msdn.microsoft.com/library/windows/hardware/ff552968). Using a guarded region is faster than raising and lowering the current IRQL, but guarded regions are only available in Windows Server 2003 and later versions of Windows.

The following mutex operations have the same effect as entering or leaving a critical or guarded region or raising or lowering the current IRQL:

-   Holding a mutex object implicitly places the holder within a critical region.

-   Holding a guarded mutex implicitly places the holder within a guarded region.

-   Holding a fast mutex implicitly raises the current IRQL to APC\_LEVEL.

For more information about mutex objects, see [Mutex Objects](mutex-objects.md). For more information about fast and guarded mutexes, see [Fast Mutexes and Guarded Mutexes](fast-mutexes-and-guarded-mutexes.md).

 

 




