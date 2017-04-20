---
title: Lost Surfaces, Surface Handles, and Contexts
description: Lost Surfaces, Surface Handles, and Contexts
ms.assetid: d2458077-56f8-481b-b612-a706e9560314
keywords:
- context WDK Direct3D , D3dCreateSurfaceEx
- D3dCreateSurfaceEx
- surface handles WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Lost Surfaces, Surface Handles, and Contexts


## <span id="ddk_lost_surfaces_surface_handles_and_contexts_gg"></span><span id="DDK_LOST_SURFACES_SURFACE_HANDLES_AND_CONTEXTS_GG"></span>


Some surfaces should be referred to in a context (such as the render target, Z-buffer, or a texture), typically by storing the handles for those surfaces in the driver's context. These surfaces may become lost (destroyed) as far as the driver is concerned. The context itself may survive, but may now have stale (invalid) handles to lost surfaces. The runtime guarantees that no rendering commands are passed to the context while it is in this state, but there is still the problem of how to reassociate the context with restored surfaces before rendering can begin again. The runtime guarantees that the handles for lost surfaces do not change. This in turn guarantees that if a context keeps handles to its surfaces (render target, Z, and textures), then these surfaces are always recreated (restored) *with the same handle values* before rendering can resume on this context.

Some driver writers may wish to optimize the state of a context by storing surface data directly in the context, rather than doing the work of dereferencing the handles on every [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) call. Because the cost of this dereference is likely to be small compared to the cost of executing a batch of *D3dDrawPrimitives2* tokens, this optimization is not encouraged. However, if driver writers wish to do so, then they must be aware that surfaces may move when they are restored. This means that while the handle may be the same, there is no guarantee that a surface is restored with the same **fpVidMem** (a member of the [**DD\_SURFACE\_GLOBAL**](https://msdn.microsoft.com/library/windows/hardware/ff551726) structure) pointer with which it was created. Contexts that are optimized in this way may end up with stale video memory pointers, and have no information that the surface has moved. One method to deal with this is that the driver may tag any surface when it is associated with a context (as render target, Z-buffer, or texture). Then at [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) time, it can search for any context that refers to this surface and then update that context.

It is not recommended that a surface keep a pointer to a context, because one surface may be associated with more than one context.

The concept of *lost* surfaces was introduced in the DirectDraw SDK documentation. Lost surfaces have some implications in the DirectX 7.0 DDI model. For more information, see [Losing and Restoring DirectDraw Surfaces](losing-and-restoring-directdraw-surfaces.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Lost%20Surfaces,%20Surface%20Handles,%20and%20Contexts%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




