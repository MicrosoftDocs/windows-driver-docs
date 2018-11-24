---
title: The DirectDraw Driver
description: The DirectDraw Driver
ms.assetid: 6f3343d6-9544-4389-a753-f4520f21a65c
keywords:
- drawing WDK DirectDraw , DirectDraw driver
- DirectDraw WDK Windows 2000 display , DirectDraw driver
- DirectDraw driver WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The DirectDraw Driver


## <span id="ddk_the_directdraw_driver_gg"></span><span id="DDK_THE_DIRECTDRAW_DRIVER_GG"></span>


DirectDraw provides device independence through the DirectDraw driver. The DirectDraw driver is a device-specific interface usually provided by the display hardware manufacturer. DirectDraw exposes methods to the application and uses the DirectDraw portion of the display driver to work directly with the hardware. Applications never call the display driver directly.

Under Windows 2000 and later, the DirectDraw driver is always implemented as 32-bit code. The DirectDraw driver can be part of the display driver or a separate DLL that communicates with the display driver through a private interface defined by the driver writer. The DirectDraw documentation assumes that under Windows 2000 and later, the DirectDraw driver is part of the display driver.

The DirectDraw driver contains only device-dependent code and performs no emulation. If a function is not performed by the hardware, the DirectDraw driver does not report it as a hardware capability. Additionally, the DirectDraw driver does not validate parameters because the DirectDraw runtime does this before the driver is invoked.

 

 





