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

As described in GDI Support for Graphics Drivers management work. The driver must supply its default palette to GDI in the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure when GDI calls the function [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev). At this time, the driver should create the default palette with a call to the GDI service function [**EngCreatePalette**](/windows/win32/api/winddi/nf-winddi-engcreatepalette).

Drivers that support settable palettes also must support the [**DrvSetPalette**](/windows/win32/api/winddi/nf-winddi-drvsetpalette) function. This function is used exclusively by display drivers.
