---
title: Transparent Blt
description: Transparent Blt
ms.assetid: bc2f4159-cd5d-43db-8bc3-e6fbf1e594fb
keywords:
- surfaces WDK DirectDraw , blitting
- drawing blt WDK DirectDraw , transparent blt
- DirectDraw blitting WDK Windows 2000 display , transparent blt
- blitting WDK DirectDraw , transparent blt
- blt WDK DirectDraw , transparent
- color keys WDK DirectDraw
- transparent blts WDK DirectDraw
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Transparent Blt


## <span id="ddk_transparent_blt_gg"></span><span id="DDK_TRANSPARENT_BLT_GG"></span>


In a *transparent blt*, a color key normally specifies the colors that will not be moved. The source color key is analogous to the blue screen used in motion pictures. The color is compared to each pixel and if they match, the pixel is not copied. If they do not match, the pixel is copied. DirectDraw also supports color keys that are ranges.

In some cases, a transparent blt may be only partially supported by the hardware. This is probably still faster than doing it in software. The DDCAPS\_COLORKEYHWASSIST flag should be set in these cases.

An example of a partially supported transparent blt is a display card that requires a bitmask, instead of just using a color key. In this case, rather than comparing each pixel with the color key to determine whether to copy it, a monochrome mask is built. That is, all of the pixels are compared with the color key and the entire surface is converted to a bitmask (usually one bit per byte, depending on color depth). When using DirectDraw, this is done when the surface is unlocked.

Once the alpha mask is built, it is compared to the source surface. Everything that is not set on the alpha mask is copied to the destination surface. This accomplishes the same effect as a source color key, but requires a mask to be built first, rather than comparing and copying at the same time. The mask must be rebuilt any time the color key is set. It also must be checked whenever a blt occurs because a color key override can be specified at that time. When the application's **Blt** function is called, check that the color key override (the only color key passed to the blt) is the same as the color key that is set on the surface. If they are the same, it is not really an override and the mask does not need to be rebuilt. If they are different, then the mask must be rebuilt. (The driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function always sees the color key as an override.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Transparent%20Blt%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




