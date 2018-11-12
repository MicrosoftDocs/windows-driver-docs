---
title: Requesting to Rename an Allocation
description: Requesting to Rename an Allocation
ms.assetid: f22e19ba-9ff3-4aa1-a3f0-103f67ea7c60
keywords:
- command buffers WDK display , allocation renaming
- DMA buffers WDK display , allocation renaming
- allocation renaming WDK display
- renaming allocations WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requesting to Rename an Allocation


The user-mode display driver should request that the video memory manager rename an allocation associated with a surface when an application indicates to discard the content of the surface as part of a request to lock the surface (for example, a vertex buffer). The Microsoft Direct3D runtime passes the **Discard** bit-field flag to indicate that it no longer requires the current content of the surface. The driver can request that the video memory manager allocate a new allocation to handle the lock request if the current allocation holding the content of the surface is busy, rather than stalling the application thread until the current allocation becomes idle.

The user-mode display driver requests that the video memory manager rename an allocation when the driver sets the **Discard** member of the [**D3DDDICB\_LOCKFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544214) structure in a call to the [**pfnLockCb**](https://msdn.microsoft.com/library/windows/hardware/ff568914) function. The video memory manager determines if it should rename the allocation or should cause the application to stall until the allocation is idle based on whether the allocation is currently busy and on the current memory condition. For each allocation being renamed, the video memory manager maintains a list of allocations that are successively used for locking allocations. The video memory manager cycles through the list each time the application discards the content of an allocation. The length of the list is determined by application requirements and memory pressure. The video memory manager attempts to keep the list long enough to avoid stalling the application thread on a lock request. However, under memory pressure, the video memory manager can trim the list to avoid causing extra memory pressure.

To impose a limit on the length of the renaming list for an allocation, the driver sets the **MaximumRenamingListLength** member of the [**DXGK\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff560960) structure when it creates the allocation. If the driver sets **MaximumRenamingListLength** to a nonzero value, then the video memory manager determines the appropriate length of the renaming list without exceeding the limit imposed by the driver. If the driver sets **MaximumRenamingListLength** to 0, then the memory manager can increase the size of the renaming list to whatever size is necessary to improve performance.

Note that when the user-mode display driver sets the **Discard** member of [**D3DDDICB\_LOCKFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544214), the video memory manager does not call the display miniport driver to allocate extra allocations for the original allocation. The video memory manager creates all extra allocations using the creation parameters of the original allocation. From the perspective of the display miniport driver, the same allocation is paged in at potentially multiple simultaneous segment locations.

 

 





