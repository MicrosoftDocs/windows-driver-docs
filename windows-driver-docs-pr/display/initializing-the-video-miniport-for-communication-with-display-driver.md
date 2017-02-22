---
title: Initializing the Video Miniport for Communication with Display Driver
description: Initializing the Video Miniport for Communication with Display Driver
ms.assetid: 73ba423c-7ebc-4a07-aed0-d2e33f11b878
keywords: ["video miniport drivers WDK Windows 2000 , initializing", "initializing video miniport drivers", "HwVidInitialize", "one-time initialization WDK video miniport"]
---

# Initializing the Video Miniport for Communication with Display Driver


## <span id="ddk_initializing_the_video_miniport_for_communication_with_display_dri"></span><span id="DDK_INITIALIZING_THE_VIDEO_MINIPORT_FOR_COMMUNICATION_WITH_DISPLAY_DRI"></span>


For each adapter found by the PnP manager and successfully configured by the miniport driver, the miniport driver's [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) function is called when the corresponding display driver is loaded. *HwVidInitialize* can initialize software state information, but it should not set up visible state on the adapter. On return from *HwVidInitialize*, the adapter should be set to the same state as on return from the miniport driver's [*HwVidResetHw*](https://msdn.microsoft.com/library/windows/hardware/ff567363) routine. For more information about *HwVidResetHw*, see [Resetting the Adapter in Video Miniport Drivers](resetting-the-adapter-in-video-miniport-drivers.md).

If necessary, a miniport driver's *HwVidInitialize* function can carry out a one-time initialization operation on the adapter that was postponed by its *HwVidFindAdapter* function. For example, a miniport driver might postpone loading microcode on the adapter and have the *HwVidInitialize* function call [**VideoPortGetRegistryParameters**](https://msdn.microsoft.com/library/windows/hardware/ff570316).

When the [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) function returns control, the graphics engine has a handle for the miniport driver's adapter. The corresponding display driver then can call the engine's [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) function to request access to mapped video memory or to request any other operation. The video port driver sends such a request on to the miniport driver's [*HwVidStartIO*](https://msdn.microsoft.com/library/windows/hardware/ff567367) function, as a [*VRP*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-request-packet--vrp-). See [Processing Video Requests (Windows 2000 Model)](processing-video-requests--windows-2000-model-.md) for details.

Usually, a display driver controls the display the end user sees, except occasionally when a full-screen MS-DOS application is run in an x86-based machine running an NT-based operating system. For more information about supporting this feature in VGA-compatible miniport drivers, see [VGA-Compatible Video Miniport Drivers (Windows 2000 Model)](vga-compatible-video-miniport-drivers--windows-2000-model-.md).

The [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) function can call [**VideoPortGetRegistryParameters**](https://msdn.microsoft.com/library/windows/hardware/ff570316) or [**VideoPortSetRegistryParameters**](https://msdn.microsoft.com/library/windows/hardware/ff570365) to get and set configuration information in the registry. For example, *HwVidInitialize* might call **VideoPortSetRegistryParameters** to set up nonvolatile configuration information in the registry for the next boot. It might call **VideoPortGetRegistryParameters** to get adapter-specific, bus-relative configuration parameters written into the registry by an installation program.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Initializing%20the%20Video%20Miniport%20for%20Communication%20with%20Display%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




