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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Overlay support


## <span id="ddk_overlay_support_gg"></span><span id="DDK_OVERLAY_SUPPORT_GG"></span>


DirectDraw also supports overlays. An *overlay surface* is one that can be displayed on top of the primary surface without altering the physical bits in the surface underneath it. With an overlay, registers are set that define a rectangle on the primary surface that contains the overlay surface. The digital-to-analog converter (DAC) changes the location of the rectangles. The scan line reads data in primary surface memory until it reaches the rectangle that is set aside for the overlay. It reads from the overlay surface until that line in the overlay is finished, then continues with the original primary surface image. This switching from primary surface to the overlay and back happens on every pass of the scan line and continues until the overlay is completely displayed.

The overlay surface can have a different pixel depth than the primary surface. For example, while 8 bits per pixel (bpp) may look fine for the primary surface, a video clip may need 16 bpp to display acceptably. The pixel depth switches seamlessly between the primary surface and the overlay. For more information about overlays with DirectDraw, see the [Video Port Extensions to DirectX](video-port-extensions-to-directx.md) section.

Overlays flip in exactly the same way as the primary surface. The DirectDraw surface objects swap pointers so that the new overlay surface is read when the scan line reaches the rectangle bounding the overlay. The same flipping algorithm described in [Timing a Flip](timing-a-flip.md) prevents tearing.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Overlay%20support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




