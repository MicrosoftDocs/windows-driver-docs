---
title: Video Miniport Driver's Device Extension (Windows 2000 Model)
description: Video Miniport Driver's Device Extension (Windows 2000 Model)
ms.assetid: 4d7841d1-39e2-4bdf-b79b-3feb363a0fe5
keywords:
- video miniport drivers WDK Windows 2000 , device extensions
- device extensions WDK video miniport
- extensions WDK video miniport
- adapter states WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Miniport Driver's Device Extension (Windows 2000 Model)


## <span id="ddk_video_miniport_driver_s_device_extension_windows_2000_model__gg"></span><span id="DDK_VIDEO_MINIPORT_DRIVER_S_DEVICE_EXTENSION_WINDOWS_2000_MODEL__GG"></span>


A device extension is each miniport driver's primary and only global storage area for adapter-specific state information.

Each miniport driver defines the size, internal structure, and contents of its device extension. The video port driver passes a pointer to the device extension as an input parameter to every system-defined miniport driver function except **DriverEntry** and, if implemented, the [*HwVidSynchronizeExecutionCallback*](https://msdn.microsoft.com/library/windows/hardware/ff567369) and *SvgaHwIoPortXxx* functions. Many **VideoPort***Xxx* functions require this pointer as an argument as well.

The miniport driver must also use the device extension to maintain the state information for a single adapter. Each adapter detected by the system will have separate state information maintained in a separate device extension. The miniport driver must not use global variables to store any per-adapter state. This is especially critical in order to provide seamless multiple monitor support.

 

 





