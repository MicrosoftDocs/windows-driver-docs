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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DxApi Miniport Driver Functions For Windows 2000 and Later


## <span id="ddk_dxapi_miniport_driver_functions_for_windows_2000_and_later_gg"></span><span id="DDK_DXAPI_MINIPORT_DRIVER_FUNCTIONS_FOR_WINDOWS_2000_AND_LATER_GG"></span>


Supporting the DxApi interface in a [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md) is only supported with Windows 2000 and later.

DxApi interface support is useful for the following operations:

-   Autoflipping using an IRQ for devices that do not support hardware autoflipping or that have limitations that make it undependable. This allows DirectDraw to always revert to software autoflipping when hardware autoflipping is unavailable.

-   Field skipping using an IRQ to support MPEG drivers that can undo the 3:2 pulldown of MPEG data originally sampled from film.

-   Bus mastering, so devices can continuously transfer data without having to call [*DdLock*](https://msdn.microsoft.com/library/windows/hardware/ff549599) / [*DdUnlock*](https://msdn.microsoft.com/library/windows/hardware/ff550365) for every frame. This is especially useful because the drivers for these devices are WDM drivers.

-   Capturing video and VBI. In the miniport driver, it is easy to capture video that is based on a hardware video port IRQ or graphics IRQ.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DxApi%20Miniport%20Driver%20Functions%20For%20Windows%202000%20and%20Later%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




