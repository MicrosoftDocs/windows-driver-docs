---
title: Special Effects in Display Drivers
description: Special Effects in Display Drivers
ms.assetid: f44a89df-6412-442c-8491-3e2f2bbd826f
keywords:
- display drivers WDK Windows 2000 , special effects
- special effects WDK Windows 2000 display
- effects WDK Windows 2000 display
- blend-in animations WDK Windows 2000 display
- blend-out animations WDK Windows 2000 display
- alpha cursors WDK Windows 2000 display
- gradient fills WDK Windows 2000 display
- alpha blending WDK Windows 2000 display
- bit-block transfers WDK Windows 2000 display
- stretching WDK Windows 2000 display
- animations WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Special Effects in Display Drivers


## <span id="ddk_special_effects_in_display_drivers_gg"></span><span id="DDK_SPECIAL_EFFECTS_IN_DISPLAY_DRIVERS_GG"></span>


Windows 2000 and later operating system versions support the following special effects:

-   If the display hardware supports alpha blending, the display driver can implement [**DrvAlphaBlend**](https://msdn.microsoft.com/library/windows/hardware/ff556176).

-   If the display hardware supports gradient fills, the display driver should implement [**DrvGradientFill**](https://msdn.microsoft.com/library/windows/hardware/ff556236).

### <span id="Alpha_Blending"></span><span id="alpha_blending"></span><span id="ALPHA_BLENDING"></span>Alpha Blending

The Microsoft Windows 2000 (and later) Shell uses alpha blending extensively to perform operations such as *blend-in* and *blend-out animations* and *alpha cursors*. Because alpha blend operations require reading from both the source and destination surfaces, it is very slow to punt to GDI when either the source or destination is in video memory. Consequently, hardware accelerations in the driver will yield visibly smoother animations and improve overall system performance.

Drivers should implement [**DrvAlphaBlend**](https://msdn.microsoft.com/library/windows/hardware/ff556176) for *bit-block transfers* from compatible bitmaps using a constant alpha, and from 32 bpp BGRA system-memory surfaces with per-pixel alpha values. *DrvAlphaBlend* can be implemented using [*triangle texture fills*](https://msdn.microsoft.com/library/windows/hardware/ff556341#wdkgloss-triangle-texture-fill), provided that no seam is ever visible.

The worst-case error produced by *DrvAlphaBlend* should not exceed one (1) per color channel. When stretching is involved, the source should be COLORONCOLOR-stretched (see the Windows SDK documentation) prior to blending; the worst-case error should not exceed one (1) per color channel combined with the worst-case stretching error.

In cases where alpha blending is combined with stretching, there are tests in the WDK that evaluate a display driver's implementation of *DrvAlphaBlend* in the following way:

1.  The test calls the display driver's *DrvAlphaBlend*, producing an alpha-blended and stretched rectangle.

2.  The test generates a destination rectangle, using the same source rectangle as was used in the call to *DrvAlphaBlend*.

3.  For each pixel P in the destination rectangle of step 2, the test simulates a reverse stretch to determine the corresponding pixel in the source rectangle, before stretching. The test applies a tolerance value to the reverse stretch to accommodate the varying stretch implementations by drivers. The test then calculates the alpha blend that should be applied to that pixel.

    Because any of four possible pixels (the corners of the 3 X 3 pixel square centered on pixel P) in the source rectangle could be stretched to produce pixel P in the destination rectangle, the test must compare the color value of each corner pixel with that of the pixel at the corresponding position in the rectangle produced by *DrvAlphaBlend*.

The worst-case stretching error is the largest difference in color value between any pair of corresponding corner pixels, where one of them is on the *DrvAlphaBlend*-produced rectangle, and the other is on the test-produced source rectangle.

### <span id="Gradient_Fills"></span><span id="gradient_fills"></span><span id="GRADIENT_FILLS"></span>Gradient Fills

The Windows 2000 (and later) Shell uses *gradient fills* on all caption bars.

The results produced by [**DrvGradientFill**](https://msdn.microsoft.com/library/windows/hardware/ff556236) depend on the number of bits per pixel, and must satisfy the following guidelines:

### <span id="_24_bpp_or_32_bpp_surfaces"></span><span id="_24_BPP_OR_32_BPP_SURFACES"></span>24-bpp or 32-bpp surfaces

-   Values must increase or decrease monotonically in all gradated directions.

-   For rectangular gradients:
    When *ulMode* == GRADIENT\_FILL\_RECT\_H, each vertical bar must be a single color.
    When *ulMode* == GRADIENT\_FILL\_RECT\_V, each horizontal bar must be a single color.
-   The worst-case error in any channel cannot exceed Â±1.

-   The endpoints of the region must be exact matches.

### <span id="_15_bpp_or_16_bpp_surfaces"></span><span id="_15_BPP_OR_16_BPP_SURFACES"></span>15-bpp or 16-bpp surfaces

The worst-case error in any channel cannot exceed Â±15.

### <span id="_1_bpp_to_8_bpp_surfaces"></span><span id="_1_BPP_TO_8_BPP_SURFACES"></span>1-bpp to 8-bpp surfaces

No error is permitted in gradient fills for any of these surfaces. For an 8-bpp surface, GDI does not call the driver's *DrvGradientFill* function.

Note that in all surfaces, clipping does not affect results.

 

 





