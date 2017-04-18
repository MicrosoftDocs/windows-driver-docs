---
title: Resetting the Adapter in Video Miniport Drivers
description: Resetting the Adapter in Video Miniport Drivers
ms.assetid: 321a5b6c-5a70-4acb-bf88-42ffb0cff86d
keywords: ["video miniport drivers WDK Windows 2000 , resetting adapters", "resetting adapters WDK video miniport", "HwVidResetHw"]
---

# Resetting the Adapter in Video Miniport Drivers


## <span id="ddk_resetting_the_adapter_in_video_miniport_drivers_gg"></span><span id="DDK_RESETTING_THE_ADAPTER_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


Every miniport driver must have a [*HwVidResetHw*](https://msdn.microsoft.com/library/windows/hardware/ff567363) function if its adapter cannot be reset to an initialized state without a hard reboot of the machine.

*HwVidResetHw* is called by the [*HAL*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hal) if the machine is about to crash or if the user initiates a soft reboot of the machine. *HwVidResetHw* resets the adapter to a specified character mode, so the HAL can display crash-dump information as it shuts down the system or initialization information during a soft reboot.

*HwVidResetHw* cannot call the BIOS, cannot call any pageable code, nor may it be made pageable. If possible, it should call only the **VideoPortRead***Xxx* and **VideoPortWrite***Xxx* functions, but it also can call any of the following:

[**VideoPortStallExecution**](https://msdn.microsoft.com/library/windows/hardware/ff570368)

[**VideoPortZeroDeviceMemory**](https://msdn.microsoft.com/library/windows/hardware/ff570492)

[**VideoPortZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff570493)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Resetting%20the%20Adapter%20in%20Video%20Miniport%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




