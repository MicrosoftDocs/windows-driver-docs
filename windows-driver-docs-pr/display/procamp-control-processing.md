---
title: ProcAmp Control Processing
description: ProcAmp Control Processing
ms.assetid: feb66d91-1b25-415b-83f4-a75361b9dc11
keywords: ["DirectX Video Acceleration WDK Windows 2000 display , ProcAmp", "Video Acceleration WDK DirectX , ProcAmp", "VA WDK DirectX , ProcAmp", "ProcAmp WDK DirectX VA", "ProcAmp WDK DirectX VA , about ProcAmp control processing", "VMR WDK DirectX VA"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20ProcAmp%20Control%20Processing%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




