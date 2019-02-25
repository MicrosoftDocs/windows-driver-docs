---
title: Reporting Support for DeinterlaceBltEx
description: Reporting Support for DeinterlaceBltEx
ms.assetid: 9cf8d05c-ef59-44a4-a377-66282e7888d5
keywords:
- DeinterlaceBltEx, reporting
- DXVA_VideoProcess_SubStreamsExtended
- DXVA_VideoProcess_YUV2RGBExtended
- DXVA_VideoProcess_AlphaBlendExtended
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Support for DeinterlaceBltEx


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The display driver reports support for the [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927)[deinterlace DDI](https://msdn.microsoft.com/library/windows/hardware/ff552701) function by setting the DXVA\_VideoProcess\_SubStreams, DXVA\_VideoProcess\_StretchX, and DXVA\_VideoProcess\_StretchY flags in the **VideoProcessingCaps** member of the [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure. The driver returns a pointer to DXVA\_DeinterlaceCaps when its [**DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563946) function is called.

The display driver sets DXVA\_VideoProcess\_SubStreams to combine video substream compositing with deinterlacing. The driver sets DXVA\_VideoProcess\_StretchX and DXVA\_VideoProcess\_StretchY because the pixel aspect ratio of the video stream and substreams can be different and nonsquare, and the driver must be able to independently stretch (horizontally and/or vertically) the video frame that is submitted for deinterlacing as well as the supplied video substreams.

The DXVA\_VideoProcess\_YUV2RGB and DXVA\_VideoProcess\_AlphaBlend flags in the **VideoProcessingCaps** member of the [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure have no meaning in the context of the driver's [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) function. These flags relate to the original [**DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563924) function. Because a display driver that supports *DeinterlaceBltEx* must also support *DeinterlaceBlt*, the driver must still report these flags if it supports their associated operations in the context of *DeinterlaceBlt*.

### <span id="DXVA_VideoProcess_SubStreamsExtended_DXVA_VideoProcess_YUV2RGBExtended_and_DXVA_VideoProcess_AlphaBlendExtended_flags"></span><span id="dxva_videoprocess_substreamsextended_dxva_videoprocess_yuv2rgbextended_and_dxva_videoprocess_alphablendextended_flags"></span><span id="DXVA_VIDEOPROCESS_SUBSTREAMSEXTENDED_DXVA_VIDEOPROCESS_YUV2RGBEXTENDED_AND_DXVA_VIDEOPROCESS_ALPHABLENDEXTENDED_FLAGS"></span>DXVA\_VideoProcess\_SubStreamsExtended DXVA\_VideoProcess\_YUV2RGBExtended and DXVA\_VideoProcess\_AlphaBlendExtended flags

A display driver that implements the [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) function can support significantly enhanced color information for each source and destination surface. The driver can report such support by setting the DXVA\_VideoProcess\_SubStreamsExtended, DXVA\_VideoProcess\_YUV2RGBExtended, and DXVA\_VideoProcess\_AlphaBlendExtended flags in the **VideoProcessingCaps** member of the [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure.

Support for the DXVA\_VideoProcess\_SubStreamsExtended flag indicates that the display driver can perform the necessary color adjustments to the source video streams and substreams. These adjustments are indicated in the extended color data, as the video is deinterlaced, composited with the substreams, and written to the destination surface. Extended color data is specified by members of the [**DXVA\_ExtendedFormat**](https://msdn.microsoft.com/library/windows/hardware/ff563967) structure in the **SampleFormat** members of the [**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092) structures for the source sample array (*lpDDSrcSurfaces* parameter in the [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) call or **Source** member of the [**DXVA\_DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563915) structure).

Support for the DXVA\_VideoProcess\_YUV2RGBExtended flag indicates that the display driver can perform a color-space-conversion operation as the deinterlaced and composited pixels are written to the destination surface. If an RGB destination surface is passed to the display driver, the VMR ensures that each color channel contains a minimum of 8 bits. An RGB destination surface could be an offscreen, texture, or Direct3D render target, or a combined texture and Direct3D render target surface type. The VMR still specifies the background color parameter in the YUV color space even though an RGB destination surface is used.

Support for the DXVA\_VideoProcess\_AlphaBlendExtended flag indicates that the display driver can perform an alpha-blend operation with the destination surface when the deinterlaced and composited pixels are written to the destination surface. The driver must handle background color based on the alpha value of the *fAlpha* parameter in the [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) call. When the alpha value is 1.0f, the background color is drawn opaque (without transparency). When the alpha value is 0.0f, the background should not be drawn (transparent).

 

 





