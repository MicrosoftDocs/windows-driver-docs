---
title: Optional Features for Multiple Render Targets
description: Optional Features for Multiple Render Targets
ms.assetid: 265df4d3-acc9-4978-97d1-a6f81bc7afaf
keywords:
- rendering multiple targets WDK DirectX 9.0 , optional features
- multiple render targets WDK DirectX 9.0 , optional features
- simultaneous render targets WDK DirectX 9.0 , optional features
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Optional Features for Multiple Render Targets


## <span id="ddk_optional_features_for_multiple_render_targets_gg"></span><span id="DDK_OPTIONAL_FEATURES_FOR_MULTIPLE_RENDER_TARGETS_GG"></span>


A DirectX 9.0 version driver that supports rendering to multiple targets simultaneously can support extended features. If the driver supports these extended features, it must indicate such support by reporting capability bits in the **PrimitiveMiscCaps** member of the D3DCAPS9 structure. The driver can support the following extended features:

-   Setting independent bit depths for render targets in a multiple render target group. The render targets can have different formats; however, unless this feature is supported, the render targets must have identical bit depths. The D3DPMISCCAPS\_MRTINDEPENDENTBITDEPTHS capability bit must be set to indicate support for independent bit depths.

-   Performing operations--other than the z and stencil test--on render targets in a multiple render target group after pixel shader operations. For example, unless this feature is supported, the driver cannot dither, alpha test, apply fog, blend, or perform raster operations after pixel shader operations. The D3DPMISCCAPS\_MRTPOSTPIXELSHADERBLENDING capability bit must be set to indicate support for postpixel-shader operations.

    If D3DPMISCCAPS\_MRTPOSTPIXELSHADERBLENDING is set, the display device must apply the following states to all render targets that are simultaneously rendered:

    -   Alpha blend. Set oCi to cause the color value to blend with the ith render target.
    -   Alpha test. Set oC0 for a comparison to occur; if the comparison fails, the pixel is canceled for all render targets.
    -   Fog. Apply fog to render target 0; other render targets are undefined. The driver can apply fog to all render targets using the same state.
    -   Dither. Undefined.
-   Applying independent color-write masks (D3DRS\_COLORWRITEENABLE) for render targets in a multiple render target group. The D3DPMISCCAPS\_INDEPENDENTWRITEMASKS capability bit must be set to indicate support for independent color-write masks. If D3DPMISCCAPS\_INDEPENDENTWRITEMASKS is set, the available number of independent color-write masks is equal to the maximum number of render targets in a multiple render target group (the **NumSimultaneousRTs** member of the D3DCAPS9 structure).

Note that a driver for a display device that supports pixel shader version 3.0 and later must indicate that it supports the extended features for multiple render targets. For more information, see [Reporting Capabilities for Shader 3 Support](reporting-capabilities-for-shader-3-support.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Optional%20Features%20for%20Multiple%20Render%20Targets%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




