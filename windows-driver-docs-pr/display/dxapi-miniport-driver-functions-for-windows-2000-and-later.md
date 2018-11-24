---
title: DxApi Miniport Driver Functions For Windows 2000 and Later
description: DxApi Miniport Driver Functions For Windows 2000 and Later
ms.assetid: e9a41e27-930c-49a2-b5e3-0b709b873bb3
keywords:
- DxApi miniport drivers WDK DirectDraw
- DxApi miniport drivers WDK DirectDraw , about DxApi miniport drivers
- autoflipping WDK DirectDraw
- field skipping WDK DirectDraw
- bus mastering WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DxApi Miniport Driver Functions For Windows 2000 and Later


## <span id="ddk_dxapi_miniport_driver_functions_for_windows_2000_and_later_gg"></span><span id="DDK_DXAPI_MINIPORT_DRIVER_FUNCTIONS_FOR_WINDOWS_2000_AND_LATER_GG"></span>


Supporting the DxApi interface in a [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md) is only supported with Windows 2000 and later.

DxApi interface support is useful for the following operations:

-   Autoflipping using an IRQ for devices that do not support hardware autoflipping or that have limitations that make it undependable. This allows DirectDraw to always revert to software autoflipping when hardware autoflipping is unavailable.

-   Field skipping using an IRQ to support MPEG drivers that can undo the 3:2 pulldown of MPEG data originally sampled from film.

-   Bus mastering, so devices can continuously transfer data without having to call [*DdLock*](https://msdn.microsoft.com/library/windows/hardware/ff549599) / [*DdUnlock*](https://msdn.microsoft.com/library/windows/hardware/ff550365) for every frame. This is especially useful because the drivers for these devices are WDM drivers.

-   Capturing video and VBI. In the miniport driver, it is easy to capture video that is based on a hardware video port IRQ or graphics IRQ.

 

 





