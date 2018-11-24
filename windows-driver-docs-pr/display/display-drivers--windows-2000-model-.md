---
title: Display Drivers (Windows 2000 Model)
description: Display Drivers (Windows 2000 Model)
ms.assetid: 9d49f4e7-5153-417e-8f15-42b3dcdf3fa6
keywords:
- display driver model WDK Windows 2000 , display drivers
- Windows 2000 display driver model WDK , display drivers
- display drivers WDK Windows 2000
- display drivers WDK Windows 2000 , about display drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Display Drivers (Windows 2000 Model)


## <span id="ddk_display_drivers_windows_2000_model__gg"></span><span id="DDK_DISPLAY_DRIVERS_WINDOWS_2000_MODEL__GG"></span>


Microsoft NT-based operating system display driver writers are concerned with two core software interfaces:

-   Graphics DDI interface--The set of functions that the display driver implements. GDI can call the graphics DDI interface to process graphics commands.

-   GDI interface--System-supplied helper routines called by display drivers to simplify driver implementation.

This section describes key concepts associated with NT-based operating system display drivers as well as some implementation information. See [GDI Support for Graphics Drivers](gdi-support-for-graphics-drivers.md) and [Using the Graphics DDI](using-the-graphics-ddi.md) for graphics driver design details that are common to both printer drivers and display drivers, such as driver initialization and termination, and graphics output.

Display driver writers can also implement the following DDIs:

-   DirectDraw DDI -- Graphics interface that allows vendors to provide hardware accelerations for DirectDraw. See [DirectDraw](directdraw.md) for details.

-   Direct3D DDI -- 3D graphics interface that allows vendors to provide hardware accelerations for Direct3D. See [Direct3D DDI](direct3d.md) for details.

For complete descriptions of the graphics DDI entry points and structures, as well as GDI service functions and objects, see [GDI Functions](https://msdn.microsoft.com/library/windows/hardware/ff566543).

 

 





