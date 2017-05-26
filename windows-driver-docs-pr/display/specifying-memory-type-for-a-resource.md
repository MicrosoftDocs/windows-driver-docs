---
title: Specifying Memory Type for a Resource
description: Specifying Memory Type for a Resource
ms.assetid: b4691de0-d3c9-4a6f-a9f4-aafb22ea3e97
keywords:
- video memory types WDK display
- memory types WDK display
- resource memory types WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Specifying%20Memory%20Type%20for%20a%20Resource%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




