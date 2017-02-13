---
title: Supporting Graphics DDI Font and Text Functions
description: Supporting Graphics DDI Font and Text Functions
ms.assetid: c8abf3bd-7a5a-4a48-988e-a1de1b426656
keywords: ["fonts WDK graphics", "GDI WDK Windows 2000 display , fonts", "graphics drivers WDK Windows 2000 display , fonts", "GDI WDK Windows 2000 display , text output", "graphics drivers WDK Windows 2000 display , text output", "text output WDK graphics", "drawing WDK GDI , fonts", "drawing WDK GDI , text output"]
---

# Supporting Graphics DDI Font and Text Functions


## <span id="ddk_supporting_graphics_ddi_font_and_text_functions_gg"></span><span id="DDK_SUPPORTING_GRAPHICS_DDI_FONT_AND_TEXT_FUNCTIONS_GG"></span>


For many devices, GDI can handle all font functions. Some drivers, however, can draw their own fonts, or their device's own fonts, on device surfaces. Other drivers are font drivers, which can provide glyph bitmaps and/or outlines, as well as glyph metrics to GDI. In these cases, the driver must support some of the available font functions.

Text output is a more general function. If the surface is a standard-format bitmap, GDI can handle all text output, unless the driver hooks out the call to enhance performance. For a device-managed surface, the driver must support text output.

The following topics provide information with regard to the support of font and text management functions.

[Managing and Optimizing Fonts](managing-and-optimizing-fonts.md)

[Drawing Text](drawing-text.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Graphics%20DDI%20Font%20and%20Text%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




