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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Transparent Blt


## <span id="ddk_transparent_blt_gg"></span><span id="DDK_TRANSPARENT_BLT_GG"></span>


In a *transparent blt*, a color key normally specifies the colors that will not be moved. The source color key is analogous to the blue screen used in motion pictures. The color is compared to each pixel and if they match, the pixel is not copied. If they do not match, the pixel is copied. DirectDraw also supports color keys that are ranges.

In some cases, a transparent blt may be only partially supported by the hardware. This is probably still faster than doing it in software. The DDCAPS\_COLORKEYHWASSIST flag should be set in these cases.

An example of a partially supported transparent blt is a display card that requires a bitmask, instead of just using a color key. In this case, rather than comparing each pixel with the color key to determine whether to copy it, a monochrome mask is built. That is, all of the pixels are compared with the color key and the entire surface is converted to a bitmask (usually one bit per byte, depending on color depth). When using DirectDraw, this is done when the surface is unlocked.

Once the alpha mask is built, it is compared to the source surface. Everything that is not set on the alpha mask is copied to the destination surface. This accomplishes the same effect as a source color key, but requires a mask to be built first, rather than comparing and copying at the same time. The mask must be rebuilt any time the color key is set. It also must be checked whenever a blt occurs because a color key override can be specified at that time. When the application's **Blt** function is called, check that the color key override (the only color key passed to the blt) is the same as the color key that is set on the surface. If they are the same, it is not really an override and the mask does not need to be rebuilt. If they are different, then the mask must be rebuilt. (The driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function always sees the color key as an override.)

 

 





