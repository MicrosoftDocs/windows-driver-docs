---
title: Mirror Driver Support in Video Miniport Drivers (XDDM)
description: Mirror Driver Support in Video Miniport Drivers (Windows 2000 Model)
keywords:
- video miniport drivers WDK Windows 2000 , mirror drivers
- mirror drivers WDK Windows 2000 display
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Mirror Driver Support in Video Miniport Drivers (Windows 2000 Model)

> [!NOTE]
>
> Starting with Windows 8, mirror drivers will not install on the system. For more information, see [Mirror Drivers](mirror-drivers.md).


*Mirror driver* support for video miniport drivers is provided by Windows 2000 and later, so a miniport driver must not have any special code to attempt such support. See [Mirror Drivers](mirror-drivers.md) for more information about display drivers in mirroring systems.

The requirements for a mirror driver miniport driver are minimal. The only functions which must be implemented are [**DriverEntry**](./driverentry-of-video-miniport-driver.md), which is exported by the miniport driver, and the following:

[*HwVidFindAdapter*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_find_adapter)

[*HwVidInitialize*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_initialize)

[*HwVidStartIO*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_start_io)

Since there is no physical display device associated with a mirrored surface, all three of the functions shown in the preceding list can be empty implementations that always return success.
