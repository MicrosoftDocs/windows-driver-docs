---
title: Initializing Video Miniport/Display Driver Communications
description: Initializing the Video Miniport for Communication with Display Driver
ms.assetid: 73ba423c-7ebc-4a07-aed0-d2e33f11b878
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

For each adapter found by the PnP manager and successfully configured by the miniport driver, the miniport driver's [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) function is called when the corresponding display driver is loaded. *HwVidInitialize* can initialize software state information, but it should not set up visible state on the adapter. On return from *HwVidInitialize*, the adapter should be set to the same state as on return from the miniport driver's [*HwVidResetHw*](https://msdn.microsoft.com/library/windows/hardware/ff567363) routine. For more information about *HwVidResetHw*, see [Resetting the Adapter in Video Miniport Drivers](resetting-the-adapter-in-video-miniport-drivers.md).

If necessary, a miniport driver's *HwVidInitialize* function can carry out a one-time initialization operation on the adapter that was postponed by its *HwVidFindAdapter* function. For example, a miniport driver might postpone loading microcode on the adapter and have the *HwVidInitialize* function call [**VideoPortGetRegistryParameters**](https://msdn.microsoft.com/library/windows/hardware/ff570316).

When the *HwVidInitialize*. See [Processing Video Requests (Windows 2000 Model)](processing-video-requests--windows-2000-model-.md) for details.

Usually, a display driver controls the display the end user sees, except occasionally when a full-screen MS-DOS application is run in an x86-based machine running an NT-based operating system. For more information about supporting this feature in VGA-compatible miniport drivers, see [VGA-Compatible Video Miniport Drivers (Windows 2000 Model)](vga-compatible-video-miniport-drivers--windows-2000-model-.md).

The [*HwVidInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff567345) function can call [**VideoPortGetRegistryParameters**](https://msdn.microsoft.com/library/windows/hardware/ff570316) or [**VideoPortSetRegistryParameters**](https://msdn.microsoft.com/library/windows/hardware/ff570365) to get and set configuration information in the registry. For example, *HwVidInitialize* might call **VideoPortSetRegistryParameters** to set up nonvolatile configuration information in the registry for the next boot. It might call **VideoPortGetRegistryParameters** to get adapter-specific, bus-relative configuration parameters written into the registry by an installation program.

 

 





