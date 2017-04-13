---
title: Handling Device-Managed Surfaces
author: windows-driver-content
description: Handling Device-Managed Surfaces
ms.assetid: 4403165f-c528-450e-9c96-77a9ce0778aa
keywords: ["Unidrv, device-managed surfaces", "device-managed surfaces WDK Unidrv", "surface device-managed WDK Unidrv", "hooking graphics DDI functions WDK Unidrv", "DrvTextOut", "Unidrv WDK print"]
---

# Handling Device-Managed Surfaces


## <a href="" id="ddk-handling-device-managed-surfaces-gg"></a>


When Unidrv renders print page images, it uses GDI-managed drawing surfaces. All images are rendered as bitmaps. For devices with capabilities that cannot be exploited by this scenario, such as the ability to draw vectors, you can provide customized driver support for a device-managed drawing surface. To support a device-managed surface, you must provide a rendering plug-in that implements the following:

-   A set of hooking functions for all the Unidrv-supported graphics DDI drawing functions. The following functions must be hooked:
    [**DrvAlphaBlend**](https://msdn.microsoft.com/library/windows/hardware/ff556176)
    [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180)
    [**DrvCopyBits**](https://msdn.microsoft.com/library/windows/hardware/ff556182)
    [**DrvDitherColor**](https://msdn.microsoft.com/library/windows/hardware/ff556202)
    [**DrvFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556220)
    [**DrvGradientFill**](https://msdn.microsoft.com/library/windows/hardware/ff556236)
    [**DrvLineTo**](https://msdn.microsoft.com/library/windows/hardware/ff556245)
    [**DrvPlgBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556258)
    [**DrvRealizeBrush**](https://msdn.microsoft.com/library/windows/hardware/ff556273)
    [**DrvStretchBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556302)
    [**DrvStretchBltROP**](https://msdn.microsoft.com/library/windows/hardware/ff556306)
    [**DrvStrokeAndFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556311)
    [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316)
    [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277)
    [**DrvTransparentBlt**](https://msdn.microsoft.com/library/windows/hardware/ff557283)
-   The [**IPrintOemUni::EnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff554248) method, which is used to provide Unidrv with pointers to the graphics DDI hooking functions.

-   The [**IPrintOemUni::DriverDMS**](https://msdn.microsoft.com/library/windows/hardware/ff554245) method, which informs Unidrv that a device-managed surface is to be used, and specifies which of the defined hooking functions will be used for the surface.

The hooking functions cannot call back to GDI's Eng-prefixed support services when drawing on a device-managed surface. However, they can create a temporary bitmap surface, and then pass that surface's handle to Eng-prefixed drawing functions (see [Rendering a Print Job](rendering-a-print-job.md)).

The [**IPrintOemUni::DriverDMS**](https://msdn.microsoft.com/library/windows/hardware/ff554245) method is called each time a print job is about to be rendered, so the rendering plug-in can specify the type of rendering surface (GDI-managed or device-managed) for each job. Basing the surface choice on a selectable option in the user interface requires you to also provide a [user interface plug-in](user-interface-plug-ins.md).

### Drawing Text on a Device-Managed Surface

The rendering plug-in must hook out Unidrv's [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277) function (along with all other graphics DDI drawing functions). Creating text for a device-managed surface involves interaction among the following four functions:

-   Unidrv's [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277) function

-   Rendering plug-in's [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277) hooking function

-   Unidrv's [**IPrintOemDriverUni::DrvUniTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff553132) method

-   Rendering plug-in's [**IPrintOemUni::TextOutAsBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff554277) method

The steps involved in displaying text on a device-managed surface are as follows:

1.  GDI calls Unidrv's [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277) function.

2.  Unidrv calls the rendering plug-in's [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277) hooking function.

3.  The hooking function sends commands to the device to specify the text's brush, rotation, and clip region.

4.  The hooking function calls Unidrv's [**IPrintOemDriverUni::DrvUniTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff553132) method, which uses downloaded fonts to output the text. This method also handles glyph-based clipping.

5.  If [**IPrintOemDriverUni::DrvUniTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff553132) cannot use a downloadable font (because the font is not available or is rotated), it calls the rendering plug-in's [**IPrintOemUni::TextOutAsBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff554277) method, which draws the text as a bitmap.

6.  After [**IPrintOemDriverUni::DrvUniTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff553132) returns, the [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277) hooking function must draw underlines and strike-throughs, based on the rectangles specified by the **DrvTextOut** function's *prclExtra* parameter, using vector commands (if supported).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Handling%20Device-Managed%20Surfaces%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


