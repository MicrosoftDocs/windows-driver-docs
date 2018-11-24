---
title: Supporting Graphics DDI Font and Text Functions
description: Supporting Graphics DDI Font and Text Functions
ms.assetid: c8abf3bd-7a5a-4a48-988e-a1de1b426656
keywords:
- fonts WDK graphics
- GDI WDK Windows 2000 display , fonts
- graphics drivers WDK Windows 2000 display , fonts
- GDI WDK Windows 2000 display , text output
- graphics drivers WDK Windows 2000 display , text output
- text output WDK graphics
- drawing WDK GDI , fonts
- drawing WDK GDI , text output
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Graphics DDI Font and Text Functions


## <span id="ddk_supporting_graphics_ddi_font_and_text_functions_gg"></span><span id="DDK_SUPPORTING_GRAPHICS_DDI_FONT_AND_TEXT_FUNCTIONS_GG"></span>


For many devices, GDI can handle all font functions. Some drivers, however, can draw their own fonts, or their device's own fonts, on device surfaces. Other drivers are font drivers, which can provide glyph bitmaps and/or outlines, as well as glyph metrics to GDI. In these cases, the driver must support some of the available font functions.

Text output is a more general function. If the surface is a standard-format bitmap, GDI can handle all text output, unless the driver hooks out the call to enhance performance. For a device-managed surface, the driver must support text output.

The following topics provide information with regard to the support of font and text management functions.

[Managing and Optimizing Fonts](managing-and-optimizing-fonts.md)

[Drawing Text](drawing-text.md)

 

 





