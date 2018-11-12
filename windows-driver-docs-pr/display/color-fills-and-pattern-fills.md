---
title: Color Fills and Pattern Fills
description: Color Fills and Pattern Fills
ms.assetid: 6e597405-e40f-4cb8-b177-896681745e00
keywords:
- drawing blt WDK DirectDraw , color fills
- DirectDraw blitting WDK Windows 2000 display , color fills
- blitting WDK DirectDraw , color fills
- blt WDK DirectDraw , color fills
- surfaces WDK DirectDraw , blitting
- drawing blt WDK DirectDraw , pattern fills
- DirectDraw blitting WDK Windows 2000 display , pattern fills
- blitting WDK DirectDraw , pattern fills
- blt WDK DirectDraw , pattern fills
- color fills WDK DirectDraw
- pattern fills WDK DirectDraw
- fill colors WDK DirectDraw
- fill patterns WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Color Fills and Pattern Fills


## <span id="ddk_color_fills_and_pattern_fills_gg"></span><span id="DDK_COLOR_FILLS_AND_PATTERN_FILLS_GG"></span>


A color fill, as described by a rectangle, fills an area of the screen with a particular color. On most cards, only the address of display memory, the dimensions of the rectangle, and the color are needed. Some cards require beginning and ending X and Y coordinates. Note that Windows automatically drops the last line of these coordinates. For example, when they are numbered from 0 to 640, Windows drops line 640.

Some cards use a pattern fill, which can accomplish the same thing as a color fill. An 8 x 8 region of pixels (the pattern) makes up the desired color, and that pattern is used to fill the specified area. The pattern is set to equal the color desired and filled in the same as a color fill. A pattern fill takes four separate colors that can be blended, reducing the number of necessary instructions.

 

 





