---
title: Graphics DDI Functions for Display Drivers
description: Graphics DDI Functions for Display Drivers
ms.assetid: 9edd06bd-7aac-4015-864d-b08f3e3a79fd
keywords: ["display drivers WDK Windows 2000 , graphics", "graphics DDI functions WDK Windows 2000 display"]
---

# Graphics DDI Functions for Display Drivers


## <span id="ddk_graphics_ddi_functions_for_display_drivers_gg"></span><span id="DDK_GRAPHICS_DDI_FUNCTIONS_FOR_DISPLAY_DRIVERS_GG"></span>


A Microsoft NT-based operating system display driver must implement several graphics DDI functions. Although writing a driver that capitalizes on existing GDI capabilities would be smaller and simpler to write, you should make sure that your driver also implements those operations it can perform more efficiently than GDI.

The display driver graphics DDI functions fall into three groups, each of which is discussed in following topics:

1.  [Graphics DDI functions required by every display driver](required-display-driver-functions.md).

2.  [Graphics DDI functions required under certain conditions](conditionally-required-display-driver-functions.md).

3.  [Graphics DDI functions that are optional](optional-display-driver-functions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Graphics%20DDI%20Functions%20for%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




