---
title: Texture Blitting
description: Texture Blitting
ms.assetid: 5a2e49c1-e99d-4b0d-a46c-b22b3dcefaf8
keywords:
- blt WDK Direct3D
- texture management WDK Direct3D , blitting
- blitting WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Texture Blitting


## <span id="ddk_texture_blitting_gg"></span><span id="DDK_TEXTURE_BLITTING_GG"></span>


An important change to the Direct3D DDI, introduced in DirectX 7.0, is that textures are blitted by embedding a token in the [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) command stream. This token is D3DDP2OP\_TEXBLT, and it signals the driver that a texture has to be transferred from a backing surface into local or nonlocal video memory.

Also, instead of the driver being responsible for creating internal handles for textures through the legacy *D3dTextureCreate* and *D3dTextureDestroy* callbacks, the runtime now assigns a handle number to each DirectDrawSurface object that is created within the Direct3D context. The driver is signaled about this handle number through the [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) callback.

*D3dCreateSurfaceEx* is called after every hardware abstraction layer (HAL) [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) call is finished. *D3dCreateSurfaceEx* is also called after every internal hardware emulation layer (HEL) **CreateSurface** call is finished. The HEL call usually occurs when a backing DirectDrawSurface object is created. These calls may occur before and after a Direct3D context is created with [**D3dContextCreate**](https://msdn.microsoft.com/library/windows/hardware/ff542178).

Also, when the application is running, a call is made to [**D3dDestroyDDLocal**](https://msdn.microsoft.com/library/windows/hardware/ff544685) to clean up and destroy any driver data created explicitly for these surfaces. This call is also made before a Direct3D context is created. This is done to ensure that there are no dirty handles associated with any contexts that have not been cleaned up. This is simply a preventative measure that should not actually destroy anything if contexts are properly cleaned up after use.

 

 





