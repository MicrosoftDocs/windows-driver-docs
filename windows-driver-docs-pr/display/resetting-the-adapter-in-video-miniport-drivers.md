---
title: Resetting the Adapter in Video Miniport Drivers
description: Resetting the Adapter in Video Miniport Drivers
keywords:
- video miniport drivers WDK Windows 2000 , resetting adapters
- resetting adapters WDK video miniport
- HwVidResetHw
ms.date: 04/20/2017
---

# Resetting the Adapter in Video Miniport Drivers


## <span id="ddk_resetting_the_adapter_in_video_miniport_drivers_gg"></span><span id="DDK_RESETTING_THE_ADAPTER_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


Every miniport driver must have a [*HwVidResetHw*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_reset_hw) function if its adapter cannot be reset to an initialized state without a hard reboot of the machine.

*HwVidResetHw* is called by the *HAL* if the machine is about to crash or if the user initiates a soft reboot of the machine. *HwVidResetHw* resets the adapter to a specified character mode, so the HAL can display crash-dump information as it shuts down the system or initialization information during a soft reboot.

*HwVidResetHw* cannot call the BIOS, cannot call any pageable code, nor may it be made pageable. If possible, it should call only the **VideoPortRead***Xxx* and **VideoPortWrite***Xxx* functions, but it also can call any of the following:

[**VideoPortStallExecution**](/windows-hardware/drivers/ddi/video/nf-video-videoportstallexecution)

[**VideoPortZeroDeviceMemory**](/windows-hardware/drivers/ddi/video/nf-video-videoportzerodevicememory)

[**VideoPortZeroMemory**](/windows-hardware/drivers/ddi/video/nf-video-videoportzeromemory)

 

