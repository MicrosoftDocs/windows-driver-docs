---
title: Surface Negotiation
description: Surface Negotiation
keywords:
- surface negotiation WDK GDI
- GDI WDK Windows 2000 display , surfaces
- graphics drivers WDK Windows 2000 display , surface negotiation
- drawing WDK GDI , surface negotiation
- negotiation WDK GDI
- surface negotiation WDK GDI , about surface negotiation
- GDI WDK Windows 2000 display , bitmaps
- graphics drivers WDK Windows 2000 display , bitmaps
- drawing WDK GDI , bitmaps
- bitmaps WDK GDI
- secondary surfaces WDK GDI
- off-screen surfaces WDK GDI
- primary surfaces WDK GDI
- on-screen surfaces WDK GDI
ms.date: 04/20/2017
---

# Surface Negotiation


## <span id="ddk_surface_negotiation_gg"></span><span id="DDK_SURFACE_NEGOTIATION_GG"></span>


Drawing and text output require a surface on which to draw. This surface is created by the [**DrvEnableSurface**](/windows/win32/api/winddi/nf-winddi-drvenablesurface) function and is referred to as the *primary surface*. This surface is also known as the *on-screen surface*, because it appears in the video display. There is only one primary surface enabled per *PDEV* although a driver can support several PDEVs. Drivers that support the [**DrvCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-drvcreatedevicebitmap) function can create and use additional surfaces. These bitmap surfaces are referred to as *secondary surfaces* or *off-screen surfaces*. For either type of surface, the driver is responsible for determining the type of drawing operations it supports.

