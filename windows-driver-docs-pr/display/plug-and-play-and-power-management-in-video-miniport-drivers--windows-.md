---
title: Plug and Play and Power Management in Video Miniport Drivers (Windows 2000)
description: Plug and Play and Power Management in Video Miniport Drivers (Windows 2000 Model)
ms.assetid: e5b2ac53-e492-43de-91a3-5b02c26ee9a3
keywords: ["video miniport drivers WDK Windows 2000 , Plug and Play", "video miniport drivers WDK Windows 2000 , power management", "Plug and Play WDK video miniport", "PnP WDK video miniport", "power management WDK video miniport"]
---

# Plug and Play and Power Management in Video Miniport Drivers (Windows 2000 Model)


## <span id="ddk_plug_and_play_and_power_management_in_video_miniport_drivers_windo"></span><span id="DDK_PLUG_AND_PLAY_AND_POWER_MANAGEMENT_IN_VIDEO_MINIPORT_DRIVERS_WINDO"></span>


All Windows 2000 and later miniport drivers must support Plug and Play and Power Management. This includes the ability to enumerate child devices such as [*DDC*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-ddc) monitors, inter-integrated circuit (I²C) devices, and secondary adapters.

The video port driver manages most of the PnP requirements for the miniport driver, including creating the FDO (Functional Device Object) and receiving and dispatching PnP-specific IRP codes (see [IRP Major Function Codes](https://msdn.microsoft.com/library/windows/hardware/ff550710)) on the miniport driver's behalf.

Miniport drivers must implement the following functions to support PnP and Power Management:

[*HwVidSetPowerState*](https://msdn.microsoft.com/library/windows/hardware/ff567365)

[*HwVidGetPowerState*](https://msdn.microsoft.com/library/windows/hardware/ff567336)

[*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341)

The graphics adapter for a legacy miniport driver cannot be removed from the system while the system is running, nor are legacy miniport drivers automatically detected when added to a running system.

See [Child Devices of the Display Adapter (Windows 2000 Model)](child-devices-of-the-display-adapter--windows-2000-model-.md) for more information about detecting and communicating with an adapter's child devices. For general information about Plug and Play drivers, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Plug%20and%20Play%20and%20Power%20Management%20in%20Video%20Miniport%20Drivers%20%28Windows%202000%20Model%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




