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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Motion Compensation Callbacks


## <span id="ddk_motion_compensation_callbacks_gg"></span><span id="DDK_MOTION_COMPENSATION_CALLBACKS_GG"></span>


[DirectX Video Acceleration](directx-video-acceleration.md) makes use of the following motion compensation callback functions provided in DirectDraw drivers for acceleration of digital video decoding processing, with support of alpha blending for such purposes as DVD subpicture support:

[*DdMoCompBeginFrame*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_beginframe)

[*DdMoCompCreate*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_create)

[*DdMoCompDestroy*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_destroy)

[*DdMoCompEndFrame*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_endframe)

[*DdMoCompGetBuffInfo*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_getcompbuffinfo)

[*DdMoCompGetFormats*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_getformats)

[*DdMoCompGetGuids*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_getguids)

[*DdMoCompGetInternalInfo*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_getinternalinfo)

[*DdMoCompQueryStatus*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_querystatus)

[*DdMoCompRender*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_render)

The motion compensation callback functions comprise the device driver side of the DirectX Video Acceleration interface. The motion compensation callback functions are specified by members of the [**DD\_MOTIONCOMPCALLBACKS**](https://docs.microsoft.com/windows/desktop/api/ddrawint/ns-ddrawint-dd_motioncompcallbacks) structure. The following steps show how motion compensation callback functions are accessed:

1.  GUIDs received from **IAMVideoAccelerator::GetVideoAcceleratorGUIDs** originate from the device driver's [*DdMoCompGetGuids*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_getguids).

2.  A call to the downstream input pin's **IAMVideoAccelerator::GetUncompFormatsSupported** returns data from the device driver's [*DdMoCompGetFormats*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_getformats).

3.  At the start of the relevant processing, the [**DXVA\_ConnectMode**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_connectmode) data structure from the output pin of the decoder's **IAMVideoAcceleratorNotify::GetCreateVideoAcceleratorData** is passed to the device driver's [*DdMoCompCreate*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_create), which notifies the decoder about the video acceleration object.

4.  Data returned from **IAMVideoAccelerator::GetCompBufferInfo** originates from the device driver's [*DdMoCompGetBuffInfo*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_getcompbuffinfo).

5.  Buffers sent using **IAMVideoAccelerator::Execute** are received by the device driver's [*DdMoCompRender*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_render).

6.  Use of **IAMVideoAccelerator::QueryRenderStatus** calls the device driver's [*DdMoCompQueryStatus*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_querystatus). A return code of DDERR\_WASSTILLDRAWING from *DdMoCompQueryStatus* will be seen by the host decoder as a return code of E\_PENDING from **IAMVideoAccelerator::QueryRenderStatus**.

7.  Data sent to **IAMVideoAccelerator::BeginFrame** is received by the device driver's [*DdMoCompBeginFrame*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_beginframe). A return code of DDERR\_WASSTILLDRAWING is needed from *DdMoCompBeginFrame* in order for E\_PENDING to be seen by the host decoder in response to **IAMVideoAccelerator::BeginFrame**.

8.  Data sent to **IAMVideoAccelerator::EndFrame** is received by the device driver's [*DdMoCompEndFrame*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_endframe).

9.  At the end of the relevant processing, the device driver's [*DdMoCompDestroy*](https://docs.microsoft.com/windows/desktop/api/ddrawint/nc-ddrawint-pdd_mocompcb_destroy) is used to notify the driver that the current video acceleration object will no longer be used, so that the driver can perform any necessary cleanup.

 

 





