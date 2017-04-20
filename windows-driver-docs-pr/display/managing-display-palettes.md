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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Managing Display Palettes


## <span id="ddk_managing_display_palettes_gg"></span><span id="DDK_MANAGING_DISPLAY_PALETTES_GG"></span>


If the video hardware supports colors that can be set, it maintains a color lookup table called a [*palette*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-palette). GDI takes each RGB value and translates it into a device [*color index*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-color-index) so that it can be displayed. GDI uses precalculated and cached tables for the translation. These tables are accessible to drivers as the user object [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634). Therefore, every GDI graphics function that takes source colors and moves them to a destination device uses a XLATEOBJ structure to translate the colors. For more information about palettes and how GDI handles them, see [GDI Support for Palettes](gdi-support-for-palettes.md).

If the video hardware supports palettes that can be set, GDI calls the [**DrvSetPalette**](https://msdn.microsoft.com/library/windows/hardware/ff556282) function in the display driver when it has finished mapping colors into the [*device palette*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-palette) requested by the application. GDI passes the new palette to the display driver, and the driver queries the [**PALOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff568844) to set its internal hardware palette to match the palette changes for the video hardware. This is known as [*palette realization*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-palette-realization).

The *DrvSetPalette* function supplies a handle to a [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) to the driver, and requests the driver to realize the palette for that device. The driver should set the hardware palette to match the entries in the given palette as closely as possible.

This entry point is required if the device supports a palette that can be set, and should not be provided otherwise. A display driver specifies that its device has a settable palette by setting the GCAPS\_PALMANAGED bit in the **flGraphicsCaps** field of the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure returned in [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211).

The service routine [**PALOBJ\_cGetColors**](https://msdn.microsoft.com/library/windows/hardware/ff568845) is available to display drivers. This function downloads RGB colors from an indexed palette, and should be called from within the implementation of *DrvSetPalette*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Managing%20Display%20Palettes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




