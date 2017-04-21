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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Combining%20Deinterlacing%20and%20Video%20Substream%20Compositing%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




