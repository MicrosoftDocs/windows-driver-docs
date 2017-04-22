---
title: Display Drivers (Windows 2000 Model)
description: Display Drivers (Windows 2000 Model)
ms.assetid: 9d49f4e7-5153-417e-8f15-42b3dcdf3fa6
keywords:
- display driver model WDK Windows 2000 , display drivers
- Windows 2000 display driver model WDK , display drivers
- display drivers WDK Windows 2000
- display drivers WDK Windows 2000 , about display drivers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Display%20Drivers%20%28Windows%202000%20Model%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




