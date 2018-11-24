---
title: Managing Display Palettes
description: Managing Display Palettes
ms.assetid: a0ff1a9c-82dc-4317-a0ec-c387027a52ba
keywords:
- display drivers WDK Windows 2000 , palettes
- color lookup tables WDK Windows 2000 display
- palettes WDK Windows 2000 display
- color palettes WDK Windows 2000 display
- color index WDK Windows 2000 display
- settable palettes WDK Windows 2000 display
- indexed palettes WDK Windows 2000 display
- RGB colors WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Display Palettes


## <span id="ddk_managing_display_palettes_gg"></span><span id="DDK_MANAGING_DISPLAY_PALETTES_GG"></span>


If the video hardware supports colors that can be set, it maintains a color lookup table called a [*palette*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-palette). GDI takes each RGB value and translates it into a device [*color index*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-color-index) so that it can be displayed. GDI uses precalculated and cached tables for the translation. These tables are accessible to drivers as the user object [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634). Therefore, every GDI graphics function that takes source colors and moves them to a destination device uses a XLATEOBJ structure to translate the colors. For more information about palettes and how GDI handles them, see [GDI Support for Palettes](gdi-support-for-palettes.md).

If the video hardware supports palettes that can be set, GDI calls the [**DrvSetPalette**](https://msdn.microsoft.com/library/windows/hardware/ff556282) function in the display driver when it has finished mapping colors into the [*device palette*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-palette) requested by the application. GDI passes the new palette to the display driver, and the driver queries the [**PALOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff568844) to set its internal hardware palette to match the palette changes for the video hardware. This is known as [*palette realization*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-palette-realization).

The *DrvSetPalette* function supplies a handle to a [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) to the driver, and requests the driver to realize the palette for that device. The driver should set the hardware palette to match the entries in the given palette as closely as possible.

This entry point is required if the device supports a palette that can be set, and should not be provided otherwise. A display driver specifies that its device has a settable palette by setting the GCAPS\_PALMANAGED bit in the **flGraphicsCaps** field of the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure returned in [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211).

The service routine [**PALOBJ\_cGetColors**](https://msdn.microsoft.com/library/windows/hardware/ff568845) is available to display drivers. This function downloads RGB colors from an indexed palette, and should be called from within the implementation of *DrvSetPalette*.

 

 





