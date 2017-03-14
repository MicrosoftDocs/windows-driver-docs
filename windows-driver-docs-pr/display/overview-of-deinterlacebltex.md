---
title: Overview of DeinterlaceBltEx
description: Overview of DeinterlaceBltEx
ms.assetid: ff487508-eb04-4d4d-9057-ed2d9ea273e0
keywords: ["DeinterlaceBltEx, about DeinterlaceBltEx", "VMR WDK DirectX VA"]
---

# Overview of DeinterlaceBltEx


## <span id="ddk_overview_of_deinterlacebltex_gg"></span><span id="DDK_OVERVIEW_OF_DEINTERLACEBLTEX_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The VMR on Windows Server 2003 SP1 and later and Windows XP SP2 and later can initiate calls to the display driver's [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) function to combine deinterlacing and substream compositing operations.

The VMR on Windows Server 2003 and Windows XP SP1 uses DXVA to deinterlace or frame-rate convert video and to output the video onto an RGB32 surface. The VMR then uses Direct3D to combine video substreams with the video image. In other words, the video is first deinterlaced, resized, and then color-space converted to a Direct3D RGB32 render target using the display driver's [**DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563924) function. Then, video substreams are composited over the top of the resulting video image using calls to the display driver's [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function.

By using *DeinterlaceBltEx* rather than *DeinterlaceBlt* and *D3dDrawPrimitives2* combined, operations can be performed more efficiently on the available hardware.

The *DeinterlaceBltEx* function also can be called with progressive video and multiple video substreams. This scenario can occur when the VMR is used for DVD playback that contains a mixture of progressive and interlaced video. In this case, the driver should not attempt to deinterlace the video stream because the stream is already progressive. The driver should combine the video stream with any given substreams and resize each stream as required.

If you implement the [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) function in your driver, you must also implement the original [**DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563924) function. The VMR on Windows Server 2003 SP1 and later and Windows XP SP2 and later can initiate calls to either the driver's *DeinterlaceBltEx* or *DeinterlaceBlt* function; the application controls which function the VMR uses.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Overview%20of%20DeinterlaceBltEx%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




