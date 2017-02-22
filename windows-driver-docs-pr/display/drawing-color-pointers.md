---
title: Drawing Color Pointers
description: Drawing Color Pointers
ms.assetid: f2791ccc-3d9e-46f0-bc70-051ac298c1ee
keywords: ["drawing pointers WDK Windows 2000 display", "display drivers WDK Windows 2000 , pointers", "pointers WDK Windows 2000 display", "color pointers WDK Windows 2000 display"]
---

# Drawing Color Pointers


## <span id="ddk_drawing_color_pointers_gg"></span><span id="DDK_DRAWING_COLOR_POINTERS_GG"></span>


Defining the color pointer in the same way as the monochrome pointer (that is, as a bitmap that includes an AND portion and an XOR portion -- see [Pointer Drawing](pointer-drawing.md) and [Drawing Monochrome Pointers](drawing-monochrome-pointers.md)) also supports transparency and inversion.

-   If the color bitmap is black (index 0) and the AND mask value is 1, then the result is transparency.

-   If the color bitmap is white and the AND mask value is 1, then the result is inversion.

-   If the device cannot display color, then a pointer can be drawn as black and white.

These conventions allow applications to use a single pointer definition for both color and monochrome displays.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Drawing%20Color%20Pointers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




