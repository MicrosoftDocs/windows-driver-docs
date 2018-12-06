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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Blitting


## <span id="ddk_blitting_gg"></span><span id="DDK_BLITTING_GG"></span>


If a blt is happening within one surface and the source and destination areas overlap, the proper direction must be determined to avoid overwriting part of the source before it is copied. This can be accomplished with just two potential starting points at opposite corners of the surface. All the blt engine needs are the location and dimensions for each image.

Everything possible should be done to speed up the actual blt. Duplicating sections of code to avoid an IF statement may make the driver go faster, for example. Perhaps the best implementation of this technique is to put the code in a macro and use that in different places rather than making function calls. For more information, see [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205).

 

 





