---
title: Flipping
description: Flipping
ms.assetid: e577b73f-7664-4c87-8d43-c3cf04705081
keywords:
- tears WDK DirectDraw
- drawing page flips WDK DirectDraw , about flipping
- DirectDraw flipping WDK Windows 2000 display , about flipping
- page flipping WDK DirectDraw , about flipping
- flipping WDK DirectDraw , about flipping
- drawing page flips WDK DirectDraw
- DirectDraw flipping WDK Windows 2000 display
- page flipping WDK DirectDraw
- flipping WDK DirectDraw
- primary surfaces WDK DirectDraw
- surfaces WDK DirectDraw , flipping
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Flipping


## <span id="ddk_flipping_gg"></span><span id="DDK_FLIPPING_GG"></span>


Using a back buffer that can be flipped with a front buffer is the best way to take advantage of DirectDraw. Page flipping is essential for smooth, tear-free animation in games and video playback.

The *primary surface* is the area of memory that is being read from to draw the screen that is currently being displayed. If a primary surface has one or more attached back buffers, it is a *flippable* surface.

Flipping structures are used to page flip in DirectDraw. Conceptually, they can be thought of as linked lists made of surfaces. The front buffer is the "visible" buffer. The back buffer and all attached flippable surfaces must be the same size and pixel depth as the front buffer. Most modern graphics cards have enough memory for flippable front and back buffers in high resolution modes.

All types of surfaces can be flipped in DirectDraw; page flipping is the common special case. For instance, flipping is not limited to the primary surface on cards that support overlays, or on 3D capable display cards that have texture memory. In these cases, overlays and textures can be flipped in the same way as the primary surface, with the same driver entry point.

Surfaces that are not used for flipping can have any dimension and can store nonflippable objects such as image data. Image data may also be stored in system memory, but in that case DirectDraw may use the hardware emulation layer (HEL) because hardware blitters cannot normally reach system memory to blit the image data. Some cards allow hardware blitters to have direct memory access (DMA) to system memory, so DirectDraw performs a check for DMA.

The following figure illustrates the relationship between two flippable surfaces.

![diagram illustrating flipping](images/ddfig7.png)

If a front buffer has one or more back buffers attached, it is a flippable surface, as shown in the preceding figure. The back buffer and all attached flippable surfaces must be the same size and pixel depth as the front buffer. A back buffer surface becomes the primary surface using a flip. A flip simply changes a pointer so it points to a different flippable surface, thereby displaying the new surface. The front buffer (which is no longer the primary surface) then becomes accessible, and can have new data written to it.

Flipping solves most screen flicker problems. The ability to render to a surface that is not being displayed allows smooth, tear-free animation for game play and video playback.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Flipping%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




