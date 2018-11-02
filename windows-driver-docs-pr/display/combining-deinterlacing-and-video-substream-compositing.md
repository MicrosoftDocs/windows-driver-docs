---
title: Combining Deinterlacing and Video Substream Compositing
description: Combining Deinterlacing and Video Substream Compositing
ms.assetid: d62fe460-104d-4aff-a88c-3dc5829321fa
keywords:
- DeinterlaceBltEx
- deinterlacing WDK DirectX VA , combining substream compositing
- combining substream compositing WDK DirectX VA
- video substream compositing WDK DirectX VA
- substream compositing WDK DirectX VA
- VMR WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Combining Deinterlacing and Video Substream Compositing


## <span id="ddk_combining_deinterlacing_and_video_substream_compositing_gg"></span><span id="DDK_COMBINING_DEINTERLACING_AND_VIDEO_SUBSTREAM_COMPOSITING_GG"></span>


This section applies only to Microsoft Windows Server 2003 with Service Pack 1 (SP1) and later, and Windows XP with Service Pack 2 (SP2) and later.

To improve video quality on hardware with limited memory bandwidth, driver writers can implement the [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) function in their display drivers. The **DeinterlaceBltEx** function combines, within the YUV color space, operations that composite the video substreams on top of the video stream with operations that deinterlace and/or frame-rate convert each video frame. Driver writers are encouraged to support the **DeinterlaceBltEx** function in their drivers for all of their deinterlacing modes.

The following topics describe how to support **DeinterlaceBltEx**:

[Overview of DeinterlaceBltEx](overview-of-deinterlacebltex.md)

[Reporting Support for DeinterlaceBltEx](reporting-support-for-deinterlacebltex.md)

[Supplying Video Substream and Destination Surfaces](supplying-video-substream-and-destination-surfaces.md)

[Supporting Operations on Video Substream and Destination Surfaces](supporting-operations-on-video-substream-and-destination-surfaces.md)

[Displaying Samples and Background Color in the Target Rectangle](displaying-samples-and-background-color-in-the-target-rectangle.md)

[Processing Subrectangles](processing-subrectangles.md)

[Input Buffer Order](input-buffer-order.md)

[Deinterlacing and Compositing on 64-bit Operating Systems](deinterlacing-and-compositing-on-64-bit-operating-systems.md)

 

 





