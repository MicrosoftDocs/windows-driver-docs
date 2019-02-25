---
title: Specifying Memory Type for a Resource
description: Specifying Memory Type for a Resource
ms.assetid: b4691de0-d3c9-4a6f-a9f4-aafb22ea3e97
keywords:
- video memory types WDK display
- memory types WDK display
- resource memory types WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Memory Type for a Resource


The user-mode display driver receives information about the memory type that should be used when it receives a [request to create a resource](requesting-and-using-surface-memory.md). The memory type is specified as either system or video memory through the D3DDDIPOOL\_SYSTEMMEM or D3DDDIPOOL\_VIDEOMEMORY enumerators, respectively, of the **Pool** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure. In addition, the Microsoft Direct3D runtime provides hints to the driver about the type of video memory to use by specifying one of following enumerators in the **Pool** member:

-   D3DDDIPOOL\_LOCALVIDMEM

    The runtime recommends that the driver use local video memory.

-   D3DDDIPOOL\_NONLOCALVIDMEM

    The runtime recommends that the driver use nonlocal video memory (for example, AGP memory).

The runtime provides hints to the user-mode display driver to improve performance. For example, the runtime might specify D3DDDIPOOL\_NONLOCALVIDMEM if the CPU writes to the surface, which is performed faster using nonlocal video memory.

The user-mode display driver passes the hints to the display miniport driver through the **pPrivateDriverData** members of the [**D3DDDI\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff544364) and [**DXGK\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff560960) structures in a vendor-specific way. The display miniport driver indicates to the video memory manager the appropriate memory segment to use by returning the identifier of the segment in the **HintedSegmentId** member of the DXGK\_ALLOCATIONINFO structure from a call to the driver's [**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606) function.

Regardless of the type of video memory that is used to create the resource, the user-mode display driver must not expose any semantic differences to the runtime. That is, for each video memory type, the driver must render information identically and must return the same return values.

 

 





