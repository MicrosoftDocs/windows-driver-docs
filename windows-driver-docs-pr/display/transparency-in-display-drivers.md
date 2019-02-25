---
title: Transparency in Display Drivers
description: Transparency in Display Drivers
ms.assetid: 566706fb-66bd-44f5-b98c-23ed60e27970
keywords:
- display drivers WDK Windows 2000 , transparency
- transparency WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Transparency in Display Drivers


## <span id="ddk_transparency_in_display_drivers_gg"></span><span id="DDK_TRANSPARENCY_IN_DISPLAY_DRIVERS_GG"></span>


If the display hardware supports transparency, the display driver should implement [**DrvTransparentBlt**](https://msdn.microsoft.com/library/windows/hardware/ff557283).

To reduce the cost of reading from video memory, drivers should implement this function when both the source and destination surfaces are in video memory. Drivers should let GDI process transparent bit-block transfers from system memory to video memory, and let GDI handle stretched bit-block transfers as well.

 

 





