---
title: Reporting DirectDraw Capabilities for DMA Model Nonlocal Display Memory
description: Reporting DirectDraw Capabilities for DMA Model Nonlocal Display Memory
ms.assetid: e503fc8b-db27-486a-8616-a1b88ea77218
keywords:
- DMA-style AGP WDK DirectDraw
- display memory WDK DirectDraw , DMA-style AGP
- nonlocal display memory WDK DirectDraw , DMA-style AGP
- AGP WDK DirectDraw , DMA-style AGP
- drawing AGP support WDK DirectDraw , DMA-style AGP
- DirectDraw AGP support WDK Windows 2000 display , DMA-style AGP
- memory WDK DirectDraw AGP , DMA-style AGP
- reporting DirectDraw capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting DirectDraw Capabilities for DMA Model Nonlocal Display Memory


## <span id="ddk_reporting_directdraw_capabilities_for_dma_model_nonlocal_display_m"></span><span id="DDK_REPORTING_DIRECTDRAW_CAPABILITIES_FOR_DMA_MODEL_NONLOCAL_DISPLAY_M"></span>


A DMA model driver has different capabilities for nonlocal display memory than for local display memory. For example, a display card may be able to stretch blit local display memory surfaces but not nonlocal display memory surfaces. If the driver specifies the DDCAPS2\_NONLOCALVIDMEMCAPS flag, the driver is probed for the DirectDraw capabilities of nonlocal display memory surface by the [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) driver entry point. The GUID that identifies this probe is GUID\_NonLocalVidMemCaps.

It is important to note that for this release of DirectDraw, a driver can only specify the capabilities for blts from nonlocal display memory to local display memory. Transfers from local display memory to nonlocal display memory, and from nonlocal display memory to nonlocal display memory, are always emulated by the DirectDraw HEL. This restriction may be relaxed in a future release.

 

 





