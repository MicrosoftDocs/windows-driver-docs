---
title: Handling DMA-style AGP
description: Handling DMA-style AGP
ms.assetid: f43f662f-0036-4725-ad6b-5b836b23a734
keywords:
- DMA-style AGP WDK DirectDraw
- display memory WDK DirectDraw , DMA-style AGP
- nonlocal display memory WDK DirectDraw , DMA-style AGP
- AGP WDK DirectDraw , DMA-style AGP
- drawing AGP support WDK DirectDraw , DMA-style AGP
- DirectDraw AGP support WDK Windows 2000 display , DMA-style AGP
- memory WDK DirectDraw AGP , DMA-style AGP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling DMA-style AGP


## <span id="ddk_handling_dma_style_agp_gg"></span><span id="DDK_HANDLING_DMA_STYLE_AGP_GG"></span>


An AGP-compatible display card can use AGP memory in one of two ways: using the execute model or the direct memory access (DMA) model.

-   In the execute model, if there is a texture in nonlocal video memory, the card accesses AGP memory directly. That is, if a card is textured from AGP memory it reads texel data directly from a backing surface (system memory copy of a surface).

-   In the DMA model, the contents of the surfaces must be explicitly moved to local display memory on the card before a texturing operation can be performed.

It is important to note that the model refers to how a client of the display card sees the transfer. For example, a display card may automatically move texel data from a backing surface to a small local display memory cache when texturing. This may seem like the DMA model. However, because the client application has no information about this transfer taking place, the display card is, in fact, exposing an execute model. Only when the client application has to take explicit action to move the contents of a backing surface to local display memory is the display card considered to be exposing the DMA model.

The previous sections that dealt with AGP memory described how a driver can enable and expose the execute model of AGP usage. This section describes the additional steps a driver must take to expose use of DMA model AGP to the application. Note that the driver writer must decide whether to expose the execute model or the DMA model when writing the driver. *The driver should expose one model or the other, but not both.*

Before exposing the DMA model from a driver, it is important to consider the implications of the DMA model to the application writer. If a driver exposes execute model AGP support, DirectDraw assumes that surfaces in AGP (nonlocal display memory) and local display memory are functionally identical. Thus the display card can texture either from nonlocal or local display memory without any additional actions by the application. When setting a render state, an application can specify the handle to a texture surface directly, regardless of whether the surface is in nonlocal or local display memory.

However, if a driver exposes the DMA model, surfaces in nonlocal display memory may have different capabilities from those in local display memory. Therefore, before attempting to texture from a nonlocal display memory surface, the application must check whether the hardware is capable of texture from nonlocal display memory. This is accomplished by examining the capabilities exposed by the driver. The same is true for blitting.

An application explicitly requests AGP memory by specifying DDSCAPS\_VIDEOMEMORY ORed with DDSCAPS\_NONLOCALVIDMEM. If an application does not specify a memory type or only specifies DDSCAPS\_VIDEOMEMORY, nonlocal display memory is not considered. Also, if the call does not specify local or nonlocal display memory, the surface is a texture, and the device sets the D3DDEVCAPS\_TEXTURENONLOCALVIDEOMEMORY flag, then the surface can be allocated in AGP memory.

This means that if a driver exposes the DMA model, surfaces are not allocated from AGP memory. This is in contrast to a driver that exposes execute model, in which AGP memory is allocated even if the application does not explicitly request it. Drivers that expose the execute model are therefore much simpler for applications to use. Furthermore, an execute model driver allows a legacy application to gain the benefits of AGP, whereas a DMA model driver only accelerates new applications written explicitly for AGP. This should be considered when deciding whether to expose the execute or DMA models.

 

 





