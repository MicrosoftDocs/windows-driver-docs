---
title: Drawing Color Pointers
description: Drawing Color Pointers
ms.assetid: f2791ccc-3d9e-46f0-bc70-051ac298c1ee
keywords:
- drawing pointers WDK Windows 2000 display
- display drivers WDK Windows 2000 , pointers
- pointers WDK Windows 2000 display
- color pointers WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Drawing Color Pointers


## <span id="ddk_drawing_color_pointers_gg"></span><span id="DDK_DRAWING_COLOR_POINTERS_GG"></span>


Defining the color pointer in the same way as the monochrome pointer (that is, as a bitmap that includes an AND portion and an XOR portion -- see [Pointer Drawing](pointer-drawing.md) and [Drawing Monochrome Pointers](drawing-monochrome-pointers.md)) also supports transparency and inversion.

-   If the color bitmap is black (index 0) and the AND mask value is 1, then the result is transparency.

-   If the color bitmap is white and the AND mask value is 1, then the result is inversion.

-   If the device cannot display color, then a pointer can be drawn as black and white.

These conventions allow applications to use a single pointer definition for both color and monochrome displays.

 

 





