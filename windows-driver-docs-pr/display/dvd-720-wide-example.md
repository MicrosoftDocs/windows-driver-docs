---
title: DVD 720-Wide Example
description: DVD 720-Wide Example
ms.assetid: 02761bf5-afae-4f38-9178-6a721fcad84e
keywords:
- alpha-blend combination WDK DirectX VA , DVD 720-wide example
- blended pictures WDK DirectX VA , DVD 720-wide example
- DVD 720-wide example WDK DirectX VA
- 720-wide example WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DVD 720-Wide Example


## <span id="ddk_dvd_720_wide_example_gg"></span><span id="DDK_DVD_720_WIDE_EXAMPLE_GG"></span>


The use of MPEG-2 on DVD with 720-wide pictures uses picture source rectangle values specified by the **PictureSourceRect16thPel** member of the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure (in one-sixteenth of a luminance sample spacing resolution) with the following values:

-   **left** = 0

-   **right** = **left** + (16 X *horizontal\_size*) = 11520

Generally, the following destination rectangle values are used:

-   **left** = 0

-   **right** = **left** + *horizontal\_size* = 720

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DVD%20720-Wide%20Example%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




