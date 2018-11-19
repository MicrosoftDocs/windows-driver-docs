---
title: Processing Video Frames
description: Processing Video Frames
ms.assetid: 0f613186-1887-4d67-95d6-f562124c69ab
keywords:
- video processing WDK DirectX VA , video frame processing
- video frame processing WDK DirectX VA
- frames WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Video Frames


The Microsoft Direct3D runtime calls the user-mode display driver's [**VideoProcessBeginFrame**](https://msdn.microsoft.com/library/windows/hardware/ff570494) and [**VideoProcessEndFrame**](https://msdn.microsoft.com/library/windows/hardware/ff570497) functions to indicate a time period between these function calls that the user-mode display driver can process video frames. Before the user-mode display driver can process any video frames, the Microsoft Direct3D runtime must call the user-mode display driver's [**SetVideoProcessRenderTarget**](https://msdn.microsoft.com/library/windows/hardware/ff569695) function to set the render target surface for video processing. However, the call to *SetVideoProcessRenderTarget* can occur only outside the begin-frame and end-frame time period.

After the render target surface for video processing is set, the user-mode display driver can receive calls to its [**VideoProcessBlt**](https://msdn.microsoft.com/library/windows/hardware/ff570495) function to process video frames between the begin-frame and end-frame time period.

 

 





