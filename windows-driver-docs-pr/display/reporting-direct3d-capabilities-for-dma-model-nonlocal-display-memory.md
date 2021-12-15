---
title: Reporting Direct3D Capabilities for Nonlocal Display Memory
description: A DMA model driver must export the Direct3D capabilities for nonlocal display memory surfaces.
keywords:
- DMA-style AGP WDK DirectDraw
- display memory WDK DirectDraw , DMA-style AGP
- nonlocal display memory WDK DirectDraw , DMA-style AGP
- AGP WDK DirectDraw , DMA-style AGP
- drawing AGP support WDK DirectDraw , DMA-style AGP
- DirectDraw AGP support WDK Windows 2000 display , DMA-style AGP
- memory WDK DirectDraw AGP , DMA-style AGP
- reporting Direct3D capabilities
ms.date: 12/06/2018
ms.custom: seodec18
---

# Reporting Direct3D Capabilities for Nonlocal Display Memory

A DMA model driver must also export the Direct3D capabilities for nonlocal display memory surfaces. This is significantly simpler than reporting DirectDraw capabilities. The only capability affected is D3DDEVCAPS\_TEXTURENONLOCALVIDEOMEMORY. If a display card exporting the DMA model can texture directly from nonlocal display memory, it should set this capability in its Direct3D device description. If it cannot, and the application must explicitly load or blt the nonlocal display memory surface to a local display memory surface before performing texturing, it should not set this capability. For completeness, an execute model driver should always set this capability bit.

 

 





