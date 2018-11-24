---
title: Handling Renaming on Windows 2000
description: Handling Renaming on Windows 2000
ms.assetid: d8f533f8-3037-47c0-986b-bd283bb3804d
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , vertex buffers, renaming on Windows 2000
- vertex buffers WDK DirectX 8.0 , renaming on Windows 2000
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Renaming on Windows 2000


## <span id="ddk_handling_renaming_on_windows_2000_gg"></span><span id="DDK_HANDLING_RENAMING_ON_WINDOWS_2000_GG"></span>


In order to correctly perform vertex buffer renaming it is important to understand the nature of the **fpVidMem** pointer stored in the surface global object on Windows 2000 and later. The interpretation of **fpVidMem** depends on the type of memory in which the surface is stored. For both system and nonlocal video memory (AGP) surfaces the **fpVidMem** is a pointer directly into the user-mode address space of the process owning that surface.

For local video memory surfaces, **fpVidMem** is an offset from the start of video memory. In order to convert this to a user-mode pointer it is necessary to add the base address of video memory as mapped into a user-mode process. This base address can be found in the **fpProcess** field of the DirectDraw local object for a given process.

Although **fpVidMem** for a nonlocal video memory surface is simply a user-mode pointer the means by which this user-mode pointer are generated are somewhat complex. It is necessary to understand how the Windows 2000 kernel maintains AGP heaps and manages surface allocations from them. The first important point is that, for nonlocal heaps, the start address of the heap maintained by the kernel may not be a heap into any real address space. It is in fact, normally, a numerical offset designed to ensure that valid allocations from that heap cannot have a **NULL** (zero) address.

It may be helpful to think of AGP heaps as residing in a conceptual address space that does not correspond to any real address space. The **fpStart** field of an AGP heap is the base address of the heap in this conceptual address space. Furthermore, any surfaces allocated from an AGP heap have an **fpHeapOffset** that also lies in this conceptual address space. Thus, **fpHeapOffset** is an offset from the base of this conceptual heap and it is not an offset from the start of the heap itself. Furthermore, it is not a pointer into any real address space. In order for a user-mode process to access the memory of a surface **fpHeapOffset** must be mapped (through pointer arithmetic) into the address space of that user-mode process. When a surface is created, the kernel performs this mapping according to the formula outlined below.

Given a surface (**pSurface**), a kernel-mode AGP heap (**pvmHeap**) and a mapping of the heap into a particular user-mode process (**pMap**), the following formula is used to compute the actual, user-mode **fpVidMem** for a surface:

```cpp
fpVidMem = pMap->pvVirtAddr +
    (pSurface->fpHeapOffset âˆ’ pvmHeap->fpStart)
```

**pvVirtAddr** is the base address of the user-mode mapping of the AGP heap into a given process. **fpStart** is the offset of the base of the AGP heap into the conceptual address space described above and **fpHeapOffset** is the offset of the start of the surface from the base of the same conceptual address space.

Your driver is notified of the conceptual base address of AGP heaps through the [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) callback. When *DdGetDriverInfo* is called with GUID\_UpdateNonLocalHeap the **fpGARTLin** field of the data structure passed is the same value as **fpStart**, that is, the base address of the start of the AGP heap in the conceptual address space. Unfortunately, your driver is not notified of the value of **pvVirtAddr** and it is not visible to the driver through any of the data structures passed to the driver. Therefore, its value has to be computed from the **fpVidMem** computed by the kernel for the vertex buffer on initial creating. Given the **fpVidMem** computed by the kernel, simply subtract the current **fpHeapOffset** less the heap's **fpStart**. Given the **fpHeapOffset** of the new memory to be swapped into the vertex buffer on renaming, the new value of **fpVidMem** can be easily computed.

The following code fragment demonstrates computing a new **fpVidMem** for an AGP surface in a lock call.

```cpp
// Get the vertex buffer&#39;s surface local and global from the
// lock data
LPDDRAWI_DDRAWSURFACE_LCL*pLcl = pLockData->lpDDSurface;
LPDDRAWI_DDRAWSURFACE_GBL*pGbl = pLcl->lpGbl;

// Get heap this vertex buffer was allocated from
LPVVIDEOMEMORY pHeap = pGbl->lpVidMemHeap;

// Get the current fpVidMem for the vertex buffer
FLATPTR fpCurrentVidMem = pGbl->fpVidMem;

// Compute the virtual base address of the mapping of this AGP
// into the process owning this vertex buffer.
FLATPTR pvVirtAddr = fpCurrentVidMem âˆ’
                     (pGbl->fpHeapOffset âˆ’ pHeap->fpStart);

// Given the fpHeapOffset of the nonlocal video memory to be
// swapped into the new vertex buffer compute the new fpVidMem
// as follow
FLATPTR fpNewVidMem = pvVirtAddr + (fpNewHeapOffset âˆ’ pHeap->fpStart);

// Now store the new fpVidMem in the surface global object and
// also in the lock data.
pGbl->fpHeapOffset = fpNewHeapOffset;
pGbl->fpVidMem = fpNewVidMem;
pLockData->lpSurfData = fpNewVidMem;

// Return success and driver handled
pLockData->ddRVal = DD_OK;
return DDHAL_DRIVER_HANDLED;
```

In order to make nonlocal video memory accessible to a user-mode process it is necessary for the memory to be both committed and mapped to the user-mode process. To ensure that this is done when vertex buffer renaming is being performed it is essential, that the new memory for the vertex buffer be allocated using the **Eng***Xxx* function [**HeapVidMemAllocAligned**](https://msdn.microsoft.com/library/windows/hardware/ff567267). This guarantees that the memory is committed and mapped before use. **HeapVidMemAllocAligned** returns an offset into the conceptual address space of the AGP heap and, therefore, this pointer can be used as an **fpHeapOffset** directly.

If the driver returns DDHAL\_DRIVER\_HANDLED for a lock of an AGP surface the kernel code returns the value of **lpSurfData** in the [**DD\_LOCKDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551637) data structure to the runtime and application. If the driver returns DDHAL\_DRIVER\_NOTHANDLED the kernel simply returns the value of **fpVidMem** to user mode. Therefore, it is not necessary to return DDHAL\_DRIVER\_HANDLED as long as **fpVidMem** is updated to point to the new user-mode pointer. However, we recommend that the driver both set **fpVidMem** and **lpSurfData** and return DDHAL\_DRIVER\_HANDLED.

 

 





