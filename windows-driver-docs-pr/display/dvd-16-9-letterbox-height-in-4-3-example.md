---
title: DVD 16 9 Letterbox Height in 4 3 Example
description: DVD 16 9 Letterbox Height in 4 3 Example
ms.assetid: 67e5e50e-5102-4392-9430-feddc9609f2e
keywords:
- alpha-blend combination WDK DirectX VA , DVD 16 9 letterbox height example
- blended pictures WDK DirectX VA , DVD 16 9 letterbox height example
- DVD 16 9 letterbox height example WDK DirectX VA
- 16 9 letterbox height example WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DVD 16:9 Letterbox Height in 4:3 Example


## <span id="ddk_dvd_16_9_letterbox_height_in_4_3_example_gg"></span><span id="DDK_DVD_16_9_LETTERBOX_HEIGHT_IN_4_3_EXAMPLE_GG"></span>


The use of 16:9 video for 4:3 displays with letterbox framing for DVD has the following values for the source and destination pictures.

The following rectangle values are used in the **PictureSourceRect16thPel** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure for the source picture:

-   **top** = 0

-   **bottom** = **top** + (16 X *vertical\_size*) = 7680 or 9216

The following rectangle values are used in the **PictureDestinationRect** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure for the destination picture:

-   **top** = *vertical\_size* / 8 = 60 or 72

-   **bottom** = 7 X *vertical\_size* / 8 = 420 or 504

 

 





