---
title: AGP Support
description: AGP Support
ms.assetid: 05a2f942-4374-421e-8292-d122f9fe3571
keywords: ["AGP WDK DirectDraw , about AGP support", "drawing AGP support WDK DirectDraw , about AGP support", "DirectDraw AGP support WDK Windows 2000 display , about AGP support", "memory WDK DirectDraw AGP , about AGP support", "Accelerated Graphics Port WDK DirectDraw", "display memory WDK DirectDraw", "nonlocal display memory WDK DirectDraw", "display memory WDK DirectDraw , about AGP support", "nonlocal display memory WDK DirectDraw , about nonlocal display memory", "AGP WDK DirectDraw", "drawing AGP support WDK DirectDraw", "DirectDraw AGP support WDK Windows 2000 display", "memory WDK DirectDraw AGP"]
---

# AGP Support


## <span id="ddk_agp_support_gg"></span><span id="DDK_AGP_SUPPORT_GG"></span>


Microsoft DirectDraw treats *Accelerated Graphics Port (AGP) memory* as a subclass of display memory. This memory type is referred to as *nonlocal display memory*. The terms AGP memory and nonlocal display memory are synonymous from the perspective of DirectDraw and DirectDraw drivers.

AGP memory is considered a pure subclass of display memory. That is, if a driver indicates it supports AGP memory, in most cases it must have the same functional capabilities for local and nonlocal display memory, although performance differences are permitted. The exception is if the DDCAPS2\_NONLOCALVIDMEMCAPS flag is set, in which case the blt capabilities for nonlocal display memory can differ from local display memory.

For example, if a driver states that it can texture from display memory, it must be able to texture from both local and nonlocal display memory. Blitting is treated similarly. A driver that exports the source color key blt capability must be able to do a source color keyed blt both to and from nonlocal display memory. The one exception to this rule is that it is possible to preclude certain surface types from ever being allocated in nonlocal display memory. For example, it is possible to use heaps to prevent overlay surfaces from ever being allocated in AGP memory.

Because AGP memory is treated as a subclass of display memory, DirectDraw has no separate set of display driver entry points for AGP memory. The existing display driver calls are used for both AGP surfaces and local display memory surfaces. An AGP-compatible driver must check incoming surfaces to see if they are in nonlocal or local display memory, and take the appropriate action. Blts from system to AGP (and vice versa) go through DirectDraw emulation layer as normal, unless a driver supports system-to-display memory blts (in which case it must support system-to-AGP transfers as well).

Drivers should set the DDCAPS2\_TEXMANINNONLOCALVIDMEM flag as much as possible because the Direct3D texture manager keeps its backing image of the video memory copy of a surface in AGP memory (rather than system memory) when this is the case.

The remainder of this section discusses the steps necessary to modify your existing driver to support AGP memory using DirectDraw nonlocal display memory features.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20AGP%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




