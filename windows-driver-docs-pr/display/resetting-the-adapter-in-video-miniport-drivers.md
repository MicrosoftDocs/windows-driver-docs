---
title: Resetting the Adapter in Video Miniport Drivers
description: Resetting the Adapter in Video Miniport Drivers
ms.assetid: 321a5b6c-5a70-4acb-bf88-42ffb0cff86d
keywords:
- video miniport drivers WDK Windows 2000 , resetting adapters
- resetting adapters WDK video miniport
- HwVidResetHw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Resetting the Adapter in Video Miniport Drivers


## <span id="ddk_resetting_the_adapter_in_video_miniport_drivers_gg"></span><span id="DDK_RESETTING_THE_ADAPTER_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


Every miniport driver must have a [*HwVidResetHw*](https://msdn.microsoft.com/library/windows/hardware/ff567363) function if its adapter cannot be reset to an initialized state without a hard reboot of the machine.

*HwVidResetHw* is called by the [*HAL*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hal) if the machine is about to crash or if the user initiates a soft reboot of the machine. *HwVidResetHw* resets the adapter to a specified character mode, so the HAL can display crash-dump information as it shuts down the system or initialization information during a soft reboot.

*HwVidResetHw* cannot call the BIOS, cannot call any pageable code, nor may it be made pageable. If possible, it should call only the **VideoPortRead***Xxx* and **VideoPortWrite***Xxx* functions, but it also can call any of the following:

[**VideoPortStallExecution**](https://msdn.microsoft.com/library/windows/hardware/ff570368)

[**VideoPortZeroDeviceMemory**](https://msdn.microsoft.com/library/windows/hardware/ff570492)

[**VideoPortZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff570493)

 

 





