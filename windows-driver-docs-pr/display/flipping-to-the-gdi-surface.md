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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Flipping to the GDI Surface


## <span id="ddk_flipping_to_the_gdi_surface_gg"></span><span id="DDK_FLIPPING_TO_THE_GDI_SURFACE_GG"></span>


A display driver should be implemented so that the GDI (desktop) surface can become the primary surface. Doing so lets applications display GDI-rendered content, such as dialog boxes. The driver can use one of the following methods to make the GDI surface into the primary surface:

-   The driver can include the GDI surface as one of the buffers in the driver's flipping chain. This method is the recommended way to let applications flip to the GDI surface. By default, when an application makes flipping requests, DirectDraw makes calls to the driver's [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) function to cycle through the buffers in the order that they are attached to each other in the chain. An application can flip to the GDI surface by determining the position of the GDI surface in the chain and then by making the appropriate number of flipping requests.

-   The driver can implement a [*DdFlipToGDISurface*](https://msdn.microsoft.com/library/windows/hardware/ff549335) function to receive notification when DirectDraw is flipping to or from a GDI surface. If the driver can access the GDI surface, the driver can flip to the GDI surface after receiving this notification. Using this method, the GDI surface is not required to be part of the driver's flipping chain.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Flipping%20to%20the%20GDI%20Surface%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




