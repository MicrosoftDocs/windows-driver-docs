---
title: Render Target Requirements
description: Render Target Requirements
ms.assetid: 4d16819e-f209-44df-b5af-f3ff9cae256b
keywords:
- render targets WDK Direct3D
- color buffers WDK Direct3D
- buffers WDK Direct3D
- depth buffers WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Render Target Requirements


## <span id="ddk_render_target_requirements_gg"></span><span id="DDK_RENDER_TARGET_REQUIREMENTS_GG"></span>


The requirements for color buffers and depth buffers are as follows:

### <span id="color_buffers"></span><span id="COLOR_BUFFERS"></span>Color Buffers

If the hardware does not support a render target that is also to be used as a texture (that is, the device cannot "render to a texture"), the device must fail calls to the **IDirect3DDevice7::SetRenderTarget** and **IDirect3D7::CreateDevice** methods. These methods are described in the Direct3D SDK documentation. The fact that a render target is to be used as a texture is signified by the presence of the DDSCAPS\_TEXTURE flag in the surface description (see the **dwCaps** member of the [**DDSCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff550286) structure).

### <span id="depth_buffers"></span><span id="DEPTH_BUFFERS"></span>Depth Buffers

If the hardware does not support a particular combination of render target and depth-buffers, then the device must fail API calls that cause this scenario when it detects mismatches of this sort, such as in calls to the **IDirect3D7::CreateDevice** and **IDirectDrawSurface7::AddAttachedSurface** methods. These methods are described in the Direct3D and DirectDraw SDK documentation sets, respectively. An example of such a mismatch might be when the render target and depth buffer are of different bit depths. Do not transparently alter the format of either the render target or the depth-buffer to cause an invalid combination to work properly. Instead, allocate a higher-precision depth buffer without informing the DirectX runtime.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Render%20Target%20Requirements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




