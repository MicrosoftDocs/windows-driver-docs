---
title: Allocating System-Space Memory
description: Allocating System-Space Memory
ms.assetid: eee425b3-6ddd-4e9d-b51d-1f2c9ea106a5
keywords: ["memory management WDK kernel , system-allocated space", "system-allocated space WDK kernel", "allocating system-space memory", "allocating I/O buffer memory", "I/O buffer memory allocations WDK kernel", "buffer memory allocations WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Allocating System-Space Memory





Drivers can use system-allocated space within their [device extensions](device-extensions.md) as global storage areas for device-specific information. Drivers can use only the kernel stack to pass small amounts of data to their internal routines. Some drivers have to allocate additional, larger amounts of system-space memory, typically for I/O buffers.

To allocate I/O buffer space, the best memory allocation routines to use are [**MmAllocateNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554479), [**MmAllocateContiguousMemorySpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff554464), [**AllocateCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff540575) (if the driver's device uses bus-master DMA or a system DMA controller's auto-initialize mode), or [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520).

Nonpaged pool typically becomes fragmented as the system runs, so a driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine should call these routines to set up any long-term I/O buffers the driver needs. Each of these routines, except [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520), allocates memory that is aligned on a processor-specific boundary (determined by the processor's data-cache-line size) to provide best performance.

Drivers should allocate I/O buffers as economically as possible, because nonpaged pool memory is a limited system resource. Typically, a driver should avoid calling these support routines repeatedly to request allocations of less than PAGE\_SIZE because each allocation that is less than PAGE\_SIZE also comes with a pool header that is used to internally manage the allocation.

### Tips for Allocating Driver Buffer Space Economically

To allocate I/O buffer memory economically, be aware of the following:

-   Each call to [**MmAllocateNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554479) or [**MmAllocateContiguousMemorySpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff554464) always returns a full multiple of the system's page size, of nonpaged system-space memory, whatever the size of the requested allocation. Therefore, requests for less than a page are rounded up to a full page and any remainder bytes on the page are wasted; they are inaccessible by the driver that called the function and are unusable by other kernel-mode code.

-   Each call to [**AllocateCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff540575) uses at least one adapter object map register, which maps at least one byte and at most one page. For more information about map registers and using common buffers, see [Adapter Objects and DMA](adapter-objects-and-dma.md).

### Allocating Memory with ExAllocatePoolWithTag

Drivers can also call [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520), specifying one of the following system-defined [**POOL\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559707) values for the *PoolType* parameter:

-   *PoolType* = **NonPagedPool** for any objects or resources not stored in a device extension or controller extension that the driver might access while it is running at IRQL &gt; APC\_LEVEL.

    For this *PoolType* value, [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) allocates the amount of memory that is requested if the specified *NumberOfBytes* is less than or equal to PAGE\_SIZE. Otherwise, any remainder bytes on the last-allocated page are wasted: inaccessible to the caller and unusable by other kernel-mode code.

    For example, on an x86, an allocation request of 5 kilobytes (KB) returns two 4-KB pages. The last 3 KB of the second page is unavailable to the caller or another caller. To avoid wasting nonpaged pool, the driver should allocate multiple pages efficiently. In this case, for example, the driver could make two allocations, one for PAGE\_SIZE and the other for 1 KB, to allocate a total of 5 KB.

    **Note**  Starting with Windows Vista, the system automatically adds the additional memory so two allocations are unnecessary.

     

-   *PoolType* = **PagedPool** for memory that is always accessed at IRQL &lt;= APC\_LEVEL and is not in the file system's write path.

**ExAllocatePoolWithTag** returns a **NULL** pointer if it cannot allocate the requested number of bytes. Drivers should always check the returned pointer. If its value is **NULL**, the **DriverEntry** routine (or any other driver routine that returns NTSTATUS values) should return STATUS\_INSUFFICIENT\_RESOURCES or handle the error condition if possible.

 

 




