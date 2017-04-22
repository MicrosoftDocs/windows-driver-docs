---
title: Losing and Restoring DirectDraw Surfaces
description: Losing and Restoring DirectDraw Surfaces
ms.assetid: 74203932-8a30-44ea-8d0d-45265dd2e74a
keywords:
- drawing surfaces WDK DirectDraw , losing
- DirectDraw surfaces WDK Windows 2000 display , losing
- surfaces WDK DirectDraw , losing
- drawing surfaces WDK DirectDraw , restoring
- DirectDraw surfaces WDK Windows 2000 display , restoring
- surfaces WDK DirectDraw , restoring
- restoring surfaces WDK DirectDraw
- lost surfaces WDK DirectDraw
- suspended surfaces WDK DirectDraw
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Losing and Restoring DirectDraw Surfaces


## <span id="ddk_losing_and_restoring_directdraw_surfaces_gg"></span><span id="DDK_LOSING_AND_RESTORING_DIRECTDRAW_SURFACES_GG"></span>


Surface object lifetimes are longer for the runtime's surface objects than they are for the driver's surface objects. In a few situations, most notably mode changes, surfaces become *lost*. This means that the driver's surface object is destroyed when [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) is called, but the runtime's surface object is placed into a suspended state. Later, the runtime object can be *restored*, which corresponds to a [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) call at the driver level.

Normally, drivers do not have to be aware of this intermediate lost state. However, there are some cases where an understanding of this process will help the driver writer.

Driver writers can elect to handle complex surface restoration in one atomic call. At surface restoration time, the DirectDraw runtime examines the driver's [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) entry point. If this entry point is defined, then the DirectDraw runtime restores all complex surfaces in one call to [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263). The driver probably will not be able to differentiate between the original creation and the creation caused by restoring a surface.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Losing%20and%20Restoring%20DirectDraw%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




