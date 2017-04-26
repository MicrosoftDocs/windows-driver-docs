---
title: Halftoning
description: Halftoning
ms.assetid: 94cf0d87-055d-470e-94ca-225d519aeb14
keywords:
- GDI WDK Windows 2000 display , halftoning
- graphics drivers WDK Windows 2000 display , halftoning
- drawing WDK GDI , halftoning
- halftoning WDK GDI
- fixed-cell spacing WDK GDI
- size WDK GDI halftoning
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Halftoning


## <span id="ddk_halftoning_gg"></span><span id="DDK_HALFTONING_GG"></span>


Traditional analog halftoning uses a halftoning screen, composed of cells of equal sizes, with fixed-cell spacing center-to-center. The fixed-cell spacing accommodates the thickness of the ink, while the size of a dot within each cell can vary to produce the impression of a continuous tone.

On a computer, most printing or screen shading also uses a fixed-cell pixel size. To simulate the variable dot size, a combination of cluster pixels simulates the halftone screen. GDI includes halftoning default parameters that provide a good first approximation. Additional device-specific information can be added to the system to improve output.

The driver sends GDI the device-related specifications that GDI needs to do halftoning through the [**GDIINFO**](https://msdn.microsoft.com/library/windows/hardware/ff566484) structure returned by the [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) function. The driver specifies the pattern size with the **ulHTPatternSize** member of GDIINFO, which defines the preferred output format for halftoning. For specific devices, halftoning relates to the halftone pattern sizes. GDI provides numerous predefined pattern sizes from 2 x 2 through 16 x 16.

For each standard pattern size, there is also a modified version. It is identified by the suffix "\_M" on the standard pattern size's name. For example, the defined name of the standard 6-by-6 pattern is HT\_PATSIZE\_6x6, while the name of the modified 6-by-6 pattern is HT\_PATSIZE\_6x6\_M). The modified version gives more color resolution, but can produce a side effect of horizontal or vertical noise. In addition, because each of these pattern sizes is device resolution-dependent, the appropriate pattern size depends upon the specific device.

The tradeoff between pattern size (spatial resolution) and color resolution is determined by the pattern size. A larger halftone pattern produces better color resolution, while a smaller pattern results in the best spatial resolution. Determining the best pattern size is frequently a matter of trial and error. For more information, refer to [**GDIINFO**](https://msdn.microsoft.com/library/windows/hardware/ff566484).

Another of the GDIINFO structure members affecting halftoning is **flHTFlags**, which contains flags that describe the device resolution needed for halftoning.

GDI handles color adjustment requests from the application and passes the information down to driver functions through the graphics DDI. If the application selects halftoning and the surface is a standard format [*DIB*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-), GDI processes the bitmap using its halftoning capabilities, after which, the bitmap is sent to the device. In the PostScript driver, the [**EngStretchBlt**](https://msdn.microsoft.com/library/windows/hardware/ff565025) function can send the bitmap to the printer using either the [**DrvCopyBits**](https://msdn.microsoft.com/library/windows/hardware/ff556182) or [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180) (in the SRCCOPY mode) functions.

Letting GDI perform the halftoning instead of the PostScript printer, for example, provides a faster output with better WYSIWYG quality. An interface to the PostScript driver allows the user to adjust the halftoning and provides a check box to turn off GDI halftoning if the printer's built-in halftoning capabilities are preferred.

The [**DrvDitherColor**](https://msdn.microsoft.com/library/windows/hardware/ff556202) function can return the DCR\_HALFTONE value, which requests that GDI approximate a color using the existing device (halftone) palette. DCR\_HALFTONE can be used with a display driver only when the device contains a device (halftone) palette, such as a VGA-16 adapter card, because it has a standard fixed palette. Monochrome drivers, including most raster printers, can use the *iMode* parameter in *DrvDitherColor* to obtain good gray-scale effects.

**Note**   Windows 2000 and later do not support halftoning on 24-bit (or higher) devices.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Halftoning%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




