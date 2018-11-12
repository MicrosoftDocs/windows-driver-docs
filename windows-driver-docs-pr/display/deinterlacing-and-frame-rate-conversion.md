---
title: Deinterlacing and Frame-Rate Conversion
description: Deinterlacing and Frame-Rate Conversion
ms.assetid: 73435a68-532a-4a15-b2b9-a6165cadb8fe
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , frame-rate conversion
- Video Acceleration WDK DirectX , frame-rate conversion
- VA WDK DirectX , frame-rate conversion
- DirectX Video Acceleration WDK Windows 2000 display , deinterlacing
- Video Acceleration WDK DirectX , deinterlacing
- VA WDK DirectX , deinterlacing
- deinterlacing WDK DirectX VA
- frame-rate conversion WDK DirectX VA
- deinterlacing WDK DirectX VA , about deinterlacing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deinterlacing and Frame-Rate Conversion


## <span id="ddk_deinterlacing_and_frame_rate_conversion_gg"></span><span id="DDK_DEINTERLACING_AND_FRAME_RATE_CONVERSION_GG"></span>


A DDI between the DirectDraw and the graphics device driver extends DirectX VA to support deinterlacing and frame-rate conversion of video content by using the kernel-mode portion of the DirectDraw DDI and the Direct3D DDI. The deinterlace and frame-rate conversion interface is independent of all video presentation mechanisms.

The output of the deinterlacing or frame-rate conversion process is always a progressive frame.

To use this interface, the following requirements must be met:

-   The deinterlaced output must physically exist in the target DirectDraw surface. This requirement precludes all hardware overlay solutions.

-   The graphics engine and the hardware overlay, if present, must support a minimum of bob and weave deinterlacing functionality.

-   This DDI applies to Microsoft Windows XP SP1 and later versions.

This section covers the following topics:

[Deinterlace Modes](deinterlace-modes.md)

[Frame-Rate Conversion Modes](frame-rate-conversion-modes.md)

[Bob Deinterlacing](bob-deinterlacing.md)

[Mapping the Deinterlace DDI to DirectDraw and DirectX VA](mapping-the-deinterlace-ddi-to-directdraw-and-directx-va.md)

[Video Content for Deinterlace and Frame-Rate Conversion](video-content-for-deinterlace-and-frame-rate-conversion.md)

[Deinterlacing on 64-bit Operating Systems](deinterlacing-on-64-bit-operating-systems.md)

[Combining Deinterlacing and Video Substream Compositing](combining-deinterlacing-and-video-substream-compositing.md)

[Sample Functions for Deinterlacing](sample-functions-for-deinterlacing.md)

 

 





