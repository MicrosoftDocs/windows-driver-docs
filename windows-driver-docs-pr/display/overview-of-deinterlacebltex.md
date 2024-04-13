---
title: Overview of DeinterlaceBltEx
description: Overview of DeinterlaceBltEx
keywords:
- DeinterlaceBltEx, about DeinterlaceBltEx
- VMR WDK DirectX VA
ms.date: 04/20/2017
---

# Overview of DeinterlaceBltEx


## <span id="ddk_overview_of_deinterlacebltex_gg"></span><span id="DDK_OVERVIEW_OF_DEINTERLACEBLTEX_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The VMR on Windows Server 2003 SP1 and later and Windows XP SP2 and later can initiate calls to the display driver's [**DeinterlaceBltEx**](./dxva-deinterlacebobdeviceclass-deinterlacebltex.md) function to combine deinterlacing and substream compositing operations.

The VMR on Windows Server 2003 and Windows XP SP1 uses DXVA to deinterlace or frame-rate convert video and to output the video onto an RGB32 surface. The VMR then uses Direct3D to combine video substreams with the video image. In other words, the video is first deinterlaced, resized, and then color-space converted to a Direct3D RGB32 render target using the display driver's [**DeinterlaceBlt**](./dxva-deinterlacebobdeviceclass-deinterlaceblt.md) function. Then, video substreams are composited over the top of the resulting video image using calls to the display driver's [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) function.

By using *DeinterlaceBltEx* rather than *DeinterlaceBlt* and *D3dDrawPrimitives2* combined, operations can be performed more efficiently on the available hardware.

The *DeinterlaceBltEx* function also can be called with progressive video and multiple video substreams. This scenario can occur when the VMR is used for DVD playback that contains a mixture of progressive and interlaced video. In this case, the driver should not attempt to deinterlace the video stream because the stream is already progressive. The driver should combine the video stream with any given substreams and resize each stream as required.

If you implement the [**DeinterlaceBltEx**](./dxva-deinterlacebobdeviceclass-deinterlacebltex.md) function in your driver, you must also implement the original [**DeinterlaceBlt**](./dxva-deinterlacebobdeviceclass-deinterlaceblt.md) function. The VMR on Windows Server 2003 SP1 and later and Windows XP SP2 and later can initiate calls to either the driver's *DeinterlaceBltEx* or *DeinterlaceBlt* function; the application controls which function the VMR uses.

 

