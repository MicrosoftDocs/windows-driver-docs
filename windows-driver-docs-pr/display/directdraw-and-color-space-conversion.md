---
title: DirectDraw and Color Space Conversion
description: DirectDraw and Color Space Conversion
ms.assetid: 2a5e59ea-2190-4701-ab7b-7a6503aec6e5
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DirectDraw and Color Space Conversion


## <span id="ddk_directdraw_and_color_space_conversion_gg"></span><span id="DDK_DIRECTDRAW_AND_COLOR_SPACE_CONVERSION_GG"></span>


DirectDraw allows surfaces to be created and stored in YUV formats. Four Character Codes ([*FOURCCs*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc)) denote what color space conversions are being used. Then, during the overlay process, the image is converted to 16-bit RGB. YUV 4:2:2 is effectively the same density as 16 bits per pixel (bpp), but the color fidelity is better. The image can be written in as YUV and go into display memory as RGB, but normally the translation is done as it is read out of display memory so that the compression is maintained. This saves display memory and speeds up playback. For Windows 2000 and later, some YUV formats (UYVY and YUY2 âˆ’ both types of 4:2:2) are emulated, but only when used as textures. Note that unsupported YUV format surfaces cannot be created in system memory.

Three common YUV color spaces are:

-   4:2:2 (standard television is of this type)

-   4:1:1 (more compressed)

-   4:4:4 (similar to RGB)

There are many varieties of these color spaces and many other YUV formats in use today. For information about FOURCC, go to the [FOURCC](http://go.microsoft.com/fwlink/p/?linkid=8697) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DirectDraw%20and%20Color%20Space%20Conversion%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




