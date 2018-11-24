---
title: DVD 704-Wide Non-Pan-Scan Example
description: DVD 704-Wide Non-Pan-Scan Example
ms.assetid: df335e5e-4f7c-440a-88ef-00f6e0f916e2
keywords:
- alpha-blend combination WDK DirectX VA , DVD 704-wide non-pan-scan example
- blended pictures WDK DirectX VA , DVD 704-wide non-pan-scan example
- DVD 704-wide non-pan-scan example WDK DirectX VA
- 704-wide non-pan-scan example WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





