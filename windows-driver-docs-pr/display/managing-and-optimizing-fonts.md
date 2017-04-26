---
title: Managing and Optimizing Fonts
description: Managing and Optimizing Fonts
ms.assetid: 5cfc2174-c605-4399-97a6-62f51df21c16
keywords:
- fonts WDK graphics , managing and optimizing
- GDI WDK Windows 2000 display , fonts, managing and optimizing
- graphics drivers WDK Windows 2000 display , fonts, managing and optimizing
- producers WDK graphics
- consumers WDK GDI
- glyph information WDK graphics
- GDI WDK Windows 2000 display , text output, managing and optimizing
- graphics drivers WDK Windows 2000 display , text output, managing and optimizing fonts
- drawing WDK GDI , fonts, managing and optimizing
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Managing and Optimizing Fonts


## <span id="ddk_managing_and_optimizing_fonts_gg"></span><span id="DDK_MANAGING_AND_OPTIMIZING_FONTS_GG"></span>


A *producer* is a driver that can generate fonts. It produces glyph information as output, including glyph metrics, bitmaps, and outlines. A *consumer* is a driver that uses fonts. It accepts glyph information as input for generating text output, and must draw its own fonts or those of the hardware on a device-managed surface. A driver can be both a producer and a consumer. For example, a printer driver can act as a producer while servicing a [**DrvQueryFontData**](https://msdn.microsoft.com/library/windows/hardware/ff556264) call to provide glyph metrics and later act as a consumer while processing a [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277) call.

A driver is required to handle fonts only when it is a font producer or a font consumer. If the hardware has a resident font, the driver must supply information to GDI about this font, including the font metrics in the [**IFIMETRICS**](https://msdn.microsoft.com/library/windows/hardware/ff567418) structure, mappings from Unicode to individual glyph identities, individual glyph attributes, and kerning tables. There are also functions the driver must support. Some functions are required both by font drivers and drivers that use driver-specific or device-specific fonts. Others are required only by font drivers.

The support of font functions depends on the driver's abilities. The general types are:

[Metrics functions](font-metric-functions.md)

[Glyph functions](font-driver-functions.md)

[TrueType functions](truetype-font-driver-functions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Managing%20and%20Optimizing%20Fonts%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




