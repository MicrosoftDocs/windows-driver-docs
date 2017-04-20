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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Color Fills and Pattern Fills


## <span id="ddk_color_fills_and_pattern_fills_gg"></span><span id="DDK_COLOR_FILLS_AND_PATTERN_FILLS_GG"></span>


A color fill, as described by a rectangle, fills an area of the screen with a particular color. On most cards, only the address of display memory, the dimensions of the rectangle, and the color are needed. Some cards require beginning and ending X and Y coordinates. Note that Windows automatically drops the last line of these coordinates. For example, when they are numbered from 0 to 640, Windows drops line 640.

Some cards use a pattern fill, which can accomplish the same thing as a color fill. An 8 x 8 region of pixels (the pattern) makes up the desired color, and that pattern is used to fill the specified area. The pattern is set to equal the color desired and filled in the same as a color fill. A pattern fill takes four separate colors that can be blended, reducing the number of necessary instructions.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Color%20Fills%20and%20Pattern%20Fills%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




