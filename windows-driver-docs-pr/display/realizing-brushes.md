---
title: Realizing Brushes
description: Realizing Brushes
keywords:
- GDI WDK Windows 2000 display , patterns
- graphics drivers WDK Windows 2000 display , patterns
- patterns WDK GDI
- brushes WDK GDI
- brush origin WDK GDI
- realizing brushes WDK GDI
- dithering WDK Windows 2000 display
- color dithering WDK Windows 2000 display
- color management WDK GDI
- DrvRealizeBrush
- DrvDitherColor
- surface brush patterns WDK GDI
- fills WDK GDI
- lines WDK GDI
- drawing WDK GDI , brushes
ms.date: 04/20/2017
---

# Realizing Brushes

## How to realize a brush

Graphics functions that output lines, text or fills take at least one brush as an argument. The brush defines the pattern to be used to draw the graphics object on the specified surface. Each output function that takes a brush requires a *brush origin*. The brush origin provides the coordinates of a pixel on the device surface to be aligned with the upper left pixel of the brush's pattern. The brush pattern is repeated (tiled) to cover the whole device surface.

The driver can support the following functions to define brushes:

* [**DrvRealizeBrush**](/windows/win32/api/winddi/nf-winddi-drvrealizebrush)
* [**DrvDitherColor**](/windows/win32/api/winddi/nf-winddi-drvdithercolor)

A brush is always used with a mix mode that defines how the pattern should be mixed with the data already on the device surface. The MIX data type consists of two ROP2 values packed into a single ULONG value. The foreground *ROP* is in the lowest-order byte. The next byte contains the background ROP. For more information, see the Microsoft Windows SDK documentation.

GDI keeps track of all logical brushes that an application has requested for use. Before asking a driver to draw something, GDI first issues a call to the driver function [**DrvRealizeBrush**](/windows/win32/api/winddi/nf-winddi-drvrealizebrush). This allows the driver to compute the optimal representation of the required pattern for its own drawing code.

*DrvRealizeBrush* is called to realize the brush defined by *psoPattern* (pattern for the brush) and by *psoTarget* (surface for the realized brush). A realized brush contains information and accelerators a driver needs to fill an area with a pattern. This information is defined and used only by the driver. Driver realization of a brush is written into a buffer that the driver can cause to be allocated by calling the GDI service function [**BRUSHOBJ_pvAllocRbrush**](/windows/win32/api/winddi/nf-winddi-brushobj_pvallocrbrush) from within *DrvRealizeBrush*. GDI caches all realized brushes; consequently, they seldom need to be recomputed.

In *DrvRealizeBrush*, the [**BRUSHOBJ**](/windows/win32/api/winddi/ns-winddi-brushobj) user object represents the brush. The surface for which the brush is to be realized can be the physical surface for the device, a *DDB*, or a standard-format bitmap. For a raster device, the surface describing the brush pattern represents a bitmap; and for a vector device, it is always one of the pattern surfaces returned by the [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) function. The transparency mask used for the brush is a one-bit-per-pixel bitmap with the same extent as the pattern. A mask bit of zero means that the pixel is considered to be a background pixel for the brush; that is, the target pixel is unaffected by that particular pattern pixel. *DrvRealizeBrush* uses an [**XLATEOBJ**](/windows/win32/api/winddi/ns-winddi-xlateobj) structure to translate the colors in the brush pattern to the device color indexes.

The driver should call the GDI service function [**BRUSHOBJ_pvGetRbrush**](/windows/win32/api/winddi/nf-winddi-brushobj_pvgetrbrush) when the value of the **iSolidColor** member of the BRUSHOBJ structure is 0xFFFFFFFF and the **pvRbrush** member is **NULL**. **BRUSHOBJ_pvGetRbrush** retrieves a pointer to the driver's realization of a specified brush. If the brush has not been realized when the driver calls this function, GDI automatically calls *DrvRealizeBrush* for the driver's realization of the brush.

## Dithering

If necessary, GDI can request the assistance of the driver when trying to create a brush with a solid color that cannot be represented exactly on the hardware. GDI calls the driver function [**DrvDitherColor**](/windows/win32/api/winddi/nf-winddi-drvdithercolor) to request the driver to dither a brush against the reserved portion of the *device palette*.

Dithering uses a pattern of several colors to approximate the chosen color, and its result is an array of device color indexes. A brush created using these colors for its pattern is usually a good approximation of the given color. [**DrvDitherColor**](/windows/win32/api/winddi/nf-winddi-drvdithercolor) can also represent a color that cannot be specified exactly by a device. To do this, *DrvDitherColor* requests a pattern of several colors and creates a brush that approximates the given solid color.

The function *DrvDitherColor* is optional and is called only if the GCAPS_COLOR_DITHER or GCAPS_MONO_DITHER capability flags are set in the **flGraphicsCaps** member of the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure. *DrvDitherColor* can return the values listed in the following table.

| Value | Meaning |
| ----- | ------- |
| DCR_DRIVER | Indicates that the dither values have been calculated by the driver. The handle to a **cxDither** by **cyDither** array of device color indexes is passed back in this case. |
| DCR_HALFTONE | Indicates that GDI should approximate a color using the existing device (halftone) palette. For example, GDI can use the typical palette for a printer that contains only three or four colors. DCR_HALFTONE can be used with a display driver only when the device contains a device (halftone) palette, such as VGA-16 adapter card, which has a standard fixed palette. |
| DCR_SOLID | Indicates that GDI should map the requested color to the nearest color value in the existing device palette (many to one). |

Monochrome drivers should support *DrvDitherColor* in order for GDI to obtain good gray-level patterns.
