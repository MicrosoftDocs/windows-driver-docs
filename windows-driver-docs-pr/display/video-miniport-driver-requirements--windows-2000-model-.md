---
title: Video Miniport Driver Requirements (Windows 2000 Model)
description: Video Miniport Driver Requirements (Windows 2000 Model)
ms.assetid: f6ae5b71-97d5-4fd8-bd3d-7ee83f34581e
keywords: ["video miniport drivers WDK Windows 2000 , requirements"]
---

# Video Miniport Driver Requirements (Windows 2000 Model)


## <span id="ddk_video_miniport_driver_requirements_windows_2000_model__gg"></span><span id="DDK_VIDEO_MINIPORT_DRIVER_REQUIREMENTS_WINDOWS_2000_MODEL__GG"></span>


The following are some of the requirements for video miniport drivers.

-   **An NT-based operating system video miniport driver must be a single** ***.sys*** **file.**

    A miniport driver consists of a single binary file. The miniport driver's main purpose is to detect, initialize, and configure one or more graphics adapters of the same type.

-   **A miniport driver can only make calls exported by** ***videoprt.sys*.**

    A miniport driver can call only those functions that are exported by the system-supplied video port driver. (The exported video port functions are listed on the reference pages following [Video Port Driver Functions](https://msdn.microsoft.com/library/windows/hardware/ff570533).) Driver writers can also use the following to determine which functions a miniport driver is calling:

    ```
    link -dump -imports my_driver.sys
    ```

    A miniport driver cannot load or install another driver on the machine using undocumented operating system function calls.

-   **A miniport driver can enable panning only upon receiving an end-user request.**

    Panning must be disabled by default. The miniport driver should enable it only when it is requested through a control panel. OEMs can enable panning by default as a part of their preinstall.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Video%20Miniport%20Driver%20Requirements%20%28Windows%202000%20Model%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




