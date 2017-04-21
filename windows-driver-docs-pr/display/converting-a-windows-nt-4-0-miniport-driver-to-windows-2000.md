---
title: Converting a Windows NT 4.0 Miniport Driver to Windows 2000
description: Converting a Windows NT 4.0 Miniport Driver to Windows 2000
ms.assetid: a55192c6-3de4-4433-8825-3393f2bce04a
keywords:
- video miniport drivers WDK Windows 2000 , multiple Windows versions, converting a Windows NT 4.0 driver
- converting video miniport drivers WDK Windows 2000
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

    ```
    [ABC.Mfg]   ; Windows NT V4.0 INF
    %ABC% ABC Graphics Accelerator A = abc
    %ABC% ABC Graphics Accelerator B = abc

    [ABC.Mfg]   ; Windows 2000 and later INF
    %ABC% ABC Graphics Accelerator A = abc, PCI\VEN_ABCD&DEV_0123
    %ABC% ABC Graphics Accelerator B = abc, PCI\VEN_ABCD&DEV_4567
    ```

You can use the *geninf.exe* tool that is included with the Driver Development Kit (DDK) to generate an INF. (The DDK preceded the Windows Driver Kit \[WDK\].) Keep in mind, however, that *geninf.exe* does not create an INF for Windows NT 4.0. You must modify the INF file produced by *geninf.exe* if you intend to support Windows NT 4.0. See [Creating Graphics INF Files](creating-graphics-inf-files.md) for more details.

The Windows 2000 and later video port supports Windows NT 4.0 miniport drivers as legacy drivers. The graphics adapter for a legacy miniport driver cannot be removed from the system while the system is running, nor are legacy miniport drivers automatically detected when added to a running system.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Converting%20a%20Windows%20NT%204.0%20Miniport%20Driver%20to%20Windows%202000%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




