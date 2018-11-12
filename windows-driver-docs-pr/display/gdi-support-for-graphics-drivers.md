---
title: GDI Support for Graphics Drivers
description: GDI Support for Graphics Drivers
ms.assetid: ef42cda0-106f-4c1b-babc-29a1070e2a2f
keywords:
- GDI WDK Windows 2000 display , reference
- graphics drivers WDK Windows 2000 display , reference
- drawing WDK GDI , reference
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Support for Graphics Drivers


## <span id="ddk_gdi_support_for_graphics_drivers_gg"></span><span id="DDK_GDI_SUPPORT_FOR_GRAPHICS_DRIVERS_GG"></span>


This section describes the Microsoft Windows NT-based operating system graphics device interface (GDI). It then details the support that GDI provides to graphics drivers.

References to GDI in this section are implicit references to kernel-mode GDI; Microsoft Win32 GDI will be explicitly identified. Kernel-mode GDI is also known as the Graphics Engine.

GDI function and structure references are documented in the [Display Devices Reference](https://msdn.microsoft.com/library/windows/hardware/ff554046) section. Most of the GDI function declarations and structure definitions can be found in *Winddi.h*. For display drivers, the Microsoft DirectDraw heap manager functions are declared in *Dmemmgr.h*. Both files are shipped with the Windows Driver Kit (WDK).

 

 





