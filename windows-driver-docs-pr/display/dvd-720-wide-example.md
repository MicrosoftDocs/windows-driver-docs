---
title: DVD 720-Wide Example
description: DVD 720-Wide Example
ms.assetid: 02761bf5-afae-4f38-9178-6a721fcad84e
keywords:
- alpha-blend combination WDK DirectX VA , DVD 720-wide example
- blended pictures WDK DirectX VA , DVD 720-wide example
- DVD 720-wide example WDK DirectX VA
- 720-wide example WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DVD 720-Wide Example


## <span id="ddk_dvd_720_wide_example_gg"></span><span id="DDK_DVD_720_WIDE_EXAMPLE_GG"></span>


The use of MPEG-2 on DVD with 720-wide pictures uses picture source rectangle values specified by the **PictureSourceRect16thPel** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure (in one-sixteenth of a luminance sample spacing resolution) with the following values:

-   **left** = 0

-   **right** = **left** + (16 X *horizontal\_size*) = 11520

Generally, the following destination rectangle values are used:

-   **left** = 0

-   **right** = **left** + *horizontal\_size* = 720

 

 





