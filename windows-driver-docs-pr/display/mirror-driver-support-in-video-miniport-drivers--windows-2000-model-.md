---
title: Mirror Driver Support in Video Miniport Drivers (Windows 2000 Model)
description: Mirror Driver Support in Video Miniport Drivers (Windows 2000 Model)
ms.assetid: ca91e0a6-d619-432a-829e-49012951f27c
keywords: ["video miniport drivers WDK Windows 2000 , mirror drivers", "mirror drivers WDK Windows 2000 display"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Mirror%20Driver%20Support%20in%20Video%20Miniport%20Drivers%20%28Windows%202000%20Model%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




