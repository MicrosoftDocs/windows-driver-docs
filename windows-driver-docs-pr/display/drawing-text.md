---
title: Drawing Text
description: Drawing Text
keywords:
- GDI WDK Windows 2000 display , text output
- graphics drivers WDK Windows 2000 display , text output
- text output WDK graphics
- DrvTextOut
- DrvGetGlyphMode
- surface text output WDK GDI
- GDI WDK Windows 2000 display , text output, drawing
- graphics drivers WDK Windows 2000 display , text output, drawing
- drawing text WDK GDI
ms.date: 04/20/2017
---

# Drawing Text

The text output functions are called only for a *device-managed surface* (a device bitmap or surface), or for a GDI-managed surface if the driver has hooked the call in the [**EngAssociateSurface**](/windows/win32/api/winddi/nf-winddi-engassociatesurface) function. The graphic output primitives for text are the functions:

* [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout)
* [**DrvGetGlyphMode**](/windows/win32/api/winddi/nf-winddi-drvgetglyphmode)

GDI calls **DrvTextOut** to render the pixels for a set of glyphs at specified positions for text output. Many of the **DrvTextOut** capabilities are defined with the GCAPS bits of the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure returned by the [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) function.

The input parameters for **DrvTextOut** define two sets of pixels, *foreground* and *opaque*. The driver renders the surface to provide the following results:

1. The opaque pixels are rendered first, with the opaque brush.

2. The foreground pixels are then rendered with the foreground brush.

Each of these rendering operations is performed in a *clip region*. The pixels outside the clip region cannot be affected.

The driver must render the surface so opaque pixels are calculated and drawn on the surface first with an opaque brush. Then foreground pixels are calculated and rendered with a foreground brush. Each of these operations is limited by clipping.

Foreground and opaque pixels make up a mask through which color is brushed onto the surface. The glyphs of a font do not, in themselves, have color. The foreground set of pixels is defined as the union of the glyphs' pixels and the pixels of certain extra rectangles used to simulate strikethrough or underline. Opaque pixels are defined by opaque rectangles.

**DrvTextOut** selects the specified font using a pointer, pfo, to query the current [**FONTOBJ**](/windows/win32/api/winddi/ns-winddi-fontobj) structure. This process can include downloading a soft font or a font substitution, or any other font optimizations necessary for the device.

If a driver has scalable fonts, it should call the [**FONTOBJ_pxoGetXform**](/windows/win32/api/winddi/nf-winddi-fontobj_pxogetxform) function for the current FONTOBJ structure, to return the notional-to-device transform for the associated font. This is required for a driver-supplied font. Notional space is the design space of the device font. For example, PostScript fonts are defined in 1000-by-1000 unit character cells. Most of the metrics returned in the [**IFIMETRICS**](/windows/win32/api/winddi/ns-winddi-ifimetrics) structure are converted to notional space, which is why the notional-to-device transform is necessary.

The graphics engine queries the driver by calling the function [**DrvGetGlyphMode**](/windows/win32/api/winddi/nf-winddi-drvgetglyphmode) to find out how it should internally cache its font information. It can cache individual glyphs as bitmaps, outlines, or neither (the proper choice for device fonts).
