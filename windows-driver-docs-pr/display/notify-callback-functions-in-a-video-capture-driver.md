---
title: Notify Callback Functions in a Video Capture Driver
description: Notify Callback Functions in a Video Capture Driver
ms.assetid: 2b900436-7874-43a7-97bf-7d1eead78126
keywords:
- DxApi miniport drivers WDK DirectDraw , notifying callback functions
- notifying callback functions WDK kernel-mode video transport
- callback functions WDK kernel-mode video transport
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Notify Callback Functions in a Video Capture Driver


## <span id="ddk_notify_callback_functions_in_a_video_capture_driver_gg"></span><span id="DDK_NOTIFY_CALLBACK_FUNCTIONS_IN_A_VIDEO_CAPTURE_DRIVER_GG"></span>


The video capture driver supplies notify callback functions to the DirectDraw runtime when the video capture driver calls the runtime's [**DxApi**](https://msdn.microsoft.com/library/windows/hardware/ff557364) function for certain operations. For example, the video capture driver supplies a [*NotifyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff568545) function when the driver calls **DxApi** with the [**DD\_DXAPI\_OPENVIDEOPORT**](https://msdn.microsoft.com/library/windows/hardware/ff551498) function identifier to open a video port. After the video port closes, the DirectDraw runtime is notified and calls *NotifyCallback*. The video capture driver can then perform necessary operations that are related to the video port closing.

The video capture driver supplies a *NotifyCallback* function to the DirectDraw runtime when the video capture driver calls the [**DxApi**](https://msdn.microsoft.com/library/windows/hardware/ff557364) function and specifies any one of the following function identifiers:

-   [**DD\_DXAPI\_OPENDIRECTDRAW**](https://msdn.microsoft.com/library/windows/hardware/ff550702)

-   [**DD\_DXAPI\_OPENSURFACE**](https://msdn.microsoft.com/library/windows/hardware/ff550711)

-   [**DD\_DXAPI\_OPENVIDEOPORT**](https://msdn.microsoft.com/library/windows/hardware/ff551498)

-   [**DD\_DXAPI\_REGISTER\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551502)

-   [**DD\_DXAPI\_OPENVPCAPTUREDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551500)

Thereafter, when an event that is associated with the function identifier occurs, the DirectDraw runtime calls the *NotifyCallback* function. The video capture driver's *NotifyCallback* is implemented to perform operations related to the event.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Notify%20Callback%20Functions%20in%20a%20Video%20Capture%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




