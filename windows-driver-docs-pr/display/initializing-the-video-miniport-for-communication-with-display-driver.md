---
title: Initializing Video Miniport/Display Driver Communications
description: Initializing the Video Miniport for Communication with Display Driver
keywords:
- video miniport drivers WDK Windows 2000 , initializing
- initializing video miniport drivers
- HwVidInitialize
- one-time initialization WDK video miniport
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Initializing the Video Miniport for Communication with Display Driver

For each adapter found by the PnP manager and successfully configured by the miniport driver, the miniport driver's [*HwVidInitialize*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_initialize) function is called when the corresponding display driver is loaded. *HwVidInitialize* can initialize software state information, but it should not set up visible state on the adapter. On return from *HwVidInitialize*, the adapter should be set to the same state as on return from the miniport driver's [*HwVidResetHw*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_reset_hw) routine. For more information about *HwVidResetHw*, see [Resetting the Adapter in Video Miniport Drivers](resetting-the-adapter-in-video-miniport-drivers.md).

If necessary, a miniport driver's *HwVidInitialize* function can carry out a one-time initialization operation on the adapter that was postponed by its *HwVidFindAdapter* function. For example, a miniport driver might postpone loading microcode on the adapter and have the *HwVidInitialize* function call [**VideoPortGetRegistryParameters**](/windows-hardware/drivers/ddi/video/nf-video-videoportgetregistryparameters).

When the [*HwVidInitialize*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_initialize) function returns control, the graphics engine has a handle for the miniport driver's adapter. The corresponding display driver then can call the engine's [**EngDeviceIoControl**](/windows/win32/api/winddi/nf-winddi-engdeviceiocontrol) function to request access to mapped video memory or to request any other operation. The video port driver sends such a request on to the miniport driver's [*HwVidStartIO*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_start_io) function, as a *VRP*. See [Processing Video Requests (Windows 2000 Model)](processing-video-requests--windows-2000-model-.md) for details.

Usually, a display driver controls the display the end user sees, except occasionally when a full-screen MS-DOS application is run in an x86-based machine running an NT-based operating system. For more information about supporting this feature in VGA-compatible miniport drivers, see [VGA-Compatible Video Miniport Drivers (Windows 2000 Model)](vga-compatible-video-miniport-drivers--windows-2000-model-.md).

The [*HwVidInitialize*](/windows-hardware/drivers/ddi/video/nc-video-pvideo_hw_initialize) function can call [**VideoPortGetRegistryParameters**](/windows-hardware/drivers/ddi/video/nf-video-videoportgetregistryparameters) or [**VideoPortSetRegistryParameters**](/windows-hardware/drivers/ddi/video/nf-video-videoportsetregistryparameters) to get and set configuration information in the registry. For example, *HwVidInitialize* might call **VideoPortSetRegistryParameters** to set up nonvolatile configuration information in the registry for the next boot. It might call **VideoPortGetRegistryParameters** to get adapter-specific, bus-relative configuration parameters written into the registry by an installation program.

