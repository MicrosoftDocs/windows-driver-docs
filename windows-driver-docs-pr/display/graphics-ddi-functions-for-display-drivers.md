---
title: Graphics DDI Functions for Display Drivers
description: Graphics DDI Functions for Display Drivers
ms.assetid: 9edd06bd-7aac-4015-864d-b08f3e3a79fd
keywords:
- display drivers WDK Windows 2000 , graphics
- graphics DDI functions WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Graphics DDI Functions for Display Drivers


## <span id="ddk_graphics_ddi_functions_for_display_drivers_gg"></span><span id="DDK_GRAPHICS_DDI_FUNCTIONS_FOR_DISPLAY_DRIVERS_GG"></span>


A Microsoft NT-based operating system display driver must implement several graphics DDI functions. Although writing a driver that capitalizes on existing GDI capabilities would be smaller and simpler to write, you should make sure that your driver also implements those operations it can perform more efficiently than GDI.

The display driver graphics DDI functions fall into three groups, each of which is discussed in following topics:

1.  [Graphics DDI functions required by every display driver](required-display-driver-functions.md).

2.  [Graphics DDI functions required under certain conditions](conditionally-required-display-driver-functions.md).

3.  [Graphics DDI functions that are optional](optional-display-driver-functions.md).

 

 





