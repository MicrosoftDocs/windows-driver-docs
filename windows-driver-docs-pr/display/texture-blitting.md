---
title: Texture Blitting
description: Texture Blitting
keywords:
- blt WDK Direct3D
- texture management WDK Direct3D , blitting
- blitting WDK Direct3D
ms.date: 04/20/2017
---

# Texture Blitting


## <span id="ddk_texture_blitting_gg"></span><span id="DDK_TEXTURE_BLITTING_GG"></span>


An important change to the Direct3D DDI, introduced in DirectX 7.0, is that textures are blitted by embedding a token in the [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) command stream. This token is D3DDP2OP\_TEXBLT, and it signals the driver that a texture has to be transferred from a backing surface into local or nonlocal video memory.

Also, instead of the driver being responsible for creating internal handles for textures through the legacy *D3dTextureCreate* and *D3dTextureDestroy* callbacks, the runtime now assigns a handle number to each DirectDrawSurface object that is created within the Direct3D context. The driver is signaled about this handle number through the [**D3dCreateSurfaceEx**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex) callback.

*D3dCreateSurfaceEx* is called after every hardware abstraction layer (HAL) [*DdCreateSurface*](/previous-versions/windows/hardware/drivers/ff549263(v=vs.85)) call is finished. *D3dCreateSurfaceEx* is also called after every internal hardware emulation layer (HEL) **CreateSurface** call is finished. The HEL call usually occurs when a backing DirectDrawSurface object is created. These calls may occur before and after a Direct3D context is created with [**D3dContextCreate**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_contextcreatecb).

Also, when the application is running, a call is made to [**D3dDestroyDDLocal**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_destroyddlocal) to clean up and destroy any driver data created explicitly for these surfaces. This call is also made before a Direct3D context is created. This is done to ensure that there are no dirty handles associated with any contexts that have not been cleaned up. This is simply a preventative measure that should not actually destroy anything if contexts are properly cleaned up after use.

 

