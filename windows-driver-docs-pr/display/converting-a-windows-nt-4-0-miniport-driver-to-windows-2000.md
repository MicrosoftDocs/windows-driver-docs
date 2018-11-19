---
title: Converting a Windows NT 4.0 Miniport Driver to Windows 2000
description: Converting a Windows NT 4.0 Miniport Driver to Windows 2000
ms.assetid: a55192c6-3de4-4433-8825-3393f2bce04a
keywords:
- video miniport drivers WDK Windows 2000 , multiple Windows versions, converting a Windows NT 4.0 driver
- converting video miniport drivers WDK Windows 2000
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Converting a Windows NT 4.0 Miniport Driver to Windows 2000


## <span id="ddk_converting_a_windows_nt_4_0_miniport_driver_to_windows_2000_gg"></span><span id="DDK_CONVERTING_A_WINDOWS_NT_4_0_MINIPORT_DRIVER_TO_WINDOWS_2000_GG"></span>


A good Windows NT 4.0 and previous miniport driver can easily become a Windows 2000 and later miniport driver. The following are some of the updates necessary to provide Plug and Play support, which is required in Windows 2000 and later miniport drivers:

-   See [Plug and Play and Power Management in Video Miniport Drivers (Windows 2000 Model)](plug-and-play-and-power-management-in-video-miniport-drivers--windows-.md) for a list of new functions that must be implemented. Be sure to initialize the new members of [**VIDEO\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff570505) to point to these new functions.

-   Update the call to [**VideoPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff570320) in your [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556159) function. The fourth parameter (*HwContext*) must be **NULL** on Windows 2000 and later.

-   Update your [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) function. For devices on an enumerable bus, *HwVidFindAdapter* must be changed as follows:

    -   Remove most of your device detection code. This is because a call to [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) on Windows 2000 means that the PnP manager has already detected the device.
    -   Call [**VideoPortGetAccessRanges**](https://msdn.microsoft.com/library/windows/hardware/ff570302) to obtain the bus-relative physical addresses to which the device will respond. These addresses are assigned by the PnP manager.
    -   If the driver supports more than one device type, determine the type of device.
    -   Ignore the [*Again*](https://msdn.microsoft.com/library/windows/hardware/ff567332) parameter. This is because the system will call *HwVidFindAdapter* only once per device.

    For a device on a nonenumerable bus such as ISA, PnP still attempts to start the device, although it is the responsibility of [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) to determine whether the device is actually present.

-   Update the **.Mfg** section of the driver's INF file to include the device and vendor ID. This is required so that the PnP manager can associate the device with its INF file. Samples of the Windows NT 4.0 and updated Windows 2000 and later **.Mfg** sections follow:

    ```cpp
    [ABC.Mfg]   ; Windows NT V4.0 INF
    %ABC% ABC Graphics Accelerator A = abc
    %ABC% ABC Graphics Accelerator B = abc

    [ABC.Mfg]   ; Windows 2000 and later INF
    %ABC% ABC Graphics Accelerator A = abc, PCI\VEN_ABCD&DEV_0123
    %ABC% ABC Graphics Accelerator B = abc, PCI\VEN_ABCD&DEV_4567
    ```

You can use the *geninf.exe* tool that is included with the Driver Development Kit (DDK) to generate an INF. (The DDK preceded the Windows Driver Kit \[WDK\].) Keep in mind, however, that *geninf.exe* does not create an INF for Windows NT 4.0. You must modify the INF file produced by *geninf.exe* if you intend to support Windows NT 4.0. See [Creating Graphics INF Files](creating-graphics-inf-files.md) for more details.

The Windows 2000 and later video port supports Windows NT 4.0 miniport drivers as legacy drivers. The graphics adapter for a legacy miniport driver cannot be removed from the system while the system is running, nor are legacy miniport drivers automatically detected when added to a running system.

 

 





