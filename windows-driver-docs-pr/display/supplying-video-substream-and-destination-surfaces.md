---
title: Supplying Video Substream and Destination Surfaces
description: Supplying Video Substream and Destination Surfaces
ms.assetid: 53528c49-11d1-4e53-b700-f6d8d760bcfe
keywords:
- DeinterlaceBltEx, destination surfaces
- DeinterlaceBltEx, substream surfaces
- destination surfaces WDK DirectX VA
- substream surfaces WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supplying Video Substream and Destination Surfaces


## <span id="ddk_supplying_video_substream_and_destination_surfaces_gg"></span><span id="DDK_SUPPLYING_VIDEO_SUBSTREAM_AND_DESTINATION_SURFACES_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The VMR on Windows Server 2003 SP1 and later and Windows XP SP2 and later only supplies video substreams with substream-surface formats that DXVA supports. That is, the VMR only supplies the following [*FOURCC*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc) codes for alpha-blending substream-surface formats: AI44, IA44 or AYUV. For more information, see [Loading an AYUV Alpha-Blending Surface](loading-an-ayuv-alpha-blending-surface.md). Note that when multiple video substreams are supplied, each substream might be formatted differently. Because the formats of the supplied video substreams are palletized surface formats, a complete 16-color palette for each surface is supplied in the **Palette** member of each [**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092) structure in the array that is passed in the *pDDSrcSurfaces* parameter when *DeinterlaceBltEx* is called. Therefore, the driver is not required to maintain palette information for each video substream surface.

The VMR also only supplies destination surfaces whose formats are specified by the driver in the **d3dOutputFormat** member of the [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure. The driver returns a pointer to DXVA\_DeinterlaceCaps when its [**DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563946) function is called.

 

 





