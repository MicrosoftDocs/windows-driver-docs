---
title: Managing Palettes
description: Managing Palettes
ms.assetid: 7917b01f-f57d-4262-80b6-9e11e797e3b5
keywords:
- GDI WDK Windows 2000 display , colors
- graphics drivers WDK Windows 2000 display , colors
- color management WDK GDI
- palettes WDK Windows 2000 display
- drawing WDK GDI , colors
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Managing Palettes


## <span id="ddk_managing_palettes_gg"></span><span id="DDK_MANAGING_PALETTES_GG"></span>


As described in [GDI Support for Graphics Drivers](gdi-support-for-graphics-drivers.md), GDI handles much of the [*palette*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-palette) management work. The driver must supply its default palette to GDI in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure when GDI calls the function [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211). At this time, the driver should create the default palette with a call to the GDI service function [**EngCreatePalette**](https://msdn.microsoft.com/library/windows/hardware/ff564212).

Drivers that support settable palettes also must support the [**DrvSetPalette**](https://msdn.microsoft.com/library/windows/hardware/ff556282) function. This function is used exclusively by display drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Managing%20Palettes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




