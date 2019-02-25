---
title: Using Extended Surface Alignment
description: Using Extended Surface Alignment
ms.assetid: ae4a6820-b9be-4dd2-95d8-6030b3b63826
keywords:
- drawing extended surface alignment WDK DirectDraw
- DirectDraw extended surface alignment WDK Windows 2000 display
- surfaces WDK DirectDraw , extended alignment
- extended surface alignment WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Extended Surface Alignment


## <span id="ddk_using_extended_surface_alignment_gg"></span><span id="DDK_USING_EXTENDED_SURFACE_ALIGNMENT_GG"></span>


To enable the extended surface alignment functionality, the DirectDraw driver must perform the following tasks at initialization time:

-   The driver must specify a [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) function in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure that DirectDraw can call to get additional information.

-   The *DdGetDriverInfo* callback is called with the GUID\_GetHeapAlignment GUID specified. The driver must fill in a [**DD\_GETHEAPALIGNMENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551572) structure, then copy this structure to the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) structure.

The driver should fill in the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure pointed to in the [**HEAPALIGNMENT**](https://msdn.microsoft.com/library/windows/hardware/ff567265) structure with the logical OR of the DDSCAPS\_xxxx flags for any type of surface that requires alignment in this heap. If a bit in DDSCAPS is set, then DirectDraw abides by the alignment restrictions expressed in the appropriate [**SURFACEALIGNMENT**](https://msdn.microsoft.com/library/windows/hardware/ff569895) structure member. The DDSCAPS\_FLIP bit and the **FlipTarget** member apply to surfaces that are back buffers in the primary flipping chain, that is, a potentially primary (visible) surface. The following list shows the currently allowed set of surface capabilities for which alignment can be specified:

-   DDSCAPS\_OFFSCREENPLAIN

-   DDSCAPS\_EXECUTEBUFFER

-   DDSCAPS\_OVERLAY

-   DDSCAPS\_TEXTURE

-   DDSCAPS\_ZBUFFER

-   DDSCAPS\_ALPHA

-   DDSCAPS\_FLIP

**Note**   DirectDraw compares a new surface's capabilities against the entries in the [**HEAPALIGNMENT**](https://msdn.microsoft.com/library/windows/hardware/ff567265) structure in the order in which they are specified. For example, a surface with DDSCAPS\_MIPMAP | DDSCAPS\_TEXTURE | DDSCAPS\_FLIP set is aligned according to the **Texture** member of the HEAPALIGNMENT structure, because this is the first applicable capabilities bit for which an alignment is specified (that is, **Texture** appears before **FlipTarget** in the HEAPALIGNMENT structure). The **FlipTarget** member is not considered in this example. Because back buffers in a primary flipping chain are marked with DDSCAPS\_FLIP and no other bit for which an alignment can be specified, such surfaces are aligned according to the **FlipTarget** member. Surfaces that could potentially become members of a primary flipping chain (those with the same pixel format and size as the primary surface) are also aligned according to the **FlipTarget** member.

 

 

 





