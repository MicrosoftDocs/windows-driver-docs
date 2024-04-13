---
title: GDI Support for Palettes
description: GDI Support for Palettes
keywords:
- DrvEnablePDEV
- GDI WDK Windows 2000 display , colors
- graphics drivers WDK Windows 2000 display , colors
- color management WDK GDI
- palettes WDK Windows 2000 display
- drawing WDK GDI , colors
- DrvSetPalette
- color index WDK GDI
ms.date: 04/20/2017
---

# GDI Support for Palettes

GDI can do most of the work with regard to palette management. When GDI calls the [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) function, the driver returns its default palette to GDI as part of the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure. The driver must create this palette using the [**EngCreatePalette**](/windows/win32/api/winddi/nf-winddi-engcreatepalette) function.

A palette effectively maps 32-bit *color indexes* into 24-bit RGB color values, which is the way GDI uses palettes. A driver specifies its palette so GDI can determine how different color indexes are to appear on the device.

The driver need not deal with most palette operations and calculations as long as it uses the [**XLATEOBJ**](/windows/win32/api/winddi/ns-winddi-xlateobj) provided by GDI.

If the device supports a modifiable palette, it should implement the function [**DrvSetPalette**](/windows/win32/api/winddi/nf-winddi-drvsetpalette). GDI calls *DrvSetPalette* when an application changes the palette for a device and passes the resulting new palette to the driver. The driver should set its internal hardware palette to match the new palette as closely as possible.

A palette can be defined for GDI in either of the two different formats listed in the following table.

| Palette Format | Description |
| -------------- | ----------- |
| Indexed        | A color index is an index into an array of RGB values. The array can be small, containing, for example, 16 color indexes, or large, containing, for example, 4096 color indexes or more. |
| Bit Fields     | Bit fields in the color index specify colors in terms of the amounts of R, G, and B in each color. For example, 5 bits could be used for each, providing a value between 0 and 31 for each color. The 5-bit value would be scaled up to cover a range of 0 to 255 for each component when converting to RGB. (The usual RGB representation itself is defined by bitfields.) |

GDI typically uses the palette mapping in reverse. That is, an application specifies an RGB color for drawing and GDI must locate the color index that causes the device to display that color. As indicated in the next table, GDI provides two primary palette service functions for creating and deleting the palette, as well as some service functions related to the [**PALOBJ**](/windows/win32/api/winddi/ns-winddi-palobj) and the [**XLATEOBJ**](/windows/win32/api/winddi/ns-winddi-xlateobj) used to translate color indexes between two palettes.

| Function | Description |
| -------- | ----------- |
| [**EngCreatePalette**](/windows/win32/api/winddi/nf-winddi-engcreatepalette) | Creates a palette. The driver associates the palette with a device by returning a handle to the palette in the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure. |
| [**EngDeletePalette**](/windows/win32/api/winddi/nf-winddi-engdeletepalette) | Deletes the given palette. |
| [**EngDitherColor**](/windows/win32/api/winddi/nf-winddi-engdithercolor) | Returns a standard 8x8 dither that approximates the specified RGB color. |
| [**EngQueryPalette**](/windows/win32/api/winddi/nf-winddi-engquerypalette) | Queries a palette for its attributes. |
| [**PALOBJ_cGetColors**](/windows/win32/api/winddi/nf-winddi-palobj_cgetcolors) | Allows a driver to download RGB colors from an indexed palette. Called by the display driver in the [**DrvSetPalette**](/windows/win32/api/winddi/nf-winddi-drvsetpalette) function. |
| [**XLATEOBJ_cGetPalette**](/windows/win32/api/winddi/nf-winddi-xlateobj_cgetpalette) | Retrieves the 24-bit RGB colors or the bitfield format for the colors in an indexed source palette. The driver can use this function to obtain information from the palette to perform color blending. |
| [**XLATEOBJ_hGetColorTransform**](/windows/win32/api/winddi/nf-winddi-xlateobj_hgetcolortransform) | Returns the color transform for the specified translation object. |
| [**XLATEOBJ_iXlate**](/windows/win32/api/winddi/nf-winddi-xlateobj_ixlate) | Translates a single source color index to a destination color index. |
[**XLATEOBJ_piVector**](/windows/win32/api/winddi/nf-winddi-xlateobj_pivector) | Retrieves a translation vector from an indexed source palette. The driver can use this vector to perform its own translation of the source indexes to destination indexes. |
