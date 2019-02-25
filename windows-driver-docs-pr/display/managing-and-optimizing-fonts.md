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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing and Optimizing Fonts


## <span id="ddk_managing_and_optimizing_fonts_gg"></span><span id="DDK_MANAGING_AND_OPTIMIZING_FONTS_GG"></span>


A *producer* is a driver that can generate fonts. It produces glyph information as output, including glyph metrics, bitmaps, and outlines. A *consumer* is a driver that uses fonts. It accepts glyph information as input for generating text output, and must draw its own fonts or those of the hardware on a device-managed surface. A driver can be both a producer and a consumer. For example, a printer driver can act as a producer while servicing a [**DrvQueryFontData**](https://msdn.microsoft.com/library/windows/hardware/ff556264) call to provide glyph metrics and later act as a consumer while processing a [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277) call.

A driver is required to handle fonts only when it is a font producer or a font consumer. If the hardware has a resident font, the driver must supply information to GDI about this font, including the font metrics in the [**IFIMETRICS**](https://msdn.microsoft.com/library/windows/hardware/ff567418) structure, mappings from Unicode to individual glyph identities, individual glyph attributes, and kerning tables. There are also functions the driver must support. Some functions are required both by font drivers and drivers that use driver-specific or device-specific fonts. Others are required only by font drivers.

The support of font functions depends on the driver's abilities. The general types are:

[Metrics functions](font-metric-functions.md)

[Glyph functions](font-driver-functions.md)

[TrueType functions](truetype-font-driver-functions.md)

 

 





