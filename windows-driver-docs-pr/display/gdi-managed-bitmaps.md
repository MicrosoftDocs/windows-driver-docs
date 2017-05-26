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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI-Managed Bitmaps


## <span id="ddk_gdi_managed_bitmaps_gg"></span><span id="DDK_GDI_MANAGED_BITMAPS_GG"></span>


GDI manages bitmaps in all [*DIB*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-) formats including 1, 4, 8, 16, 24, and 32 bits-per-pixel. GDI can do all line drawing, filling, text output, and bit block transfer (bitblt) operations on these bitmaps. This makes it possible for the driver to either have GDI do all graphics rendering, or to implement functions for which its hardware offers special support.

If the device has a [*frame buffer*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-frame-buffer) in a DIB format, GDI can perform any or all graphics output directly to the frame buffer, thereby reducing the size of the driver. If the device uses a nonstandard-format frame buffer, then the driver must implement all required [drawing functions](optional-display-driver-functions.md). GDI can still simulate most drawing functions, although a performance cost is incurred: the pixels must be copied into a standard format bitmap before they can be operated on by GDI, and then be copied back to the original format after drawing is complete.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI-Managed%20Bitmaps%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




