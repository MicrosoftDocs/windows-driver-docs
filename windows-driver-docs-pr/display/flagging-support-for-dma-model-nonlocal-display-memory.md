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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Flagging Support for DMA Model Nonlocal Display Memory


## <span id="ddk_flagging_support_for_dma_model_nonlocal_display_memory_gg"></span><span id="DDK_FLAGGING_SUPPORT_FOR_DMA_MODEL_NONLOCAL_DISPLAY_MEMORY_GG"></span>


In addition to specifying the DDCAPS2\_NONLOCALVIDMEM flag to report AGP support, a DMA model driver must export the capability flag DDCAPS2\_NONLOCALVIDMEMCAPS. This flag indicates that nonlocal (AGP) memory has different capabilities than local display memory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Flagging%20Support%20for%20DMA%20Model%20Nonlocal%20Display%20Memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




