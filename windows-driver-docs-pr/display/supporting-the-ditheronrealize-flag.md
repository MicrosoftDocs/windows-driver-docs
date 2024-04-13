---
title: Supporting the DitherOnRealize Flag
description: Supporting the DitherOnRealize Flag
keywords:
- display drivers WDK Windows 2000 , dithering
- DrvDitherColor
- dithering WDK Windows 2000 display
- color dithering WDK Windows 2000 display
ms.date: 04/20/2017
---

# Supporting the DitherOnRealize Flag

In earlier versions of GDI and the graphics DDI, two calls by GDI to display driver functions were required to dither a specified color and then realize a brush for that color. For example, when an application requests that a rectangle be filled with a dithered color, GDI typically calls [**DrvBitBlt**](/windows/win32/api/winddi/nf-winddi-drvbitblt), passing the extents of the rectangle and the brush object to use. The display driver then checks the brush, finds that it has not been realized, and calls back to GDI with [**BRUSHOBJ_pvGetRbrush**](/windows/win32/api/winddi/nf-winddi-brushobj_pvgetrbrush) for GDI's realization of the brush. Because the display driver, not GDI, performs the dithering of a brush, GDI passes the RGB that the application originally supplied for dithering in a [**DrvDitherColor**](/windows/win32/api/winddi/nf-winddi-drvdithercolor) callback to the display driver.

*DrvDitherColor* returns a pointer to an array of color indexes that describe the dither information for the supplied color back to GDI. GDI immediately passes this dither information back to the display driver in a call to [**DrvRealizeBrush**](/windows/win32/api/winddi/nf-winddi-drvrealizebrush). With the [**BRUSHOBJ**](/windows/win32/api/winddi/ns-winddi-brushobj) realized, control returns back to GDI and subsequently back to the original *DrvBitBlt* function.

To accomplish dithering using the above technique, GDI must call *DrvDitherColor*, followed immediately by a call to *DrvRealizeBrush* -- two separate function calls. Setting a GCAPS_DITHERONREALIZE flag in the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure and modifying *DrvRealizeBrush* to effectively combine these two functions eliminates the need for the separate call to *DrvDitherColor* and also saves some memory allocation. Under this scheme, if the display driver sets GCAPS_DITHERONREALIZE, GDI calls *DrvRealizeBrush* with the RGB to be dithered and with the RB_DITHERCOLOR flag set in *iHatch*. The RB_DITHERCOLOR flag is set in the high byte of *iHatch*, while the RGB color to be dithered is contained in the three low-order bytes. The need to call *DrvDitherColor* is eliminated in this situation because the functionality of both calls is put into one.

For example code, refer to the *Permedia* sample display drivers.

> [!NOTE]
> The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm*) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the DDK - Windows Driver Development Kit page of the WDHC website.
