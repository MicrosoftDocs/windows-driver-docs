---
title: Losing Driver-Managed Textures
description: Losing Driver-Managed Textures
keywords:
- drawing surfaces WDK DirectDraw , lost textures
- DirectDraw surfaces WDK Windows 2000 display , lost textures
- surfaces WDK DirectDraw , lost textures
- suspended textures WDK DirectDraw
- textures WDK DirectDraw , lost
- lost textures WDK DirectDraw
ms.date: 04/20/2017
---

# Losing Driver-Managed Textures


## <span id="ddk_losing_driver_managed_textures_gg"></span><span id="DDK_LOSING_DRIVER_MANAGED_TEXTURES_GG"></span>


Driver-managed texture surfaces, which consume video memory, need the ability to be placed in a suspended state (lost). Because the driver controls the allocation of video memory for driver-managed texture surfaces, a method notifies the driver when such texture surfaces need to be lost through an extension to the [*DdDestroySurface*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_destroysurface) call.

When a driver-managed texture surface (marked with the DDSCAPS2\_TEXTUREMANAGE flag) is lost, the driver receives a special *DdDestroySurface* call with DDRAWISURF\_INVALID specified in the **dwFlags** member of the texture surface structure. The driver should free video memory associated with the managed texture surface, but should not free any other private surface information including the backing (system memory) image of the video memory copy of the surface. There will be no new [*DdCreateSurface*](/previous-versions/windows/hardware/drivers/ff549263(v=vs.85)) call to restore the lost driver-managed texture surfaces because they are not really lost from the driver's point of view. For the most part, this special *DdDestroySurface* call is used to inform the driver that it should evict its video memory copy.

 

