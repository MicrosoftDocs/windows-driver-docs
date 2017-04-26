---
title: Supplying Video Substream and Destination Surfaces
description: Supplying Video Substream and Destination Surfaces
ms.assetid: 53528c49-11d1-4e53-b700-f6d8d760bcfe
keywords:
- DeinterlaceBltEx, destination surfaces
- DeinterlaceBltEx, substream surfaces
- destination surfaces WDK DirectX VA
- substream surfaces WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supplying Video Substream and Destination Surfaces


## <span id="ddk_supplying_video_substream_and_destination_surfaces_gg"></span><span id="DDK_SUPPLYING_VIDEO_SUBSTREAM_AND_DESTINATION_SURFACES_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The VMR on Windows Server 2003 SP1 and later and Windows XP SP2 and later only supplies video substreams with substream-surface formats that DXVA supports. That is, the VMR only supplies the following [*FOURCC*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc) codes for alpha-blending substream-surface formats: AI44, IA44 or AYUV. For more information, see [Loading an AYUV Alpha-Blending Surface](loading-an-ayuv-alpha-blending-surface.md). Note that when multiple video substreams are supplied, each substream might be formatted differently. Because the formats of the supplied video substreams are palletized surface formats, a complete 16-color palette for each surface is supplied in the **Palette** member of each [**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092) structure in the array that is passed in the *pDDSrcSurfaces* parameter when *DeinterlaceBltEx* is called. Therefore, the driver is not required to maintain palette information for each video substream surface.

The VMR also only supplies destination surfaces whose formats are specified by the driver in the **d3dOutputFormat** member of the [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure. The driver returns a pointer to DXVA\_DeinterlaceCaps when its [**DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563946) function is called.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supplying%20Video%20Substream%20and%20Destination%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




