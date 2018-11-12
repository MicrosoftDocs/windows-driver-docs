---
title: Render Target Requirements
description: Render Target Requirements
ms.assetid: 4d16819e-f209-44df-b5af-f3ff9cae256b
keywords:
- render targets WDK Direct3D
- color buffers WDK Direct3D
- buffers WDK Direct3D
- depth buffers WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Render Target Requirements


## <span id="ddk_render_target_requirements_gg"></span><span id="DDK_RENDER_TARGET_REQUIREMENTS_GG"></span>


The requirements for color buffers and depth buffers are as follows:

### <span id="color_buffers"></span><span id="COLOR_BUFFERS"></span>Color Buffers

If the hardware does not support a render target that is also to be used as a texture (that is, the device cannot "render to a texture"), the device must fail calls to the **IDirect3DDevice7::SetRenderTarget** and **IDirect3D7::CreateDevice** methods. These methods are described in the Direct3D SDK documentation. The fact that a render target is to be used as a texture is signified by the presence of the DDSCAPS\_TEXTURE flag in the surface description (see the **dwCaps** member of the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure).

### <span id="depth_buffers"></span><span id="DEPTH_BUFFERS"></span>Depth Buffers

If the hardware does not support a particular combination of render target and depth-buffers, then the device must fail API calls that cause this scenario when it detects mismatches of this sort, such as in calls to the **IDirect3D7::CreateDevice** and **IDirectDrawSurface7::AddAttachedSurface** methods. These methods are described in the Direct3D and DirectDraw SDK documentation sets, respectively. An example of such a mismatch might be when the render target and depth buffer are of different bit depths. Do not transparently alter the format of either the render target or the depth-buffer to cause an invalid combination to work properly. Instead, allocate a higher-precision depth buffer without informing the DirectX runtime.

 

 





