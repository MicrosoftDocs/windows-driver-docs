---
title: Losing Driver-Managed Textures
description: Losing Driver-Managed Textures
ms.assetid: 19f87190-bb3a-40a6-a216-8df9816e2842
keywords:
- drawing surfaces WDK DirectDraw , lost textures
- DirectDraw surfaces WDK Windows 2000 display , lost textures
- surfaces WDK DirectDraw , lost textures
- suspended textures WDK DirectDraw
- textures WDK DirectDraw , lost
- lost textures WDK DirectDraw
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Losing Driver-Managed Textures


## <span id="ddk_losing_driver_managed_textures_gg"></span><span id="DDK_LOSING_DRIVER_MANAGED_TEXTURES_GG"></span>


Driver-managed texture surfaces, which consume video memory, need the ability to be placed in a suspended state (lost). Because the driver controls the allocation of video memory for driver-managed texture surfaces, a method notifies the driver when such texture surfaces need to be lost through an extension to the [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) call.

When a driver-managed texture surface (marked with the DDSCAPS2\_TEXTUREMANAGE flag) is lost, the driver receives a special *DdDestroySurface* call with DDRAWISURF\_INVALID specified in the **dwFlags** member of the texture surface structure. The driver should free video memory associated with the managed texture surface, but should not free any other private surface information including the backing (system memory) image of the video memory copy of the surface. There will be no new [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) call to restore the lost driver-managed texture surfaces because they are not really lost from the driver's point of view. For the most part, this special *DdDestroySurface* call is used to inform the driver that it should evict its video memory copy.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Losing%20Driver-Managed%20Textures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




