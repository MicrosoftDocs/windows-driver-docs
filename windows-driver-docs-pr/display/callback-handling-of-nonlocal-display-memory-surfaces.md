---
title: Callback Handling Of Nonlocal Display Memory Surfaces
description: Callback Handling Of Nonlocal Display Memory Surfaces
ms.assetid: 803c52df-93c4-4124-9e17-6ef6c734a15f
keywords:
- display memory WDK DirectDraw , callbacks
- nonlocal display memory WDK DirectDraw , callbacks
- AGP WDK DirectDraw , callbacks
- drawing AGP support WDK DirectDraw , callbacks
- DirectDraw AGP support WDK Windows 2000 display , callbacks
- memory WDK DirectDraw AGP , callbacks
- callbacks WDK DirectDraw nonlocal memory
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Callback Handling Of Nonlocal Display Memory Surfaces


## <span id="ddk_callback_handling_of_nonlocal_display_memory_surfaces_gg"></span><span id="DDK_CALLBACK_HANDLING_OF_NONLOCAL_DISPLAY_MEMORY_SURFACES_GG"></span>


Nonlocal display memory surfaces are treated in exactly the same way as local display memory surfaces in terms of driver callbacks. For example, a driver's [*DdCanCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549213) callback is called when attempting to create nonlocal (as well as local) display memory surfaces, [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) is called when blitting between local and nonlocal display memory surfaces, and [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) is called when the surface memory is being discarded.

Because the same driver functions are used for both local and nonlocal display memory surfaces, drivers must explicitly check the memory type of incoming surfaces. The memory type can be identified by checking the **ddsCaps.dwCaps** member of the local surface object [**DD\_SURFACE\_LOCAL**](https://msdn.microsoft.com/library/windows/hardware/ff551733) passed to the driver against the capability bits DDSCAPS\_LOCALVIDMEM and DDSCAPS\_NONLOCALVIDMEM.

Applications and AGP hardware access the bits of a DirectDraw surface using two different addresses. Applications use a virtual address that is translated through the operating system's page table to a portion of physical address space. This physical address space is mapped by the GART hardware to appear contiguous. Hardware accesses this physical linear address (again remapped to real, discontinuous pages of memory by the GART). The **fpVidMem** member of the [**DD\_SURFACE\_GLOBAL**](https://msdn.microsoft.com/library/windows/hardware/ff551726) structure holds the virtual linear address useful to applications (and potentially some driver operations). The device-side physical address can be found from:

```cpp
fpStartOffset = pSurface->fpHeapOffset - pSurface->lpVidMemHeap->fpStart;
```

This offset is then added to the device's GART physical base address (contained in the **liPhysAGPBase** member of the [**VMEMHEAP**](https://msdn.microsoft.com/library/windows/hardware/ff570561) structure).

In all other respects, nonlocal display memory surfaces behave exactly like local display memory surfaces. The driver receives lock requests when an application is trying to access the surface data of nonlocal display memory surfaces. Operations such as blts between nonlocal display memory and local display memory can be asynchronous, just as they can be between local display memory surfaces. Attempts to lock nonlocal display memory surfaces when operations involving those surfaces are still pending should be failed by the driver with DDERR\_WASSTILLDRAWING error code in the usual way.

Furthermore, although DirectDraw manages the allocation and freeing of nonlocal display memory surfaces on behalf of the driver, the driver is still notified of the creation and destruction of surfaces in nonlocal display memory. When a nonlocal display memory surface is destroyed, the driver should not return until the surface is no longer in use.

Nonlocal display memory is [lost](losing-and-restoring-directdraw-surfaces.md) in exactly the same way as local display memory, that is, when a mode switch occurs or when exclusive mode changes, all local and nonlocal display memory surfaces are lost and the [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) driver callback is invoked for each surface. However, DirectDraw does not guarantee that the actual reserved address ranges and committed memory are preserved. DirectDraw may choose to discard all committed memory and the reserved address ranges, or it may choose to decommit memory but preserve the address range. It may also preserve both and simply mark the surfaces as lost. A driver should not make assumptions based on any one of these scenarios.

 

 





