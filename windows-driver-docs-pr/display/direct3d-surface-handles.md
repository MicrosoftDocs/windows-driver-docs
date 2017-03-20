---
title: Direct3D Surface Handles
description: Direct3D Surface Handles
ms.assetid: cefede2e-3e82-4de3-ae49-4982578fd2fe
keywords: ["context WDK Direct3D , surface handles", "surface handles WDK Direct3D"]
---

# Direct3D Surface Handles


## <span id="ddk_direct3d_surface_handles_gg"></span><span id="DDK_DIRECT3D_SURFACE_HANDLES_GG"></span>


The Microsoft DirectX 7.0 device driver interface (DDI) is designed to promote a model whereby the Direct3D runtime components parse as little of the command stream as possible before handing the commands to the driver. Additionally, the command stream should be formatted so that it can be used by future hardware.

One important change directed toward these goals is the movement of all surface-related data out of intermediate structures owned by the Direct3D/DirectDraw runtime into structures owned, updated, and formatted by the driver.

Surfaces are referred to by handles embedded in the command stream. In these high-frequency operations, the driver can look up its own representation of a surface from the handle, without resorting to locking a surface via helper functions such as [**EngLockDirectDrawSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564966).

The mechanism for assigning these handles is a driver entry point called [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840). This entry point is called directly after calls to the existing [*DdCanCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549213) and [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) entry points, and after a video memory address and handle have been assigned to a surface. At **D3dCreateSurfaceEx** time, the driver copies all pertinent information out of the DirectDraw runtime's copy of the surface structure and into its own surface structure. Driver-side copies are required for surface data such as size, format, and **fpVidMem** (a member of the [**DD\_SURFACE\_GLOBAL**](https://msdn.microsoft.com/library/windows/hardware/ff551726) structure).

Handles are guaranteed by the runtime to be unique for each device and for each process. Handles are not guaranteed to be unique for each context, and this has some implications for drivers that are discussed in greater detail in [Creating Driver-Side Surface Structures](creating-driver-side-surface-structures.md).

There is no corresponding **DestroySurfaceEx** call, so driver-side surface structures are destroyed at [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) time.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct3D%20Surface%20Handles%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




