---
title: DVD 16 9 Letterbox Height in 4 3 Example
description: DVD 16 9 Letterbox Height in 4 3 Example
ms.assetid: 67e5e50e-5102-4392-9430-feddc9609f2e
keywords: ["alpha-blend combination WDK DirectX VA , DVD 16 9 letterbox height example", "blended pictures WDK DirectX VA , DVD 16 9 letterbox height example", "DVD 16 9 letterbox height example WDK DirectX VA", "16 9 letterbox height example WDK DirectX VA"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DVD%2016:9%20Letterbox%20Height%20in%204:3%20Example%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




