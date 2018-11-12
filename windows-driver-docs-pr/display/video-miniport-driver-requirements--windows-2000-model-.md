---
title: Video Miniport Driver Requirements (Windows 2000 Model)
description: Video Miniport Driver Requirements (Windows 2000 Model)
ms.assetid: f6ae5b71-97d5-4fd8-bd3d-7ee83f34581e
keywords:
- video miniport drivers WDK Windows 2000 , requirements
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Miniport Driver Requirements (Windows 2000 Model)


## <span id="ddk_video_miniport_driver_requirements_windows_2000_model__gg"></span><span id="DDK_VIDEO_MINIPORT_DRIVER_REQUIREMENTS_WINDOWS_2000_MODEL__GG"></span>


The following are some of the requirements for video miniport drivers.

-   **An NT-based operating system video miniport driver must be a single** ***.sys*** **file.**

    A miniport driver consists of a single binary file. The miniport driver's main purpose is to detect, initialize, and configure one or more graphics adapters of the same type.

-   **A miniport driver can only make calls exported by** ***videoprt.sys*.**

    A miniport driver can call only those functions that are exported by the system-supplied video port driver. (The exported video port functions are listed on the reference pages following [Video Port Driver Functions](https://msdn.microsoft.com/library/windows/hardware/ff570533).) Driver writers can also use the following to determine which functions a miniport driver is calling:

    ```cpp
    link -dump -imports my_driver.sys
    ```

    A miniport driver cannot load or install another driver on the machine using undocumented operating system function calls.

-   **A miniport driver can enable panning only upon receiving an end-user request.**

    Panning must be disabled by default. The miniport driver should enable it only when it is requested through a control panel. OEMs can enable panning by default as a part of their preinstall.

 

 





