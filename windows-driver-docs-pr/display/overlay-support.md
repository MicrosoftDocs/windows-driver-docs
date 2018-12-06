---
title: Overlay support
description: Overlay support
ms.assetid: 325a08b2-c357-49b7-a9c3-878c44bc2d26
keywords:
- drawing page flips WDK DirectDraw , overlay surfaces
- DirectDraw flipping WDK Windows 2000 display , overlay surfaces
- page flipping WDK DirectDraw , overlay surfaces
- flipping WDK DirectDraw , overlay surfaces
- overlay surfaces WDK DirectDraw
- surfaces WDK DirectDraw , overlay
- surfaces WDK DirectDraw , flipping
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overlay support


## <span id="ddk_overlay_support_gg"></span><span id="DDK_OVERLAY_SUPPORT_GG"></span>


DirectDraw also supports overlays. An *overlay surface* is one that can be displayed on top of the primary surface without altering the physical bits in the surface underneath it. With an overlay, registers are set that define a rectangle on the primary surface that contains the overlay surface. The digital-to-analog converter (DAC) changes the location of the rectangles. The scan line reads data in primary surface memory until it reaches the rectangle that is set aside for the overlay. It reads from the overlay surface until that line in the overlay is finished, then continues with the original primary surface image. This switching from primary surface to the overlay and back happens on every pass of the scan line and continues until the overlay is completely displayed.

The overlay surface can have a different pixel depth than the primary surface. For example, while 8 bits per pixel (bpp) may look fine for the primary surface, a video clip may need 16 bpp to display acceptably. The pixel depth switches seamlessly between the primary surface and the overlay. For more information about overlays with DirectDraw, see the [Video Port Extensions to DirectX](video-port-extensions-to-directx.md) section.

Overlays flip in exactly the same way as the primary surface. The DirectDraw surface objects swap pointers so that the new overlay surface is read when the scan line reaches the rectangle bounding the overlay. The same flipping algorithm described in [Timing a Flip](timing-a-flip.md) prevents tearing.

 

 





