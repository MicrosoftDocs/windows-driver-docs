---
title: Bob Deinterlacing Mechanics
description: Bob Deinterlacing Mechanics
ms.assetid: 1735f9c6-ac83-4a6a-bc6f-4d4a193876dd
keywords:
- bob deinterlacing WDK DirectX VA , mechanics
- interleaved fields WDK DirectX VA
- stride WDK DirectX VA
- deinterlacing WDK DirectX VA , bob, mechanics
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bob Deinterlacing Mechanics


## <span id="ddk_bob_deinterlacing_mechanics_gg"></span><span id="DDK_BOB_DEINTERLACING_MECHANICS_GG"></span>


All graphics adapters that can perform bit-block transfers can do simple bob-style deinterlacing. When a surface contains two interleaved fields, the memory layout of the surface can be reinterpreted to isolate each field. This is achieved by doubling the original surface's stride and dividing the height of the surface in half. After the two fields are isolated in this way, they can be deinterlaced by stretching the individual fields to the correct frame height.

Additional horizontal stretching or shrinking can also be applied to correct the aspect ratio for the pixels of the video image. A display driver can determine its ability to do this to the DirectX Video Mixing Renderer (VMR). The individual field's height can be stretched vertically by line replication or, preferably, by a filtered stretch. If the line replication method is used, the resulting image has a blocky appearance. If a filtered stretch is used, the resulting image may have a slightly fuzzy appearance.

The following figure shows a video surface that contains two interleaved fields.

![diagram illustrating memory layout of a surface containing two interleaved fields](images/deinterlace.png)

If the video sample contains two interleaved fields as specified by the **DXVA\_SampleFieldInterleavedEvenFirst** and **DXVA\_SampleFieldInterleavedOddFirst** members of the [**DXVA\_SampleFormat**](https://msdn.microsoft.com/library/windows/hardware/ff564045) enumeration, the start time of the second field is calculated using the **rtStart** and **rtEnd** members of the [**DXVA\_VideoSample**](https://msdn.microsoft.com/library/windows/hardware/ff564085) structure as follows:

(**rtStart** + **rtEnd**) / 2

The end time of the first field is the start time of the second field.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Bob%20Deinterlacing%20Mechanics%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




