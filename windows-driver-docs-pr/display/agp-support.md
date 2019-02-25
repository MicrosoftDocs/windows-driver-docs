---
title: AGP Support
description: AGP Support
ms.assetid: 05a2f942-4374-421e-8292-d122f9fe3571
keywords:
- AGP WDK DirectDraw , about AGP support
- drawing AGP support WDK DirectDraw , about AGP support
- DirectDraw AGP support WDK Windows 2000 display , about AGP support
- memory WDK DirectDraw AGP , about AGP support
- Accelerated Graphics Port WDK DirectDraw
- display memory WDK DirectDraw
- nonlocal display memory WDK DirectDraw
- display memory WDK DirectDraw , about AGP support
- nonlocal display memory WDK DirectDraw , about nonlocal display memory
- AGP WDK DirectDraw
- drawing AGP support WDK DirectDraw
- DirectDraw AGP support WDK Windows 2000 display
- memory WDK DirectDraw AGP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AGP Support


## <span id="ddk_agp_support_gg"></span><span id="DDK_AGP_SUPPORT_GG"></span>


Microsoft DirectDraw treats *Accelerated Graphics Port (AGP) memory* as a subclass of display memory. This memory type is referred to as *nonlocal display memory*. The terms AGP memory and nonlocal display memory are synonymous from the perspective of DirectDraw and DirectDraw drivers.

AGP memory is considered a pure subclass of display memory. That is, if a driver indicates it supports AGP memory, in most cases it must have the same functional capabilities for local and nonlocal display memory, although performance differences are permitted. The exception is if the DDCAPS2\_NONLOCALVIDMEMCAPS flag is set, in which case the blt capabilities for nonlocal display memory can differ from local display memory.

For example, if a driver states that it can texture from display memory, it must be able to texture from both local and nonlocal display memory. Blitting is treated similarly. A driver that exports the source color key blt capability must be able to do a source color keyed blt both to and from nonlocal display memory. The one exception to this rule is that it is possible to preclude certain surface types from ever being allocated in nonlocal display memory. For example, it is possible to use heaps to prevent overlay surfaces from ever being allocated in AGP memory.

Because AGP memory is treated as a subclass of display memory, DirectDraw has no separate set of display driver entry points for AGP memory. The existing display driver calls are used for both AGP surfaces and local display memory surfaces. An AGP-compatible driver must check incoming surfaces to see if they are in nonlocal or local display memory, and take the appropriate action. Blts from system to AGP (and vice versa) go through DirectDraw emulation layer as normal, unless a driver supports system-to-display memory blts (in which case it must support system-to-AGP transfers as well).

Drivers should set the DDCAPS2\_TEXMANINNONLOCALVIDMEM flag as much as possible because the Direct3D texture manager keeps its backing image of the video memory copy of a surface in AGP memory (rather than system memory) when this is the case.

The remainder of this section discusses the steps necessary to modify your existing driver to support AGP memory using DirectDraw nonlocal display memory features.

 

 





