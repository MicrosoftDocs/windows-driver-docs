---
title: Timers in Video Miniport Drivers
description: Timers in Video Miniport Drivers
keywords:
- video miniport drivers WDK Windows 2000 , timers
- timers WDK video miniport
- HwVidTimer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Timers in Video Miniport Drivers


## <span id="ddk_timers_in_video_miniport_drivers_gg"></span><span id="DDK_TIMERS_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


Any video miniport driver can have a [**HwVidTimer**](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_timer) function at the discretion of the driver writer. A *HwVidTimer* function allows the miniport driver to time out operations or to monitor state changes over a coarser-grained interval than is possible by calling [**VideoPortStallExecution**](/windows-hardware/drivers/ddi/video/nf-video-videoportstallexecution). *HwVidTimer* also does not prevent other system operations from occurring as **VideoPortStallExecution** does.

For example, a miniport driver for an adapter that emulates VGA functionality might have a *HwVidTimer* function that monitors the status of its adapter's "VGA" registers periodically so the driver can emulate VGA-style graphics.

After a call to [**VideoPortStartTimer**](/windows-hardware/drivers/ddi/video/nf-video-videoportstarttimer), the video port driver calls *HwVidTimer* once every second until the video miniport driver calls [**VideoPortStopTimer**](/windows-hardware/drivers/ddi/video/nf-video-videoportstoptimer). A video miniport driver can enable and disable calls to the *HwVidTimer* function repeatedly.

Note that a *HwVidTimer* function cannot disable calls to itself with **VideoPortStopTimer**. Another video miniport driver function must control the enabling or disabling of calls to a *HwVidTimer* function through the use of **VideoPortStartTimer** and **VideoPortStopTimer**.

 

