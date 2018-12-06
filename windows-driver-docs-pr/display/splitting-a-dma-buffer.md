---
title: Splitting a DMA Buffer
description: Splitting a DMA Buffer
ms.assetid: 6b35d5e2-f8aa-478a-a5a0-9f519ff0ba6f
keywords:
- DMA buffers WDK display , splitting
- splitting DMA buffers
- split points WDK display
- patch-location lists WDK display
- preempting DMA buffers WDK display
- DMA buffers WDK display , preemption
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Splitting a DMA Buffer


## <span id="ddk_splitting_a_dma_buffer_gg"></span><span id="DDK_SPLITTING_A_DMA_BUFFER_GG"></span>


Split points are used by the video memory manager to divide a large work item submitted by the display miniport driver into smaller work items that require less GPU resources to execute. For example, a large DMA buffer might reference a set of allocations that possibly cannot fit in local video memory or nonlocal memory. The only way to process such a work item is to divide it into multiple smaller work items that require less GPU resources.

**Note**   DMA buffer splitting and DMA buffer preemption are different independent concepts. A display miniport driver must always support DMA buffer splitting even on a system with a GPU where DMA buffer preemption is not possible. On a system with a GPU where context save and restore is not possible, the GPU scheduler schedules split portions of a DMA buffer back to back ensuring the split portions are not interleaved with another DMA buffer from a different GPU context. However, a paging buffer should be submitted between portions of a split DMA buffer because paging operations are required between split portions of a DMA buffer.
Each split point that the driver uses to build an application DMA stream is used by the video memory manager. A submitted DMA buffer should reprogram enough GPU state after each split point to account for a potential paging buffer that might be inserted at that location.

 

To specify split points, the display miniport driver specifies values in the **SplitOffset** and **SlotId** members of the [**D3DDDI\_PATCHLOCATIONLIST**](https://msdn.microsoft.com/library/windows/hardware/ff544630) structure for each allocation that is referenced in the **AllocationIndex** member of D3DDDI\_PATCHLOCATIONLIST. To track allocation usage within a particular DMA buffer, the video memory manager creates the required dimensions of an array using the **MaxAllocationListSlotId** member of the [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062) structure that the driver provided through a call to its [**DxgkDdiQueryAdapterInfo**](https://msdn.microsoft.com/library/windows/hardware/ff559746) function. This array is initialized at zero and is filled as split portion entries of the patch-location list are processed. The **SlotId** member of **D3DDDI\_PATCHLOCATIONLIST** for the patch location indicates which row of the resource table must be updated while the **SplitOffset** member indicates the offset within the DMA buffer where the allocation is required. The DMA buffer can be run up to the point specified by **SplitOffset** without the resource being accessible to the GPU. Similarly, if a new patch-location split portion entry refers to the same **SlotId**, the previous allocation is being replaced by the new allocation, and the previous allocation is no longer required (that is, the previous allocation can be paged-out).

When paging in the resources required by a DMA buffer, the video memory manager processes the patch-location list by starting with the first element and moving down toward the last element. The [**D3DDDI\_PATCHLOCATIONLIST**](https://msdn.microsoft.com/library/windows/hardware/ff544630) elements that are filled by the driver must contain values in their **SplitOffset** members; the elements are strictly increasing (that is, allocations must appear in the order in which they are used in the stream). The video memory manager pages in allocations that are referenced in the patch-location list in the order that they are provided. When a point is reached where the video memory manager can no longer page-in an allocation due to a low memory condition, the video memory manager submits the current portion of the DMA buffer being prepared to the GPU scheduler for execution. The DMA buffer is run from the beginning of the previous split point up to the **SplitOffset** value that is specified for an allocation that could not be brought in. Once submitted, the video memory manager determines the list of required allocations at the current split offset in the DMA stream by using the resource table. All allocations on the table are kept at their current physical location while other allocations that are no longer in use might be evicted. The video memory manager then continues to process the patch-location list, potentially splitting multiple times again.

The driver should specify split points each time an allocation is bound or unbound. To specify that an allocation is unbound, the driver can specify a **NULL** allocation handle in the **hDeviceSpecificAllocation** member of the [**DXGK\_ALLOCATIONLIST**](https://msdn.microsoft.com/library/windows/hardware/ff560975) structure with the appropriate value in the **SlotId** member of the associated [**D3DDDI\_PATCHLOCATIONLIST**](https://msdn.microsoft.com/library/windows/hardware/ff544630). The driver should unbind large resources to increase the chances that the video memory manager can solve complex memory placement issues.

Similarly, the driver should reprogram large resources at every split point. When taking a split point, the video memory manager is forced to leave a previously bound allocation to the previous allocation. This causes fragmentation of memory that can lead to a failure to solve complex memory placement issues that might have been solved if not for the previously bound allocation restriction. When calculating the state at a split point, the video memory manager determines which slot identifier (**SlotId**) is being reprogrammed at that split point (that is, each patch-location list element that shares the same **SplitOffset** value with other elements) and ignores placement restriction on this split point. For example, if the driver uses a 64-MB texture, reprogramming that texture at every split point gives the video memory manager the flexibility to move that texture around in memory between split points if necessary.

 

 





