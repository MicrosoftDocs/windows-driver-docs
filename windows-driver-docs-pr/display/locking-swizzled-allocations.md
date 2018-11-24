---
title: Locking Swizzled Allocations
description: Locking Swizzled Allocations
ms.assetid: c9be52d9-36b2-4a0f-9629-01b31293af38
keywords:
- swizzled allocation locking WDK display
- locking swizzled allocations WDK display
- unswizzled allocations WDK display
- memory segments WDK display , locking swizzled allocations
- allocation swizzle locks WDK display
- evicted allocations WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Locking Swizzled Allocations


The video memory manager provides special support for direct CPU access to swizzled allocations (that is, allocations in which the display miniport driver's [**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606) function sets the **Swizzled** flag in the **Flags** member of the [**DXGK\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff560960) structure).

When the video memory manager evicts CPU-accessible allocations that are not marked by the driver as swizzled from a memory segment, the display miniport driver must always store them in a linear format. Therefore, such allocations cannot be swizzled while they are located in an aperture segment, and they must always be swizzled or unswizzled by the driver's [**DxgkDdiBuildPagingBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559587) function.

On the other hand, allocations that are marked as swizzled are not required to always be stored in a linear format when evicted from a memory segment. For such allocations, the video memory manager tracks the swizzling state of those allocations and only requires the driver's *DxgkDdiBuildPagingBuffer* function to unswizzle an allocation during certain transfer operations.

After the user-mode display driver calls the Microsoft Direct3D runtime's [**pfnLockCb**](https://msdn.microsoft.com/library/windows/hardware/ff568914) function, the video memory manager and the display miniport driver behave in the following ways depending on the state of the allocation:

1.  Allocation located in a memory segment

    The video memory manager attempts to acquire a CPU aperture to provide linear access to the allocation. If the video memory manager cannot acquire the aperture, the video memory manager evicts the allocation back to system memory (unless the driver sets the **DonotEvict** member of the [**D3DDDICB\_LOCKFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544214) structure). When the video memory manager calls the display miniport driver's [**DxgkDdiBuildPagingBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559587) function to transfer the allocation, the display miniport driver should unswizzle the allocation.

2.  Allocation evicted (swizzled) or located in an aperture segment

    The allocation must be unswizzled before the CPU can access it. Therefore, the video memory manager first attempts to page in the allocation into a memory segment. After the allocation is located in a memory segment, the video memory manager and display miniport driver behave as in number 1.

3.  Allocation evicted (unswizzled)

    If the allocation is already unswizzled to system memory, the video memory manager returns the existing allocation pointer without further processing.

    In order for the GPU to use an allocation that was previously unswizzled, the allocation must be reswizzled before the GPU uses it. Therefore, on a surface fault, the video memory manager and the display miniport driver behave in the following ways:

    -   Allocation in a memory segment (unswizzled on the fly by the CPU aperture)

        The allocation is already in a swizzled format that the GPU can process. Therefore, no further processing is required by the video memory manager.

    -   Allocation evicted to system memory (unswizzled)

        The pages of the allocation contain unswizzled data and cannot be mapped into an aperture segment. Therefore, the allocation must be paged in a memory segment. When the video memory manager calls the display miniport driver's [**DxgkDdiBuildPagingBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559587) function to page in the allocation, the video memory manager requests that the display miniport driver swizzle the allocation.

**Note**   After a swizzled allocation is under CPU access through a CPU aperture, it can still be evicted before the user-mode display driver terminates the CPU access. This case is handled as in number 2. The eviction is performed in such a way as to be invisible to the application and user-mode display driver.
Also, a no-overwrite lock (that is, a lock obtained by setting the **IgnoreSync** member of [**D3DDDICB\_LOCKFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544214)) is not allowed on a swizzled allocation. Only the CPU or the GPU can access such an allocation at any given time.

 

 

 





