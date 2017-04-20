---
title: Introduction to DirectX VA
description: Introduction to DirectX VA
ms.assetid: e7d4faf7-f6ec-49ec-8116-faeed1ddd01c
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , about DirectX Video Acceleration
- Video Acceleration WDK DirectX , about DirectX Video Acceleration
- VA WDK DirectX , about DirectX Video Acceleration
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to DirectX VA


## <span id="ddk_introduction_to_directx_va_gg"></span><span id="DDK_INTRODUCTION_TO_DIRECTX_VA_GG"></span>


DirectX VA allows video processing operations that are frequently executed and simple to be performed by a hardware accelerator. Confining less complex video processing operations to the accelerator allows video decoding acceleration to be accomplished for various video standards with minimal customization to the accelerator. Video processing operations that are less frequently executed and more complex, such as bitstream parsing and variable-length decoding (VLD), can be performed on the host CPU.

The DirectX VA API and corresponding [motion compensation](motion-compensation.md) DDI provide support for the following operations:

-   [Alpha blending](https://msdn.microsoft.com/library/windows/hardware/ff538232) for purposes such as DVD subpicture support.

-   [Encryption](encryption-support.md) for applications that require it.

-   [Deinterlacing and frame-rate conversion](deinterlacing-and-frame-rate-conversion.md) of video content.

-   [ProcAmp](procamp-control-processing.md) control and post processing of video content.

-   Protecting video content from unauthorized copying and displaying through the [Certified Output Protection Protocol](copp-processing.md).

The information presented here is applicable to both application and device driver developers. The format specified defines how information is exchanged between the user-mode host decoder and the kernel-mode device driver. In most cases, the data is transferred from the host to the device driver but, in some cases, data is sent in the other direction.

For sample code used for decoding Windows media video format, see the Windows media sample drivers in the Windows Media Porting Kit. The Windows Media Porting Kit is used to convert audio and video to Windows media format.

For support of Windows media format, the Windows Media Video Codec version 9 or higher must be used. Windows Media Video Codecs version 8 supplied with Windows XP do not support DirectX VA.

For a display driver that uses the [deinterlacing DDI](deinterlacing-and-frame-rate-conversion.md), video content must be interlaced and properly marked as interlaced. The video mixing renderer (VMR) uses the VIDEOINFOHEADER2 structure in conjunction with the deinterlacing DDI to deinterlace and perform frame-rate conversion. For more information about the VIDEOINFOHEADER2 structure, see the Windows SDK documentation.

The [ProcAmp control DDI](procamp-control-processing.md) extends DirectX VA to support ProcAmp control and post processing of video content by graphics device drivers. The DDI maps to the existing DirectDraw and DirectX VA DDI. The DDI is not accessible through the **IAMVideoAccelerator** interface. The ProcAmp control DDI is available in Microsoft DirectX 9.0 and later versions only.

The [Implementation of Current Standards](implementation-of-current-standards.md) topic details the hardware accelerator and software decoder requirements that must be met for the following, motion-compensated video codec standards: ITU-T H.261, MPEG-1, MPEG-2 (H.262), ITU-T H.263, MPEG-4, MPEG-4 AVC (H.264), and VC-1.

There are no tools supplied with DirectX VA. For more information about tools supplied for Windows media support, see the Windows Media Porting Kit.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Introduction%20to%20DirectX%20VA%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




