---
title: Multiplane overlay hardware requirements
ms.assetid: 3BDA8F54-A0D8-4879-A828-89A2E4254179
description: Hardware requirements needed to support multiplane overlays.
---

# Multiplane overlay hardware requirements


Display drivers and hardware are not required to support multiplane overlays. However, to provide multiplane overlay support, the hardware must meet these requirements:

-   Hardware must support non-overlapping planes:
    -   One plane can cover one portion of the screen while another plane can cover a different, mutually exclusive, portion of the screen.
    -   If any portion of the screen is not covered by a plane, the hardware must scan out black for that area. The hardware can assume that there is a virtual plane at the bottom-most *z* order that is filled with black.
-   Hardware must support overlapping planes:
    -   The hardware must be able to enable or disable alpha blending on a per-plane basis. (Alpha blending is a technique where the color in a source bitmap is combined with that in a destination bitmap to produce a new destination bitmap.)
    -   Blending between the planes using pre-multiplied alpha must be supported.
-   When only one output target is active, the active output must support multiplane overlays. In the case of clone mode, where multiple outputs are simultaneously active, hardware should not report that it supports multiplane overlays unless all active outputs support multiplane overlays.
-   The Desktop Window Manager (DWM)â€™s swapchain (plane 0) must be able to interact with the other overlay planes.
-   All planes must be able to be enabled and disabled, including plane 0 (the DWMâ€™s swapchain).
-   All planes must support source and destination clipping, including plane 0 (the DWMâ€™s swapchain).
-   At least one plane must support shrinking and stretching, independent from other planes that might be enabled.
-   Planes that support scaling must support both bilinear filtering and filtering quality that is better than bilinear.
-   At least one plane must support these YUV formats (for more info, see [YUV format ranges in Windows 8.1](yuv-format-ranges.md)):
    -   Both ITU BT.601 and BT.709 YUV to RGB matrix conversion for YUV formats.
    -   Both normal (or studio) range YUV luminance (16 - 235) and extended-range YUV luminance (0 â€“ 255).
-   Hardware must handle these register latching scenarios:
    -   All per-plane attributes (buffer address, clipping, scaling, and so on) must atomically post during the vertical retrace period. When updating a block of registers, they must all post atomically—for example, if the VSync occurs after writing 10 of 20 registers pertaining to the overlay plane, none of them will post until the next VSync because they cannot all post on the current Vsync).
    -   Each plane can be updated independently from the other planes. For example, if the plane 0 registers have been updated prior to the VSync and later the plane 1 registers are updated when the VSync occurs, the plane 1 updates might wait until the next VSync, but the plane 0 updates should occur on time.
    -   When multiple planes are updated during a single present call, the updates should occur atomically. For example, if a single present call is updating plane 0 and enabling plane 1, the plane 0 registers should not post on the VSync unless the plane 1 registers also post on the same VSync.
-   Transformation, scaling, and blending should occur in this order:
    1.  The source allocation is clipped according to the specified source rectangle. The source rectangle is guaranteed to be bounded within the size of the source allocation.
    2.  Apply a horizontal image flip, then a vertical image flip if requested.
    3.  Apply scaling according to the destination rectangle, apply clipping according to the clip rectangle, and apply the appropriate filtering when scaling.
    4.  Blend with allocations at other layers. Blending should be performed from top to bottom (or until an opaque layer is hit) in *z*-order. If alpha blending is requested, hardware must honor the per-pixel-alpha, and color value is pre-multiplied by alpha. The following pseudo code performs a â€œsource over destinationâ€? operation repeatedly from top to bottom, (((Layer\[0\] over Layer\[1\]) over Layer\[2\]) over â€¦ Layer\[n\]). Outside of the destination rectangle, each layer must be treated as transparent (0,0,0,0).

        ``` syntax
        Color = Color[0]; // Layer 0 is topmost.
        Alpha = Color[0].Alpha;
        for (i = 1; Alpha < 1 && i < LayersToBlend; i++)
        {
            Color += ((1 - Alpha) * Color[i]);
            Alpha += ((1 - Alpha) * Color[i].Alpha);
        }
        Output Color;
        ```

        Hardware can blend from bottom to top as long as the output result is the same. In this case, the following blend algorithm should be used:

        ``` syntax
        Color = Color[LayersToBlend-1];  // Bottom-most layer
        Alpha = Color[LayersToBlend-1].Alpha;
        if (LayersToBlend > 1)
        {
            for (i = LayersToBlend - 2; Alpha < 1 && i >= 0; i--)
            {
                Color = Color[i] + ((1 â€“ Color[i].Alpha) * Color;
                Alpha = Color[i].Alpha + (1 â€“ Color[i].Alpha) * Alpha;
            }
        }
        Output Color;
        ```

    5.  Black color must be displayed at the area where not covered by any of destination rectangles from any layers. Hardware can assume that there is a conceptual virtual bottom-most black layer that is the size of the screen.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multiplane%20overlay%20hardware%20requirements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




