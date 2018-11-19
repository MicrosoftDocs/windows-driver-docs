---
title: Windows 8 in-box graphics driver preferred
description: In this scenario, Windows 8 in-box graphics driver are preferred over Windows 7 or older graphics drivers.
ms.assetid: 77B6F0A3-F8CE-473F-AF17-4C08237DC33C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="display.windows_8_in-box_graphics_driver_preferred_"></span>Windows 8 in-box graphics driver preferred


In this scenario, Windows 8 in-box graphics driver are preferred over Windows 7 or older graphics drivers.

In a Windows 8 upgrade installation, if the graphics hardware is covered by a Windows 8 in-box driver, the graphics drivers from the previous Windows version is not migrated to Windows 8. This is true even when the older graphics driver is a 4-part match (graphics hardware + pc model specific), and the Windows 8 in-box graphics driver is only a 2-part match (graphics hardware specific only). This is because the Windows 8 in-box driver has a better feature score than any driver in-box or Logo'ed for a previous Windows release. To understand the driver selection criteria, see [Driver matching criteria](driver-matching-criteria.md). If a Windows 8 certified driver was installed on Windows 7 before the Windows 8 upgrade installation, that driver will migrate.

**Note**  
A Windows 7 in-box graphics driver will never migrate to Windows 8, even if there is no Windows 8 in-box coverage for the graphics hardware. In this case, Windows 8 uses the Microsoft Basic Display Driver (MSBDD).

 

 

 





