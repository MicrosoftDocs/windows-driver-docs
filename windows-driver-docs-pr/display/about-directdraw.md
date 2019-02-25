---
title: About DirectDraw
description: About DirectDraw
ms.assetid: f2ab4863-8ec8-4eaf-b59f-635570aef470
keywords:
- drawing WDK DirectDraw , about DirectDraw
- DirectDraw WDK Windows 2000 display , about DirectDraw
- tears WDK DirectDraw
- screen flicker WDK DirectDraw
- GDI WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# About DirectDraw


## <span id="ddk_about_directdraw_gg"></span><span id="DDK_ABOUT_DIRECTDRAW_GG"></span>


Microsoft DirectDraw is the display component of Microsoft DirectX that enables software designers to directly manipulate display memory, hardware blitters, hardware overlays, and flipping surfaces. DirectDraw provides a device-independent way for games and Windows subsystem software, such as 3D graphics packages and digital video codecs, to gain access to the features of specific display devices.

DirectDraw provides device-independent access to the device-specific display functionality in a direct 32-bit path. DirectDraw calls important functions in a driver that accesses the display card directly, without the intervention of the Windows graphics device interface (GDI) or the device-independent bitmap (DIB) engine.

By taking advantage of this direct path, games and other display-intensive applications run faster and avoid tearing. A *tear* is a screen flicker caused by an image displayed and written to at the same time. Direct access often allows game performance to be limited solely by display card performance. DirectDraw also uses page flipping to provide smooth animation.

The rapid motion and ever-changing screens of many games and multimedia applications put a heavy burden on the display process and tend to exacerbate tearing. Although GDI is very fast at drawing spreadsheets, graphs, TrueType font rendering, and so on, it is not meant to be a real-time graphics API. DirectDraw augments GDI by handling the device-dependent hardware accelerator functions in a 32-bit driver.

 

 





