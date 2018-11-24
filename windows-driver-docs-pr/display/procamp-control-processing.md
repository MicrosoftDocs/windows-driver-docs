---
title: ProcAmp Control Processing
description: ProcAmp Control Processing
ms.assetid: feb66d91-1b25-415b-83f4-a75361b9dc11
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , ProcAmp
- Video Acceleration WDK DirectX , ProcAmp
- VA WDK DirectX , ProcAmp
- ProcAmp WDK DirectX VA
- ProcAmp WDK DirectX VA , about ProcAmp control processing
- VMR WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ProcAmp Control Processing


## <span id="ddk_procamp_control_processing_gg"></span><span id="DDK_PROCAMP_CONTROL_PROCESSING_GG"></span>


The ProcAmp control DDI extends DirectX VA to support ProcAmp control and post processing of video content by graphics device drivers. The ProcAmp control DDI is an interface between the video mixing renderer ([*VMR*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-mixer-renderer--vmr-)) and the graphics device driver. The DDI maps to the existing DirectDraw and DirectX VA DDI. The DDI is not accessible via the **IAMVideoAccelerator** interface. The ProcAmp control DDI is available in Microsoft DirectX version 9.0.

If a driver supports accelerated decoding of compressed video, the VMR will call the driver to create two DirectX VA devices, one to perform the actual video decoding work, and the other to be used strictly for ProcAmp adjustments.

This section covers the following topics:

[Processing in the 8-bit YUV Color Space](processing-in-the-8-bit-yuv-color-space.md)

[VMR Video Processing](vmr-video-processing.md)

[Mapping the ProcAmp Control DDI to DirectDraw and DirectX VA](mapping-the-procamp-control-ddi-to-directdraw-and-directx-va.md)

[ProcAmp Properties](procamp-properties.md)

[Sample Functions for ProcAmp Control](sample-functions-for-procamp-control.md)

 

 





