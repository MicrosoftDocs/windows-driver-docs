---
title: GDI-Supplied Halftoning
description: GDI-Supplied Halftoning
ms.assetid: c7f3d148-4620-4060-bbf8-253e9e35c397
keywords:
- GDI-supplied halftoning WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI-Supplied Halftoning





If a specified color format is one for which the number of bits per pixel used for rendering the image (\*DrvBPP) is the same as the bits per pixel supported by the printer (\*DevBPP multiplied by \*DevNumOfPlanes), then halftoning operations are handled by GDI. An example is a \*DrvBPP value of four, with \*DevBPP equal to one and \*DevNumOfPlanes equal to four.

For such a situation, the only halftoning methods allowed are those that GDI provides. These halftoning methods are represented in GPD files by the standard halftoning option names, which are listed under [Standard Options](standard-options.md). To specify the GDI-supported halftoning methods that you want Unidrv to allow for your printer, specify their names in \*Option entries for the Halftone feature. (The Halftone feature is one of the standard [printer features](printer-features.md).)

If you specify several halftoning methods and color modes in your GPD file, and if you want to limit which halftoning methods can be selected with which color modes, use [option constraints](option-constraints.md).

Unidrv uses the standard HT\_PATSIZE\_AUTO option if no halftoning options are specified in the GPD file. The HT\_PATSIZE\_AUTO option causes Unidrv to use the standard halftoning method that is optimum for the selected resolution and color mode. This enables a user to switch among various combinations of resolution and color mode without the need to know the best halftoning option for any particular combination.

When using GDI-supplied halftoning capabilities, you can provide [minidriver-supplied halftone patterns](minidriver-supplied-halftone-patterns.md).

For more information about color formats, see [Handling Color Formats](handling-color-formats.md).

 

 




