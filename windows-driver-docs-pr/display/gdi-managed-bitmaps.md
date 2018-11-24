---
title: GDI-Managed Bitmaps
description: GDI-Managed Bitmaps
ms.assetid: 4b575574-7090-4010-962b-80cac059bfa5
keywords:
- GDI WDK Windows 2000 display , rendering engine
- graphics drivers WDK Windows 2000 display , rendering engine
- drawing WDK GDI , rendering engine
- rendering engine WDK GDI
- GDI WDK Windows 2000 display , bitmaps
- graphics drivers WDK Windows 2000 display , bitmaps
- drawing WDK GDI , bitmaps
- bitmaps WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI-Managed Bitmaps


## <span id="ddk_gdi_managed_bitmaps_gg"></span><span id="DDK_GDI_MANAGED_BITMAPS_GG"></span>


GDI manages bitmaps in all [*DIB*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-) formats including 1, 4, 8, 16, 24, and 32 bits-per-pixel. GDI can do all line drawing, filling, text output, and bit block transfer (bitblt) operations on these bitmaps. This makes it possible for the driver to either have GDI do all graphics rendering, or to implement functions for which its hardware offers special support.

If the device has a [*frame buffer*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-frame-buffer) in a DIB format, GDI can perform any or all graphics output directly to the frame buffer, thereby reducing the size of the driver. If the device uses a nonstandard-format frame buffer, then the driver must implement all required [drawing functions](optional-display-driver-functions.md). GDI can still simulate most drawing functions, although a performance cost is incurred: the pixels must be copied into a standard format bitmap before they can be operated on by GDI, and then be copied back to the original format after drawing is complete.

 

 





