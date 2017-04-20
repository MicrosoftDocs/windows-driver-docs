---
title: GDI-Supplied Halftoning
author: windows-driver-content
description: GDI-Supplied Halftoning
ms.assetid: c7f3d148-4620-4060-bbf8-253e9e35c397
keywords:
- GDI-supplied halftoning WDK Unidrv
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI-Supplied Halftoning


## <a href="" id="ddk-gdi-supplied-halftoning-gg"></a>


If a specified color format is one for which the number of bits per pixel used for rendering the image (\*DrvBPP) is the same as the bits per pixel supported by the printer (\*DevBPP multiplied by \*DevNumOfPlanes), then halftoning operations are handled by GDI. An example is a \*DrvBPP value of four, with \*DevBPP equal to one and \*DevNumOfPlanes equal to four.

For such a situation, the only halftoning methods allowed are those that GDI provides. These halftoning methods are represented in GPD files by the standard halftoning option names, which are listed under [Standard Options](standard-options.md). To specify the GDI-supported halftoning methods that you want Unidrv to allow for your printer, specify their names in \*Option entries for the Halftone feature. (The Halftone feature is one of the standard [printer features](printer-features.md).)

If you specify several halftoning methods and color modes in your GPD file, and if you want to limit which halftoning methods can be selected with which color modes, use [option constraints](option-constraints.md).

Unidrv uses the standard HT\_PATSIZE\_AUTO option if no halftoning options are specified in the GPD file. The HT\_PATSIZE\_AUTO option causes Unidrv to use the standard halftoning method that is optimum for the selected resolution and color mode. This enables a user to switch among various combinations of resolution and color mode without the need to know the best halftoning option for any particular combination.

When using GDI-supplied halftoning capabilities, you can provide [minidriver-supplied halftone patterns](minidriver-supplied-halftone-patterns.md).

For more information about color formats, see [Handling Color Formats](handling-color-formats.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDI-Supplied%20Halftoning%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


