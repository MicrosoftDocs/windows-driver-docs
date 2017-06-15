---
title: Disabling APCs
author: windows-driver-content
description: Disabling APCs
MS-HAID:
- 'Synchro\_fb5ec63e-39e6-4570-96c2-736da24eefa3.xml'
- 'kernel.disabling\_apcs'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0578df31-1467-4bad-ba62-081d61278deb
keywords: ["asynchronous procedure calls WDK kernel", "APCs WDK kernel", "disabling APCs", "critical regions WDK kernel", "guarded regions WDK kernel", "raising current IRQLs"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Disabling%20APCs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


