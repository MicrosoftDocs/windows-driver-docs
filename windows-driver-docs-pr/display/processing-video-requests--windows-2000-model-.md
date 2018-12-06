---
title: Processing Video Requests (Windows 2000 Model)
description: Processing Video Requests (Windows 2000 Model)
ms.assetid: 86b3037e-2d18-46b0-8b02-c66be65a4001
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


All I/O requests that originate in a display driver's call to [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) are mapped from IRP codes (see [IRP Major Function Codes](https://msdn.microsoft.com/library/windows/hardware/ff550710)) to [*VRPs*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-request-packet--vrp-) by the video port driver. The video port driver then calls the corresponding miniport driver's [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) function with a pointer to each [**VIDEO\_REQUEST\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff570547) structure that it sets up. All VRPs sent to *HwVidStartIO* have the **IoControlCode** member set to an IOCTL\_VIDEO\_*XXX*.

The video port driver also manages the synchronization of incoming requests for all video miniport drivers by sending each miniport driver's *HwVidStartIO* routine only one VRP for processing at a time. *HwVidStartIO* owns each input VRP until the miniport driver completes the requested operation and returns control. Until a miniport driver completes the current VRP, the video port driver holds on to any outstanding IRP codes that the I/O manager sends in response to subsequent calls to [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) by the corresponding display driver.

On receipt of a video request, [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) must examine the VRP, process the video request on the adapter, set the appropriate status and other information in the VRP, and return **TRUE**.

 

 





