---
title: Dynamic Textures
description: Dynamic Textures
ms.assetid: 5e96b33c-a07c-4f58-a016-14d8d925285e
keywords:
- textures WDK DirectX 9.0
- dynamic textures WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dynamic Textures


## <span id="ddk_dynamic_textures_gg"></span><span id="DDK_DYNAMIC_TEXTURES_GG"></span>


Dynamic textures are almost exactly the same as [dynamic buffers](dynamic-vertex-and-index-buffers.md). Because applications also frequently lock and modify dynamic textures, drivers should:

-   Optimize the texture upload or tiling speed.

-   Create dynamic textures in a nontiled manner if the hardware architecture lets the driver use nontiled textures. This is because the performance improvement received from not requiring the driver to untile dynamic textures when the textures are locked is greater than from the fill-rate advantages of tiling.

-   Set up multiple buffering similar to the description in [Dynamic Vertex and Index Buffers](dynamic-vertex-and-index-buffers.md). That is, set the DDLOCK\_OKTOSWAP bit to lock dynamic textures. Similarly, storing dynamic textures in local video memory can also cause system performance to suffer if the application writes to such textures in a nonsequential manner. Therefore, the driver should store dynamic textures in [AGP](agp-support.md) memory.

 

 





