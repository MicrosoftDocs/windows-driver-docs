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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Palettes


## <span id="ddk_managing_palettes_gg"></span><span id="DDK_MANAGING_PALETTES_GG"></span>


As described in [GDI Support for Graphics Drivers](gdi-support-for-graphics-drivers.md), GDI handles much of the [*palette*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-palette) management work. The driver must supply its default palette to GDI in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure when GDI calls the function [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211). At this time, the driver should create the default palette with a call to the GDI service function [**EngCreatePalette**](https://msdn.microsoft.com/library/windows/hardware/ff564212).

Drivers that support settable palettes also must support the [**DrvSetPalette**](https://msdn.microsoft.com/library/windows/hardware/ff556282) function. This function is used exclusively by display drivers.

 

 





