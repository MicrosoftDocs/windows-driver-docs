---
title: MPEG-2 Pan-Scan Example
description: MPEG-2 Pan-Scan Example
ms.assetid: 6ce4722c-5406-4b29-9171-ecab049320e7
keywords:
- alpha-blend combination WDK DirectX VA , MPEG-2 pan-scan example
- blended pictures WDK DirectX VA , MPEG-2 pan-scan example
- PictureSourceRect16thPel
- MPEG-2 pan-scan example WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MPEG-2 Pan-Scan Example


## <span id="ddk_mpeg_2_pan_scan_example_gg"></span><span id="DDK_MPEG_2_PAN_SCAN_EXAMPLE_GG"></span>


When the **PictureSourceRect16thPel** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure is used to select an area specified by MPEG-2 video pan-scan parameters, the values for **PictureSourceRect16thPel** members can be computed using the following expressions. These values should not violate the restrictions described for the alpha-blend combination buffers when using **PictureSourceRect16thPel**. For more information, see the **Remarks** section for the DXVA\_BlendCombination structure.

These constraints could be violated with some MPEG-2 pan-scan parameters and, in particular, with some MPEG-2 DVD content, requiring some adjustments to the **PictureSourceRect16thPel**.

-   **left** = 8 x (*horizontal\_size* - *display\_horizontal\_size*) - *frame\_centre\_horizontal\_offset*

-   **top** = 8 x (*vertical\_size - display\_vertical\_size*) - *frame\_centre\_vertical\_offset*

-   **right** = **left** + (16 x *display\_horizontal\_size*)

-   **bottom** = **top** + (16 x *display\_vertical\_size*)

The **PictureDestinationRect** member of the DXVA\_BlendCombination structure would then typically use the following values:

-   **left** = 0 or 8 (as in [DVD 704-Wide Non-Pan-Scan Picture Example](dvd-704-wide-non-pan-scan-example.md))

-   **top** = 0

-   **right** = **left** + *display\_horizontal\_size*

-   **bottom** = **top** + *display\_vertical\_size*

 

 





