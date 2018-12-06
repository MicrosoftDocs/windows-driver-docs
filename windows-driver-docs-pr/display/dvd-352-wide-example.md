---
title: DVD 352-Wide Example
description: DVD 352-Wide Example
ms.assetid: 22047c8e-30e3-4204-9f7d-b8b97be668ae
keywords:
- alpha-blend combination WDK DirectX VA , DVD 352-wide example
- blended pictures WDK DirectX VA , DVD 352-wide example
- DVD 352-wide example WDK DirectX VA
- 352-wide example WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DVD 352-Wide Example


## <span id="ddk_dvd_352_wide_example_gg"></span><span id="DDK_DVD_352_WIDE_EXAMPLE_GG"></span>


DVD can use 352-wide pictures, which can be stretched to a width of 704 by use of the **PictureSourceRect16thPel** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure (in one-sixteenth of a luminance sample spacing resolution).

The **PictureSourceRect16thPel** member defines a source rectangle with the following values:

-   **left** = 0

-   **right** = 16 X (**left** + *horizontal\_size*) = 5632

The **PictureDestinationRect** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure defines two alternative destination rectangles with the following values:

1.  A destination rectangle with the following values:
    -   **left** = 8
    -   **right** = **left** + (2 X *horizontal\_size*) = 712

2.  A destination rectangle with the following values:
    -   **left** = 0
    -   **right** = left + (2 X *horizontal\_size*) = 704

In the second case, the rectangle indicated by the **GraphicDestinationRect** member of the DXVA\_BlendCombination structure is displaced to the left by eight to compensate for the shifted picture destination

The second of these two alternatives creates only the destination area that is used for the display.

 

 





