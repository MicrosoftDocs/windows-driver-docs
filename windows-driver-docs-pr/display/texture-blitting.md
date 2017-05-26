---
title: Texture Blitting
description: Texture Blitting
ms.assetid: 5a2e49c1-e99d-4b0d-a46c-b22b3dcefaf8
keywords:
- blt WDK Direct3D
- texture management WDK Direct3D , blitting
- blitting WDK Direct3D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Texture Blitting


## <span id="ddk_texture_blitting_gg"></span><span id="DDK_TEXTURE_BLITTING_GG"></span>


An important change to the Direct3D DDI, introduced in DirectX 7.0, is that textures are blitted by embedding a token in the [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) command stream. This token is D3DDP2OP\_TEXBLT, and it signals the driver that a texture has to be transferred from a backing surface into local or nonlocal video memory.

Also, instead of the driver being responsible for creating internal handles for textures through the legacy *D3dTextureCreate* and *D3dTextureDestroy* callbacks, the runtime now assigns a handle number to each DirectDrawSurface object that is created within the Direct3D context. The driver is signaled about this handle number through the [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) callback.

*D3dCreateSurfaceEx* is called after every hardware abstraction layer (HAL) [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) call is finished. *D3dCreateSurfaceEx* is also called after every internal hardware emulation layer (HEL) **CreateSurface** call is finished. The HEL call usually occurs when a backing DirectDrawSurface object is created. These calls may occur before and after a Direct3D context is created with [**D3dContextCreate**](https://msdn.microsoft.com/library/windows/hardware/ff542178).

Also, when the application is running, a call is made to [**D3dDestroyDDLocal**](https://msdn.microsoft.com/library/windows/hardware/ff544685) to clean up and destroy any driver data created explicitly for these surfaces. This call is also made before a Direct3D context is created. This is done to ensure that there are no dirty handles associated with any contexts that have not been cleaned up. This is simply a preventative measure that should not actually destroy anything if contexts are properly cleaned up after use.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Texture%20Blitting%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




