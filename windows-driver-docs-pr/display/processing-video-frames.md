---
title: Processing Video Frames
description: Processing Video Frames
ms.assetid: 0f613186-1887-4d67-95d6-f562124c69ab
keywords:
- video processing WDK DirectX VA , video frame processing
- video frame processing WDK DirectX VA
- frames WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Processing Video Frames


The Microsoft Direct3D runtime calls the user-mode display driver's [**VideoProcessBeginFrame**](https://msdn.microsoft.com/library/windows/hardware/ff570494) and [**VideoProcessEndFrame**](https://msdn.microsoft.com/library/windows/hardware/ff570497) functions to indicate a time period between these function calls that the user-mode display driver can process video frames. Before the user-mode display driver can process any video frames, the Microsoft Direct3D runtime must call the user-mode display driver's [**SetVideoProcessRenderTarget**](https://msdn.microsoft.com/library/windows/hardware/ff569695) function to set the render target surface for video processing. However, the call to *SetVideoProcessRenderTarget* can occur only outside the begin-frame and end-frame time period.

After the render target surface for video processing is set, the user-mode display driver can receive calls to its [**VideoProcessBlt**](https://msdn.microsoft.com/library/windows/hardware/ff570495) function to process video frames between the begin-frame and end-frame time period.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Processing%20Video%20Frames%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




