---
title: Dynamic Textures
description: Dynamic Textures
ms.assetid: 5e96b33c-a07c-4f58-a016-14d8d925285e
keywords:
- textures WDK DirectX 9.0
- dynamic textures WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Dynamic Textures


## <span id="ddk_dynamic_textures_gg"></span><span id="DDK_DYNAMIC_TEXTURES_GG"></span>


Dynamic textures are almost exactly the same as [dynamic buffers](dynamic-vertex-and-index-buffers.md). Because applications also frequently lock and modify dynamic textures, drivers should:

-   Optimize the texture upload or tiling speed.

-   Create dynamic textures in a nontiled manner if the hardware architecture lets the driver use nontiled textures. This is because the performance improvement received from not requiring the driver to untile dynamic textures when the textures are locked is greater than from the fill-rate advantages of tiling.

-   Set up multiple buffering similar to the description in [Dynamic Vertex and Index Buffers](dynamic-vertex-and-index-buffers.md). That is, set the DDLOCK\_OKTOSWAP bit to lock dynamic textures. Similarly, storing dynamic textures in local video memory can also cause system performance to suffer if the application writes to such textures in a nonsequential manner. Therefore, the driver should store dynamic textures in [AGP](agp-support.md) memory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Dynamic%20Textures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




