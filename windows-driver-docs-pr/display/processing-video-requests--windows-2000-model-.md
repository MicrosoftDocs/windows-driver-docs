---
title: Processing Video Requests (Windows 2000 Model)
description: Processing Video Requests (Windows 2000 Model)
ms.assetid: 86b3037e-2d18-46b0-8b02-c66be65a4001
keywords:
- video miniport drivers WDK Windows 2000 , processing requests
- request processing WDK video miniport
- I/O WDK video miniport
- HwVidStartIO
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Processing Video Requests (Windows 2000 Model)


## <span id="ddk_processing_video_requests_windows_2000_model__gg"></span><span id="DDK_PROCESSING_VIDEO_REQUESTS_WINDOWS_2000_MODEL__GG"></span>


All I/O requests that originate in a display driver's call to [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) are mapped from IRP codes (see [IRP Major Function Codes](https://msdn.microsoft.com/library/windows/hardware/ff550710)) to [*VRPs*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-request-packet--vrp-) by the video port driver. The video port driver then calls the corresponding miniport driver's [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) function with a pointer to each [**VIDEO\_REQUEST\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff570547) structure that it sets up. All VRPs sent to *HwVidStartIO* have the **IoControlCode** member set to an IOCTL\_VIDEO\_*XXX*.

The video port driver also manages the synchronization of incoming requests for all video miniport drivers by sending each miniport driver's *HwVidStartIO* routine only one VRP for processing at a time. *HwVidStartIO* owns each input VRP until the miniport driver completes the requested operation and returns control. Until a miniport driver completes the current VRP, the video port driver holds on to any outstanding IRP codes that the I/O manager sends in response to subsequent calls to [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) by the corresponding display driver.

On receipt of a video request, [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) must examine the VRP, process the video request on the adapter, set the appropriate status and other information in the VRP, and return **TRUE**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Processing%20Video%20Requests%20%28Windows%202000%20Model%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




