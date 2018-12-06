---
title: Surface Negotiation
description: Surface Negotiation
ms.assetid: af368be6-ea32-49ea-b49e-7e3c9a30facb
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
ms.localizationpriority: medium
---

# Surface Negotiation


## <span id="ddk_surface_negotiation_gg"></span><span id="DDK_SURFACE_NEGOTIATION_GG"></span>


Drawing and text output require a surface on which to draw. This surface is created by the [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214) function and is referred to as the *primary surface*. This surface is also known as the *on-screen surface*, because it appears in the video display. There is only one primary surface enabled per [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) although a driver can support several PDEVs. Drivers that support the [**DrvCreateDeviceBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff556185) function can create and use additional surfaces. These bitmap surfaces are referred to as *secondary surfaces* or *off-screen surfaces*. For either type of surface, the driver is responsible for determining the type of drawing operations it supports.

 

 





