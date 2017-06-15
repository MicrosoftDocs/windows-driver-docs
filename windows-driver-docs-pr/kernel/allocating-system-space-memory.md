---
title: Allocating System-Space Memory
author: windows-driver-content
description: Allocating System-Space Memory
MS-HAID:
- 'MemMgmt\_cf3a3d2a-357c-4b21-8df1-f01e8435201c.xml'
- 'kernel.allocating\_system\_space\_memory'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: eee425b3-6ddd-4e9d-b51d-1f2c9ea106a5
keywords: ["memory management WDK kernel , system-allocated space", "system-allocated space WDK kernel", "allocating system-space memory", "allocating I/O buffer memory", "I/O buffer memory allocations WDK kernel", "buffer memory allocations WDK kernel"]
---

# Allocating System-Space Memory


## <a href="" id="ddk-allocating-system-space-memory-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Allocating%20System-Space%20Memory%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


