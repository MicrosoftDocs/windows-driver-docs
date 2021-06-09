---
title: Processing Video Requests (Windows 2000 Model)
description: Processing Video Requests (Windows 2000 Model)
keywords:
- video miniport drivers WDK Windows 2000 , processing requests
- request processing WDK video miniport
- I/O WDK video miniport
- HwVidStartIO
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Video Requests (Windows 2000 Model)


## <span id="ddk_processing_video_requests_windows_2000_model__gg"></span><span id="DDK_PROCESSING_VIDEO_REQUESTS_WINDOWS_2000_MODEL__GG"></span>


All I/O requests that originate in a display driver's call to [**EngDeviceIoControl**](/windows/win32/api/winddi/nf-winddi-engdeviceiocontrol) are mapped from IRP codes (see [IRP Major Function Codes](../kernel/irp-major-function-codes.md)) to *VRPs* by the video port driver. The video port driver then calls the corresponding miniport driver's [*HwVidStartIO*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_start_io) function with a pointer to each [**VIDEO\_REQUEST\_PACKET**](/windows-hardware/drivers/ddi/video/ns-video-_video_request_packet) structure that it sets up. All VRPs sent to *HwVidStartIO* have the **IoControlCode** member set to an IOCTL\_VIDEO\_*XXX*.

The video port driver also manages the synchronization of incoming requests for all video miniport drivers by sending each miniport driver's *HwVidStartIO* routine only one VRP for processing at a time. *HwVidStartIO* owns each input VRP until the miniport driver completes the requested operation and returns control. Until a miniport driver completes the current VRP, the video port driver holds on to any outstanding IRP codes that the I/O manager sends in response to subsequent calls to [**EngDeviceIoControl**](/windows/win32/api/winddi/nf-winddi-engdeviceiocontrol) by the corresponding display driver.

On receipt of a video request, [*HwVidStartIO*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_start_io) must examine the VRP, process the video request on the adapter, set the appropriate status and other information in the VRP, and return **TRUE**.

