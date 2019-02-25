---
title: Vendor Audio Driver Options
description: Vendor Audio Driver Options
ms.assetid: 4306c027-28ae-4299-83c0-29d892bf64ca
keywords:
- WDM audio drivers WDK , vendor options
- audio drivers WDK , vendor options
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vendor Audio Driver Options


## <span id="vendor_audio_driver_options"></span><span id="VENDOR_AUDIO_DRIVER_OPTIONS"></span>


To take advantage of the built-in system support for audio devices, Microsoft recommends that vendors use one of the following:

-   A port class adapter driver (see [Audio Miniport Drivers](audio-miniport-drivers.md)) for an ISA or PCI adapter card

-   The USB Audio class driver (see [USBAudio Class System Driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver)) for a USB Audio device

-   A custom IEEE 1394 device driver (see [AVCAudio Class System Driver](kernel-mode-wdm-audio-components.md#avcaudio_class_system_driver)) for an IEEE 1394 audio device

However, if these options are not sufficient, a vendor can implement one of the following:

-   A proprietary KS filter (see [KS Filters](https://msdn.microsoft.com/library/windows/hardware/ff567644))

-   Microsoft does not recommend a proprietary KS filter because they are difficult to implement, and are unnecessary for most ISA, PCI, and USB devices.

-   Stream class minidriver (see [Streaming Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff568277))

-   Microsoft does not recommend a proprietary stream class minidriver because it is difficult to implement, although it can be appropriate for devices that integrate audio and video.

For an in-depth discussion of the available options for providing driver support for an audio device, see [Getting Started with WDM Audio Drivers](getting-started-with-wdm-audio-drivers.md).

 

 




