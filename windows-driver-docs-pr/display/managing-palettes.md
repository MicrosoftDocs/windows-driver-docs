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


As described in GDI Support for Graphics Drivers management work. The driver must supply its default palette to GDI in the [**DEVINFO**](https://docs.microsoft.com/windows/desktop/api/winddi/ns-winddi-tagdevinfo) structure when GDI calls the function [**DrvEnablePDEV**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-drvenablepdev). At this time, the driver should create the default palette with a call to the GDI service function [**EngCreatePalette**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-engcreatepalette).

Drivers that support settable palettes also must support the [**DrvSetPalette**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-drvsetpalette) function. This function is used exclusively by display drivers.

 

 





