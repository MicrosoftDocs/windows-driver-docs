---
title: DirectDraw Surfaces
description: DirectDraw Surfaces
ms.assetid: be99b124-5193-4826-be28-ed6a132b84af
keywords:
- drawing surfaces WDK DirectDraw , about surfaces
- DirectDraw surfaces WDK Windows 2000 display , about surfaces
- surfaces WDK DirectDraw , about surfaces
- capability bits WDK DirectDraw
- caps bits WDK DirectDraw
- drawing surfaces WDK DirectDraw
- DirectDraw surfaces WDK Windows 2000 display
- surfaces WDK DirectDraw
- surfaces WDK DirectDraw , capability bits
- primary surfaces WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectDraw Surfaces


## <span id="ddk_directdraw_surfaces_gg"></span><span id="DDK_DIRECTDRAW_SURFACES_GG"></span>


The Microsoft DirectDraw Surface is the basic image unit in Microsoft DirectX graphics. It is either a rectangular collection of pixels of a particular width, height, and pixel format; or a buffer containing commands or vertices for Microsoft Direct3D. Surfaces have bits associated with them that denote their behavior and usage. These bits are called *surface capability bits* (or *caps bits* for short). Caps bits denote intended usages of their associated surfaces such as holding texels for rendering (the DDSCAPS\_TEXTURE caps bit), being the target for 3D rendering (DDSCAPS\_3DDEVICE), and many others. For more information about surface caps bits, see the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure.

The *primary* surface is the surface that is currently being scanned out to the monitor by the display card. For more information about the primary surface, see the [Flipping](flipping.md) and [Memory Configurations](memory-configurations.md) sections.

 

 





