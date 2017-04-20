---
title: Using Extended Surface Alignment
description: Using Extended Surface Alignment
ms.assetid: ae4a6820-b9be-4dd2-95d8-6030b3b63826
keywords:
- drawing extended surface alignment WDK DirectDraw
- DirectDraw extended surface alignment WDK Windows 2000 display
- surfaces WDK DirectDraw , extended alignment
- extended surface alignment WDK DirectDraw
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20Extended%20Surface%20Alignment%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




