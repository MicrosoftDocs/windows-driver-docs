---
title: Handling Device-Managed Surfaces
description: Handling Device-Managed Surfaces
keywords:
- Unidrv, device-managed surfaces
- device-managed surfaces WDK Unidrv
- surface device-managed WDK Unidrv
- hooking graphics DDI functions WDK Unidrv
- DrvTextOut
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Device-Managed Surfaces





When Unidrv renders print page images, it uses GDI-managed drawing surfaces. All images are rendered as bitmaps. For devices with capabilities that cannot be exploited by this scenario, such as the ability to draw vectors, you can provide customized driver support for a device-managed drawing surface. To support a device-managed surface, you must provide a rendering plug-in that implements the following:

-   A set of hooking functions for all the Unidrv-supported graphics DDI drawing functions. The following functions must be hooked:
    [**DrvAlphaBlend**](/windows/win32/api/winddi/nf-winddi-drvalphablend)
    [**DrvBitBlt**](/windows/win32/api/winddi/nf-winddi-drvbitblt)
    [**DrvCopyBits**](/windows/win32/api/winddi/nf-winddi-drvcopybits)
    [**DrvDitherColor**](/windows/win32/api/winddi/nf-winddi-drvdithercolor)
    [**DrvFillPath**](/windows/win32/api/winddi/nf-winddi-drvfillpath)
    [**DrvGradientFill**](/windows/win32/api/winddi/nf-winddi-drvgradientfill)
    [**DrvLineTo**](/windows/win32/api/winddi/nf-winddi-drvlineto)
    [**DrvPlgBlt**](/windows/win32/api/winddi/nf-winddi-drvplgblt)
    [**DrvRealizeBrush**](/windows/win32/api/winddi/nf-winddi-drvrealizebrush)
    [**DrvStretchBlt**](/windows/win32/api/winddi/nf-winddi-drvstretchblt)
    [**DrvStretchBltROP**](/windows/win32/api/winddi/nf-winddi-drvstretchbltrop)
    [**DrvStrokeAndFillPath**](/windows/win32/api/winddi/nf-winddi-drvstrokeandfillpath)
    [**DrvStrokePath**](/windows/win32/api/winddi/nf-winddi-drvstrokepath)
    [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout)
    [**DrvTransparentBlt**](/windows/win32/api/winddi/nf-winddi-drvtransparentblt)
-   The [**IPrintOemUni::EnableDriver**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enabledriver) method, which is used to provide Unidrv with pointers to the graphics DDI hooking functions.

-   The [**IPrintOemUni::DriverDMS**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-driverdms) method, which informs Unidrv that a device-managed surface is to be used, and specifies which of the defined hooking functions will be used for the surface.

The hooking functions cannot call back to GDI's Eng-prefixed support services when drawing on a device-managed surface. However, they can create a temporary bitmap surface, and then pass that surface's handle to Eng-prefixed drawing functions (see [Rendering a Print Job](rendering-a-print-job.md)).

The [**IPrintOemUni::DriverDMS**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-driverdms) method is called each time a print job is about to be rendered, so the rendering plug-in can specify the type of rendering surface (GDI-managed or device-managed) for each job. Basing the surface choice on a selectable option in the user interface requires you to also provide a [user interface plug-in](user-interface-plug-ins.md).

### Drawing Text on a Device-Managed Surface

The rendering plug-in must hook out Unidrv's [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout) function (along with all other graphics DDI drawing functions). Creating text for a device-managed surface involves interaction among the following four functions:

-   Unidrv's [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout) function

-   Rendering plug-in's [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout) hooking function

-   Unidrv's [**IPrintOemDriverUni::DrvUniTextOut**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvunitextout) method

-   Rendering plug-in's [**IPrintOemUni::TextOutAsBitmap**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-textoutasbitmap) method

The steps involved in displaying text on a device-managed surface are as follows:

1.  GDI calls Unidrv's [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout) function.

2.  Unidrv calls the rendering plug-in's [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout) hooking function.

3.  The hooking function sends commands to the device to specify the text's brush, rotation, and clip region.

4.  The hooking function calls Unidrv's [**IPrintOemDriverUni::DrvUniTextOut**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvunitextout) method, which uses downloaded fonts to output the text. This method also handles glyph-based clipping.

5.  If [**IPrintOemDriverUni::DrvUniTextOut**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvunitextout) cannot use a downloadable font (because the font is not available or is rotated), it calls the rendering plug-in's [**IPrintOemUni::TextOutAsBitmap**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-textoutasbitmap) method, which draws the text as a bitmap.

6.  After [**IPrintOemDriverUni::DrvUniTextOut**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvunitextout) returns, the [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout) hooking function must draw underlines and strike-throughs, based on the rectangles specified by the **DrvTextOut** function's *prclExtra* parameter, using vector commands (if supported).

 

