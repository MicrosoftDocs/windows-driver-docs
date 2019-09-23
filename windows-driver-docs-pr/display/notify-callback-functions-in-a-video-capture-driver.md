---
title: Notify Callback Functions in a Video Capture Driver
description: Notify Callback Functions in a Video Capture Driver
ms.assetid: 2b900436-7874-43a7-97bf-7d1eead78126
keywords:
- DxApi miniport drivers WDK DirectDraw , notifying callback functions
- notifying callback functions WDK kernel-mode video transport
- callback functions WDK kernel-mode video transport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Notify Callback Functions in a Video Capture Driver


## <span id="ddk_notify_callback_functions_in_a_video_capture_driver_gg"></span><span id="DDK_NOTIFY_CALLBACK_FUNCTIONS_IN_A_VIDEO_CAPTURE_DRIVER_GG"></span>


The video capture driver supplies notify callback functions to the DirectDraw runtime when the video capture driver calls the runtime's [**DxApi**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxapi/nf-dxapi-dxapi) function for certain operations. For example, the video capture driver supplies a [*NotifyCallback*](https://docs.microsoft.com/windows/desktop/api/ddkmapi/nc-ddkmapi-lpdd_notifycallback) function when the driver calls **DxApi** with the [**DD\_DXAPI\_OPENVIDEOPORT**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551498(v=vs.85)) function identifier to open a video port. After the video port closes, the DirectDraw runtime is notified and calls *NotifyCallback*. The video capture driver can then perform necessary operations that are related to the video port closing.

The video capture driver supplies a *NotifyCallback* function to the DirectDraw runtime when the video capture driver calls the [**DxApi**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxapi/nf-dxapi-dxapi) function and specifies any one of the following function identifiers:

-   [**DD\_DXAPI\_OPENDIRECTDRAW**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff550702(v=vs.85))

-   [**DD\_DXAPI\_OPENSURFACE**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff550711(v=vs.85))

-   [**DD\_DXAPI\_OPENVIDEOPORT**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551498(v=vs.85))

-   [**DD\_DXAPI\_REGISTER\_CALLBACK**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551502(v=vs.85))

-   [**DD\_DXAPI\_OPENVPCAPTUREDEVICE**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551500(v=vs.85))

Thereafter, when an event that is associated with the function identifier occurs, the DirectDraw runtime calls the *NotifyCallback* function. The video capture driver's *NotifyCallback* is implemented to perform operations related to the event.

 

 





