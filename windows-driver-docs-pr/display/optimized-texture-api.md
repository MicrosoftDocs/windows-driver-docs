---
title: Optimized Texture API
description: Optimized Texture API
ms.assetid: 58d42807-3f52-415e-a06a-2ed408c20fb0
keywords:
- texture management WDK Direct3D , optimized textures
- optimized textures WDK Direct3D
- CAPS2_HINTDYNAMIC
- DDSCAPS2_HINTSTATIC
- DDSCAPS2_OPAQUE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Optimized Texture API


## <span id="ddk_optimized_texture_api_gg"></span><span id="DDK_OPTIMIZED_TEXTURE_API_GG"></span>


Three new capabilities indicate the level of optimization that can be applied to a DirectDrawSurface object. In DirectX 6.0 and beyond, only textures can be marked with these caps bits. The optimized surface paradigm may be extended in the future to cover other types of surfaces, although the semantics may not be the same as for textures.

To address these issues, three new flags are provided in the **DirectDrawSurface7:: Create** method. When none of these three flags is specified, the decision whether to patch or swizzle is left up to the driver. These flags are as follows:

<span id="DDSCAPS2_HINTDYNAMIC"></span><span id="ddscaps2_hintdynamic"></span>DDSCAPS2\_HINTDYNAMIC  
Indicates to the driver that this surface is locked frequently, (for example, once per frame) for uses such as with streaming video or procedural textures. This cap should work for *all* driver-enumerated texture surface formats. The driver should avoid any transformation for these textures, especially if it requires some overhead.

<span id="DDSCAPS2_HINTSTATIC"></span><span id="ddscaps2_hintstatic"></span>DDSCAPS2\_HINTSTATIC  
This indicates to the driver that the surface can be reordered/retiled/swizzled in the **IDirect3DDevice7::Load** and **IDirectDrawSurface7::Blt** methods (described in the Direct3D SDK and DirectDraw SDK documentation, respectively). This operation does not change the size of the texture. It is relatively fast, and symmetrical, because the application may still lock these bits (although it takes a performance hit when doing so). Drivers are not allowed to fail locks on these surfaces and therefore cannot use lossy compression techniques. MIP map surfaces can be interleaved in this case.

This cap is not intended to force swizzling under any circumstances, especially those in which no performance benefit arises. Some texel formats may silently fail to swizzle.

<span id="DDSCAPS2_OPAQUE"></span><span id="ddscaps2_opaque"></span>DDSCAPS2\_OPAQUE  
This indicates to the driver that this surface will not be accessed by the application again. This flag behaves like the DDSCAPS2\_HINTSTATIC flag, but with the addition of allowing actual compression using a hardware-specific compression scheme. This operation is relatively slow, but should allow simple, symmetric compression schemes (such as YUV 4:2:0, or color cell compression) to be used, providing compression ratios from 2 to 6x. Asymmetric schemes such as VQ should not be used here because they result in unacceptable benchmarks.

MIP map textures can be interleaved arbitrarily by the driver. This technique should probably only be requested outside of internal rendering loops such as when textures are loaded from disk. Heap size reports after such a texture is loaded reflect the reduced memory consumption if compression was applied. There is additional header overhead on textures and therefore compressing many small textures does not save as much memory as might be expected.

In general, there is no guarantee about texture compression ratio, or compression quality implied by this flag.

Surfaces created with this flag fail in the following cases:

Calls to the **IDirectDrawSurface7::Lock** method.

Calls to the **IDirectDrawSurface7::GetDC** method.

Subrectangle blts to such surfaces.

All blts from such surfaces.

The only way to put data into such surfaces is with the **IDirect3DDevice7::Load** method (described in the Direct3D SDK documentation), or a full surface blt call. For more information about **IDirectDrawSurface7::Lock** and **IDirectDrawSurface7::GetDC**, see the DirectDraw SDK documentation.

 

 





