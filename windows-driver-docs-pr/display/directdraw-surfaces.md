---
title: DirectDraw Surfaces
description: DirectDraw Surfaces
ms.assetid: be99b124-5193-4826-be28-ed6a132b84af
keywords: ["drawing surfaces WDK DirectDraw , about surfaces", "DirectDraw surfaces WDK Windows 2000 display , about surfaces", "surfaces WDK DirectDraw , about surfaces", "capability bits WDK DirectDraw", "caps bits WDK DirectDraw", "drawing surfaces WDK DirectDraw", "DirectDraw surfaces WDK Windows 2000 display", "surfaces WDK DirectDraw", "surfaces WDK DirectDraw , capability bits", "primary surfaces WDK DirectDraw"]
---

# DirectDraw Surfaces


## <span id="ddk_directdraw_surfaces_gg"></span><span id="DDK_DIRECTDRAW_SURFACES_GG"></span>


The Microsoft DirectDraw Surface is the basic image unit in Microsoft DirectX graphics. It is either a rectangular collection of pixels of a particular width, height, and pixel format; or a buffer containing commands or vertices for Microsoft Direct3D. Surfaces have bits associated with them that denote their behavior and usage. These bits are called *surface capability bits* (or *caps bits* for short). Caps bits denote intended usages of their associated surfaces such as holding texels for rendering (the DDSCAPS\_TEXTURE caps bit), being the target for 3D rendering (DDSCAPS\_3DDEVICE), and many others. For more information about surface caps bits, see the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure.

The *primary* surface is the surface that is currently being scanned out to the monitor by the display card. For more information about the primary surface, see the [Flipping](flipping.md) and [Memory Configurations](memory-configurations.md) sections.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DirectDraw%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




