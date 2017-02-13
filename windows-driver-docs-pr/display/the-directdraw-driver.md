---
title: The DirectDraw Driver
description: The DirectDraw Driver
ms.assetid: 6f3343d6-9544-4389-a753-f4520f21a65c
keywords: ["drawing WDK DirectDraw , DirectDraw driver", "DirectDraw WDK Windows 2000 display , DirectDraw driver", "DirectDraw driver WDK Windows 2000 display"]
---

# The DirectDraw Driver


## <span id="ddk_the_directdraw_driver_gg"></span><span id="DDK_THE_DIRECTDRAW_DRIVER_GG"></span>


DirectDraw provides device independence through the DirectDraw driver. The DirectDraw driver is a device-specific interface usually provided by the display hardware manufacturer. DirectDraw exposes methods to the application and uses the DirectDraw portion of the display driver to work directly with the hardware. Applications never call the display driver directly.

Under Windows 2000 and later, the DirectDraw driver is always implemented as 32-bit code. The DirectDraw driver can be part of the display driver or a separate DLL that communicates with the display driver through a private interface defined by the driver writer. The DirectDraw documentation assumes that under Windows 2000 and later, the DirectDraw driver is part of the display driver.

The DirectDraw driver contains only device-dependent code and performs no emulation. If a function is not performed by the hardware, the DirectDraw driver does not report it as a hardware capability. Additionally, the DirectDraw driver does not validate parameters because the DirectDraw runtime does this before the driver is invoked.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20The%20DirectDraw%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




