---
title: When Should Code and Data Be Pageable
author: windows-driver-content
description: When Should Code and Data Be Pageable
MS-HAID:
- 'MemMgmt\_e95e5f54-28cc-414f-af76-8e225692c051.xml'
- 'kernel.when\_should\_code\_and\_data\_be\_pageable\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2804f558-8c8c-43f4-b14e-8deaac9da286
keywords: ["memory management WDK kernel , pageable drivers", "pageable drivers WDK kernel , when should be pageable", "locked-on-demand code WDK kernel", "spin locks WDK memory", "resident code WDK pageable drivers"]
---

# When Should Code and Data Be Pageable?


## <a href="" id="ddk-when-should-code-and-data-be-pageable-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20When%20Should%20Code%20and%20Data%20Be%20Pageable?%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


