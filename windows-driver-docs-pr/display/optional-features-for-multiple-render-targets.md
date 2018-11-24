---
title: Optional Features for Multiple Render Targets
description: Optional Features for Multiple Render Targets
ms.assetid: 265df4d3-acc9-4978-97d1-a6f81bc7afaf
keywords:
- rendering multiple targets WDK DirectX 9.0 , optional features
- multiple render targets WDK DirectX 9.0 , optional features
- simultaneous render targets WDK DirectX 9.0 , optional features
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





