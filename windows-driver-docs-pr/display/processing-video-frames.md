---
title: Processing Video Frames
description: Processing Video Frames
keywords:
- video processing WDK DirectX VA , video frame processing
- video frame processing WDK DirectX VA
- frames WDK DirectX VA
ms.date: 04/20/2017
---

# Processing Video Frames


The Microsoft Direct3D runtime calls the user-mode display driver's [**VideoProcessBeginFrame**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_videoprocessbeginframe) and [**VideoProcessEndFrame**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_videoprocessendframe) functions to indicate a time period between these function calls that the user-mode display driver can process video frames. Before the user-mode display driver can process any video frames, the Microsoft Direct3D runtime must call the user-mode display driver's [**SetVideoProcessRenderTarget**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setvideoprocessrendertarget) function to set the render target surface for video processing. However, the call to *SetVideoProcessRenderTarget* can occur only outside the begin-frame and end-frame time period.

After the render target surface for video processing is set, the user-mode display driver can receive calls to its [**VideoProcessBlt**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_videoprocessblt) function to process video frames between the begin-frame and end-frame time period.

 

