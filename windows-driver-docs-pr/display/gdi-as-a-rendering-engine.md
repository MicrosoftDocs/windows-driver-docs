---
title: GDI as a Rendering Engine
description: GDI as a Rendering Engine
keywords:
- GDI WDK Windows 2000 display , rendering engine
- graphics drivers WDK Windows 2000 display , rendering engine
- drawing WDK GDI , rendering engine
- rendering engine WDK GDI
- PDEV WDK GDI
ms.date: 04/20/2017
---

# GDI as a Rendering Engine


## <span id="ddk_gdi_as_a_rendering_engine_gg"></span><span id="DDK_GDI_AS_A_RENDERING_ENGINE_GG"></span>


For rendering operations, the driver must first enable a *surface* for each *PDEV* structure that is enabled. A PDEV is a logical representation of a physical device. If the hardware can be set up as a GDI standard-format bitmap, GDI can be used to do some or all of the drawing to the bitmap surface. GDI can also handle advanced [halftoning](gdi-halftoning-capabilities.md).

For information about enabling *PDEVs* and surfaces, refer to the [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) and [**DrvEnableSurface**](/windows/win32/api/winddi/nf-winddi-drvenablesurface) functions.

 

