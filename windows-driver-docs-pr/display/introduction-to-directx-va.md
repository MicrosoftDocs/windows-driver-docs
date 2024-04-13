---
title: DXVA V1.0 Support Overview
description: Introduction to DirectX VA
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , about DirectX Video Acceleration
- Video Acceleration WDK DirectX , about DirectX Video Acceleration
- VA WDK DirectX , about DirectX Video Acceleration
ms.date: 03/18/2022
---

# DXVA v1.0 support overview

DirectX Video Acceleration Version 1.0 (DXVA) allows video processing operations that are frequently executed and simple to be performed by a hardware accelerator. Confining less complex video processing operations to the accelerator allows video decoding acceleration to be accomplished for various video standards with minimal customization to the accelerator. Video processing operations that are less frequently executed and more complex, such as bitstream parsing and variable-length decoding (VLD), can be performed on the host CPU.

The DXVA Version 1.0 API and corresponding [motion compensation](motion-compensation.md) DDI provide support for the following operations:

- [Alpha blending](directx-va-operations.md) for purposes such as DVD subpicture support.

- [Encryption](encryption-support.md) for applications that require it.

- [Deinterlacing and frame-rate conversion](deinterlacing-and-frame-rate-conversion.md) of video content.

- [ProcAmp](procamp-control-processing.md) control and post processing of video content.

- Protecting video content from unauthorized copying and displaying through the [Certified Output Protection Protocol](copp-processing.md).

The information presented here is applicable to both application and device driver developers. The format specified defines how information is exchanged between the user-mode host decoder and the kernel-mode device driver. In most cases, the data is transferred from the host to the device driver but, in some cases, data is sent in the other direction.

For sample code used for decoding Windows media video format, see the Windows media sample drivers in the Windows Media Porting Kit. The Windows Media Porting Kit is used to convert audio and video to Windows media format.

For support of Windows media format, the Windows Media Video Codec version 9 or higher must be used.

For a display driver that uses the [deinterlacing DDI](deinterlacing-and-frame-rate-conversion.md), video content must be interlaced and properly marked as interlaced. The video mixing renderer (VMR) uses the VIDEOINFOHEADER2 structure in conjunction with the deinterlacing DDI to deinterlace and perform frame-rate conversion. For more information about the VIDEOINFOHEADER2 structure, see the Windows SDK documentation.

The [ProcAmp control DDI](procamp-control-processing.md) extends DirectX VA to support ProcAmp control and post processing of video content by graphics device drivers. The DDI maps to the existing DirectDraw and DirectX VA DDI. The DDI is not accessible through the **IAMVideoAccelerator** interface. The ProcAmp control DDI is available in Microsoft DirectX 9.0 and later versions only.

The hardware accelerator and software decoder requirements that must be met for the various motion-compensated video codec standards can be found under the following topics:

- [ITU-T H.261](itu-t-h-261.md)
- [MPEG-1](mpeg-1.md)
- [MPEG-2 (H.262)](mpeg-2--h-262-.md)
- [ITU-T H.263](itu-t-h-263.md)
- [MPEG-4](mpeg-4.md)
- [MPEG-4 AVC (H.264)](mpeg-4-avc--h-264-.md)
- [VC-1](vc-1.md)

There are no tools supplied with DirectX VA. For more information about tools supplied for Windows media support, see the Windows Media Porting Kit.
