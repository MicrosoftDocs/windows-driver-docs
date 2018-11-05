---
title: Flagging Support for DMA Model Nonlocal Display Memory
description: Flagging Support for DMA Model Nonlocal Display Memory
ms.assetid: 7310bf92-a1bb-4a72-8e1a-bae7e656a499
keywords:
- DMA-style AGP WDK DirectDraw
- display memory WDK DirectDraw , DMA-style AGP
- nonlocal display memory WDK DirectDraw , DMA-style AGP
- AGP WDK DirectDraw , DMA-style AGP
- drawing AGP support WDK DirectDraw , DMA-style AGP
- DirectDraw AGP support WDK Windows 2000 display , DMA-style AGP
- memory WDK DirectDraw AGP , DMA-style AGP
- flags WDK DirectDraw nonlocal memory
- DDCAPS2_NONLOCALVIDMEM
- DDCAPS2_NONLOCALVIDMEMCAPS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flagging Support for DMA Model Nonlocal Display Memory


## <span id="ddk_flagging_support_for_dma_model_nonlocal_display_memory_gg"></span><span id="DDK_FLAGGING_SUPPORT_FOR_DMA_MODEL_NONLOCAL_DISPLAY_MEMORY_GG"></span>


In addition to specifying the DDCAPS2\_NONLOCALVIDMEM flag to report AGP support, a DMA model driver must export the capability flag DDCAPS2\_NONLOCALVIDMEMCAPS. This flag indicates that nonlocal (AGP) memory has different capabilities than local display memory.

 

 





