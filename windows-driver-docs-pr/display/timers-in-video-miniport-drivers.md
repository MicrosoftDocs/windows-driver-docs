---
title: Timers in Video Miniport Drivers
description: Timers in Video Miniport Drivers
ms.assetid: 257ea76e-7be6-4895-8e83-0f50c96e5969
keywords:
- video miniport drivers WDK Windows 2000 , timers
- timers WDK video miniport
- HwVidTimer
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Timers in Video Miniport Drivers


## <span id="ddk_timers_in_video_miniport_drivers_gg"></span><span id="DDK_TIMERS_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


Any video miniport driver can have a [**HwVidTimer**](https://msdn.microsoft.com/library/windows/hardware/ff567371) function at the discretion of the driver writer. A *HwVidTimer* function allows the miniport driver to time out operations or to monitor state changes over a coarser-grained interval than is possible by calling [**VideoPortStallExecution**](https://msdn.microsoft.com/library/windows/hardware/ff570368). *HwVidTimer* also does not prevent other system operations from occurring as **VideoPortStallExecution** does.

For example, a miniport driver for an adapter that emulates VGA functionality might have a *HwVidTimer* function that monitors the status of its adapter's "VGA" registers periodically so the driver can emulate VGA-style graphics.

After a call to [**VideoPortStartTimer**](https://msdn.microsoft.com/library/windows/hardware/ff570370), the video port driver calls *HwVidTimer* once every second until the video miniport driver calls [**VideoPortStopTimer**](https://msdn.microsoft.com/library/windows/hardware/ff570371). A video miniport driver can enable and disable calls to the *HwVidTimer* function repeatedly.

Note that a *HwVidTimer* function cannot disable calls to itself with **VideoPortStopTimer**. Another video miniport driver function must control the enabling or disabling of calls to a *HwVidTimer* function through the use of **VideoPortStartTimer** and **VideoPortStopTimer**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Timers%20in%20Video%20Miniport%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




