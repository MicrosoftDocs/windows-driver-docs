---
title: Blitting
description: Blitting
ms.assetid: d9cbe939-957d-48e0-8427-d2c1ca0a9dd6
keywords:
- blt WDK DirectDraw
- drawing blt WDK DirectDraw , about blitting
- DirectDraw blitting WDK Windows 2000 display , about blitting
- blitting WDK DirectDraw , about blitting
- surfaces WDK DirectDraw , blitting
- drawing blt WDK DirectDraw
- DirectDraw blitting WDK Windows 2000 display
- blitting WDK DirectDraw
- blt WDK DirectDraw , about blitting
- DdBlt
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Blitting


## <span id="ddk_blitting_gg"></span><span id="DDK_BLITTING_GG"></span>


If a blt is happening within one surface and the source and destination areas overlap, the proper direction must be determined to avoid overwriting part of the source before it is copied. This can be accomplished with just two potential starting points at opposite corners of the surface. All the blt engine needs are the location and dimensions for each image.

Everything possible should be done to speed up the actual blt. Duplicating sections of code to avoid an IF statement may make the driver go faster, for example. Perhaps the best implementation of this technique is to put the code in a macro and use that in different places rather than making function calls. For more information, see [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Blitting%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




