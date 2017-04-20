---
title: DirectX Video Acceleration
description: DirectX Video Acceleration
ms.assetid: e25407a3-be5c-4509-a3e7-d9688958e3d4
keywords:
- DirectX Video Acceleration WDK Windows 2000 display
- Video Acceleration WDK DirectX
- motion compensation WDK
- VA WDK DirectX
- accelerators WDK DirectX
- display driver model WDK Windows 2000 , DirectX Video Acceleration
- Windows 2000 display driver model WDK , DirectX Video Acceleration
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DirectX Video Acceleration


## <span id="ddk_directx_video_acceleration_gg"></span><span id="DDK_DIRECTX_VIDEO_ACCELERATION_GG"></span>


This section contains information about Microsoft DirectX Video Acceleration (DirectX VA). This is an application programming interface (API) and a corresponding [motion compensation](motion-compensation.md) device driver interface (DDI) for acceleration of digital video decoding. The following additional DDIs are also provided as part of DirectX VA:

-   A [deinterlacing DDI](https://msdn.microsoft.com/library/windows/hardware/ff552701) for deinterlacing and frame-rate conversion of video content.

-   A [ProcAmp DDI](https://msdn.microsoft.com/library/windows/hardware/ff569186) to support ProcAmp control and postprocessing of video content.

-   A [COPP DDI](https://msdn.microsoft.com/library/windows/hardware/ff540449) for protecting video content.

Driver writers who are creating DirectX VA drivers for Microsoft Windows XP with Service Pack 1 (SP1) and later should use the *dxva.h* header file. This contains the structures and enumerations used for video acceleration and deinterlacing, and frame-rate conversion.

This section includes the following topics:

[Introduction to DirectX VA](introduction-to-directx-va.md)

[Video Decoding](video-decoding.md)

[Deinterlacing and Frame-Rate Conversion](deinterlacing-and-frame-rate-conversion.md)

[ProcAmp Control Processing](procamp-control-processing.md)

[COPP Processing](copp-processing.md)

[Example Code for DirectX VA Devices](example-code-for-directx-va-devices.md)

[DirectX VA Data Flow Management](directx-va-data-flow-management.md)

[DirectX VA Operations](directx-va-operations.md)

[Defining Accelerator Capabilities](defining-accelerator-capabilities.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DirectX%20Video%20Acceleration%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




