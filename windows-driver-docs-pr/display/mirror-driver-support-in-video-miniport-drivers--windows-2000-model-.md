---
title: Mirror Driver Support in Video Miniport Drivers (Windows 2000 Model)
description: Mirror Driver Support in Video Miniport Drivers (Windows 2000 Model)
ms.assetid: ca91e0a6-d619-432a-829e-49012951f27c
keywords:
- video miniport drivers WDK Windows 2000 , mirror drivers
- mirror drivers WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mirror Driver Support in Video Miniport Drivers (Windows 2000 Model)


## <span id="ddk_mirror_driver_support_in_video_miniport_drivers_windows_2000_model"></span><span id="DDK_MIRROR_DRIVER_SUPPORT_IN_VIDEO_MINIPORT_DRIVERS_WINDOWS_2000_MODEL"></span>


[*Mirror driver*](https://msdn.microsoft.com/library/windows/hardware/ff556308#wdkgloss-mirror-driver) support for video miniport drivers is provided by Windows 2000 and later, so a miniport driver must not have any special code to attempt such support. See [Mirror Drivers](mirror-drivers.md) for more information about display drivers in mirroring systems.

The requirements for a mirror driver miniport driver are minimal. The only functions which must be implemented are [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556159), which is exported by the miniport driver, and the following:

[*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332)

[*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345)

[*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367)

Since there is no physical display device associated with a mirrored surface, all three of the functions shown in the preceding list can be empty implementations that always return success.

**Note**  Starting with Windows 8, mirror drivers will not install on the system. For more information, see [Mirror Drivers](mirror-drivers.md).

 

 

 





