---
title: DVD 704-Wide Non-Pan-Scan Example
description: DVD 704-Wide Non-Pan-Scan Example
ms.assetid: df335e5e-4f7c-440a-88ef-00f6e0f916e2
keywords: ["alpha-blend combination WDK DirectX VA , DVD 704-wide non-pan-scan example", "blended pictures WDK DirectX VA , DVD 704-wide non-pan-scan example", "DVD 704-wide non-pan-scan example WDK DirectX VA", "704-wide non-pan-scan example WDK DirectX VA"]
---

# DVD 704-Wide Non-Pan-Scan Example


## <span id="ddk_dvd_704_wide_non_pan_scan_example_gg"></span><span id="DDK_DVD_704_WIDE_NON_PAN_SCAN_EXAMPLE_GG"></span>


The use of MPEG-2 on DVD for 704-wide pictures requires a source rectangle that exceeds the boundaries of the decoded picture (if using the method described in [MPEG-2 Pan-Scan Example](mpeg-2-pan-scan-example.md)). In this case, the DVD specifies a *display\_horizontal\_size* of 720 that exceeds the decoded picture's *horizontal\_size* of 704. When the source rectangle exceeds the boundaries of the decoded picture, the host software decoder is responsible for cropping the source rectangle to keep it from reaching outside the allocated source area and for managing the destination rectangle to adjust for the cropping.

The source rectangle is defined by the **PictureSourceRect16thPel** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure (in one-sixteenth of a luminance sample spacing resolution) with the following values:

-   **left** = 0

-   **right** = 16 X (**left** + *horizontal\_size*) = 11264

The picture destination rectangle is defined by the **PictureDestinationRect** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure (in one-sixteenth of a luminance sample spacing resolution) by one of the following two alternatives:

1.  A rectangle with the following values:
    -   **left** = (*display\_horizontal\_size* âˆ’ *horizontal\_size*) / 2 = 8
    -   **right** = **left** + *horizontal\_size* = 712

2.  A rectangle with the following values:
    -   **left** = 0
    -   **right** = **left** + *horizontal\_size* = 704

In the second case, the rectangle indicated by the **GraphicDestinationRect** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure is displaced to the left by eight samples to compensate for the shifted picture destination.

The second of these two alternatives creates only the destination area that is used for the display.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DVD%20704-Wide%20Non-Pan-Scan%20Example%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




