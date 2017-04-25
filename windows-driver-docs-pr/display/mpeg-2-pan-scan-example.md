---
title: MPEG-2 Pan-Scan Example
description: MPEG-2 Pan-Scan Example
ms.assetid: 6ce4722c-5406-4b29-9171-ecab049320e7
keywords:
- alpha-blend combination WDK DirectX VA , MPEG-2 pan-scan example
- blended pictures WDK DirectX VA , MPEG-2 pan-scan example
- PictureSourceRect16thPel
- MPEG-2 pan-scan example WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20MPEG-2%20Pan-Scan%20Example%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




