---
title: First Steps For DirectDraw Drivers
description: First Steps For DirectDraw Drivers
ms.assetid: 0bb00060-7887-447f-a3c9-394ae5ac84db
keywords:
- drawing WDK DirectDraw , DirectDraw driver
- DirectDraw WDK Windows 2000 display , DirectDraw driver
- DirectDraw driver WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# First Steps For DirectDraw Drivers


## <span id="ddk_first_steps_for_directdraw_drivers_gg"></span><span id="DDK_FIRST_STEPS_FOR_DIRECTDRAW_DRIVERS_GG"></span>


A good way to begin implementing DirectDraw functionality is to modify an existing driver. If no driver is available, start with the sample code in the DirectDraw portion of the Windows Driver Kit (WDK) and get driver initialization, lock, and flip working. From that base functionality, more powerful functionality can be added that will improve display performance.

The minimum driver functionality DirectDraw requires is the ability to lock, unlock, and flip a surface. Assuming the hardware supports the related operations, driver support should also be added for blts (including transparent blts, which are important for speed in games), stretching, and overlays, which are critical for video playback.

 

 





