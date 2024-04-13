---
title: DirectDraw and Color Space Conversion
description: DirectDraw and Color Space Conversion
keywords:
- surfaces WDK DirectDraw , blitting
- drawing blt WDK DirectDraw , color space conversions
- DirectDraw blitting WDK Windows 2000 display , color space conversions
- blitting WDK DirectDraw , color space conversions
- blt WDK DirectDraw , color space conversions
- YUV formats WDK DirectDraw
- FOURCCs
- color space WDK DirectDraw
- converting color space
ms.date: 04/20/2017
---

# DirectDraw and Color Space Conversion


## <span id="ddk_directdraw_and_color_space_conversion_gg"></span><span id="DDK_DIRECTDRAW_AND_COLOR_SPACE_CONVERSION_GG"></span>


DirectDraw allows surfaces to be created and stored in YUV formats. Four Character Codes (*FOURCCs*) denote what color space conversions are being used. Then, during the overlay process, the image is converted to 16-bit RGB. YUV 4:2:2 is effectively the same density as 16 bits per pixel (bpp), but the color fidelity is better. The image can be written in as YUV and go into display memory as RGB, but normally the translation is done as it is read out of display memory so that the compression is maintained. This saves display memory and speeds up playback. For Windows 2000 and later, some YUV formats (UYVY and YUY2 âˆ’ both types of 4:2:2) are emulated, but only when used as textures. Note that unsupported YUV format surfaces cannot be created in system memory.

Three common YUV color spaces are:

-   4:2:2 (standard television is of this type)

-   4:1:1 (more compressed)

-   4:4:4 (similar to RGB)

There are many varieties of these color spaces and many other YUV formats in use today. For information about FOURCC, go to the [FOURCC](https://go.microsoft.com/fwlink/p/?linkid=8697) website.

 

 





