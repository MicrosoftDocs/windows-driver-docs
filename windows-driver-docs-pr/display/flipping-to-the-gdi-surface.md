---
title: Flipping to the GDI Surface
description: Flipping to the GDI Surface
ms.assetid: e74e108d-f88c-4e42-9136-ef087378807a
keywords:
- drawing page flips WDK DirectDraw , GDI surface
- DirectDraw flipping WDK Windows 2000 display , GDI surface
- page flipping WDK DirectDraw , GDI surface
- flipping WDK DirectDraw , GDI surface
- GDI surface flipping WDK DirectDraw
- surfaces WDK DirectDraw , flipping
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flipping to the GDI Surface


## <span id="ddk_flipping_to_the_gdi_surface_gg"></span><span id="DDK_FLIPPING_TO_THE_GDI_SURFACE_GG"></span>


A display driver should be implemented so that the GDI (desktop) surface can become the primary surface. Doing so lets applications display GDI-rendered content, such as dialog boxes. The driver can use one of the following methods to make the GDI surface into the primary surface:

-   The driver can include the GDI surface as one of the buffers in the driver's flipping chain. This method is the recommended way to let applications flip to the GDI surface. By default, when an application makes flipping requests, DirectDraw makes calls to the driver's [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) function to cycle through the buffers in the order that they are attached to each other in the chain. An application can flip to the GDI surface by determining the position of the GDI surface in the chain and then by making the appropriate number of flipping requests.

-   The driver can implement a [*DdFlipToGDISurface*](https://msdn.microsoft.com/library/windows/hardware/ff549335) function to receive notification when DirectDraw is flipping to or from a GDI surface. If the driver can access the GDI surface, the driver can flip to the GDI surface after receiving this notification. Using this method, the GDI surface is not required to be part of the driver's flipping chain.

 

 





