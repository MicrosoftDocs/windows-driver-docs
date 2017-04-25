---
title: Motion Compensation Callbacks
description: Motion Compensation Callbacks
ms.assetid: a1f748e4-0d62-4543-a409-bb9ec02a7d77
keywords:
- drawing WDK DirectDraw , motion compensation
- DirectDraw WDK Windows 2000 display , motion compensation
- motion compensation WDK
- compressed video decoding WDK DirectDraw
- video decoding WDK DirectDraw
- decoding WDK DirectDraw
- callback functions WDK DirectDraw motion compensation
- digital video decoding WDK DirectDraw
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Motion Compensation Callbacks


## <span id="ddk_motion_compensation_callbacks_gg"></span><span id="DDK_MOTION_COMPENSATION_CALLBACKS_GG"></span>


[DirectX Video Acceleration](directx-video-acceleration.md) makes use of the following motion compensation callback functions provided in DirectDraw drivers for acceleration of digital video decoding processing, with support of alpha blending for such purposes as DVD subpicture support:

[*DdMoCompBeginFrame*](https://msdn.microsoft.com/library/windows/hardware/ff549648)

[*DdMoCompCreate*](https://msdn.microsoft.com/library/windows/hardware/ff549656)

[*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664)

[*DdMoCompEndFrame*](https://msdn.microsoft.com/library/windows/hardware/ff549669)

[*DdMoCompGetBuffInfo*](https://msdn.microsoft.com/library/windows/hardware/ff549683)

[*DdMoCompGetFormats*](https://msdn.microsoft.com/library/windows/hardware/ff549691)

[*DdMoCompGetGuids*](https://msdn.microsoft.com/library/windows/hardware/ff550236)

[*DdMoCompGetInternalInfo*](https://msdn.microsoft.com/library/windows/hardware/ff550240)

[*DdMoCompQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff550243)

[*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248)

The motion compensation callback functions comprise the device driver side of the DirectX Video Acceleration interface. The motion compensation callback functions are specified by members of the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. The following steps show how motion compensation callback functions are accessed:

1.  GUIDs received from **IAMVideoAccelerator::GetVideoAcceleratorGUIDs** originate from the device driver's [*DdMoCompGetGuids*](https://msdn.microsoft.com/library/windows/hardware/ff550236).

2.  A call to the downstream input pin's **IAMVideoAccelerator::GetUncompFormatsSupported** returns data from the device driver's [*DdMoCompGetFormats*](https://msdn.microsoft.com/library/windows/hardware/ff549691).

3.  At the start of the relevant processing, the [**DXVA\_ConnectMode**](https://msdn.microsoft.com/library/windows/hardware/ff563138) data structure from the output pin of the decoder's **IAMVideoAcceleratorNotify::GetCreateVideoAcceleratorData** is passed to the device driver's [*DdMoCompCreate*](https://msdn.microsoft.com/library/windows/hardware/ff549656), which notifies the decoder about the video acceleration object.

4.  Data returned from **IAMVideoAccelerator::GetCompBufferInfo** originates from the device driver's [*DdMoCompGetBuffInfo*](https://msdn.microsoft.com/library/windows/hardware/ff549683).

5.  Buffers sent using **IAMVideoAccelerator::Execute** are received by the device driver's [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248).

6.  Use of **IAMVideoAccelerator::QueryRenderStatus** calls the device driver's [*DdMoCompQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff550243). A return code of DDERR\_WASSTILLDRAWING from *DdMoCompQueryStatus* will be seen by the host decoder as a return code of E\_PENDING from **IAMVideoAccelerator::QueryRenderStatus**.

7.  Data sent to **IAMVideoAccelerator::BeginFrame** is received by the device driver's [*DdMoCompBeginFrame*](https://msdn.microsoft.com/library/windows/hardware/ff549648). A return code of DDERR\_WASSTILLDRAWING is needed from *DdMoCompBeginFrame* in order for E\_PENDING to be seen by the host decoder in response to **IAMVideoAccelerator::BeginFrame**.

8.  Data sent to **IAMVideoAccelerator::EndFrame** is received by the device driver's [*DdMoCompEndFrame*](https://msdn.microsoft.com/library/windows/hardware/ff549669).

9.  At the end of the relevant processing, the device driver's [*DdMoCompDestroy*](https://msdn.microsoft.com/library/windows/hardware/ff549664) is used to notify the driver that the current video acceleration object will no longer be used, so that the driver can perform any necessary cleanup.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Motion%20Compensation%20Callbacks%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




