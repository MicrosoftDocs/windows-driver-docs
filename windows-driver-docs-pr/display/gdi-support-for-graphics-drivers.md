---
title: GDI Support for Graphics Drivers
description: GDI Support for Graphics Drivers
ms.assetid: ef42cda0-106f-4c1b-babc-29a1070e2a2f
keywords: ["GDI WDK Windows 2000 display , reference", "graphics drivers WDK Windows 2000 display , reference", "drawing WDK GDI , reference"]
---

# GDI Support for Graphics Drivers


## <span id="ddk_gdi_support_for_graphics_drivers_gg"></span><span id="DDK_GDI_SUPPORT_FOR_GRAPHICS_DRIVERS_GG"></span>


This section describes the Microsoft Windows NT-based operating system graphics device interface (GDI). It then details the support that GDI provides to graphics drivers.

References to GDI in this section are implicit references to kernel-mode GDI; Microsoft Win32 GDI will be explicitly identified. Kernel-mode GDI is also known as the Graphics Engine.

GDI function and structure references are documented in the [Display Devices Reference](https://msdn.microsoft.com/library/windows/hardware/ff554046) section. Most of the GDI function declarations and structure definitions can be found in *Winddi.h*. For display drivers, the Microsoft DirectDraw heap manager functions are declared in *Dmemmgr.h*. Both files are shipped with the Windows Driver Kit (WDK).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Support%20for%20Graphics%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




