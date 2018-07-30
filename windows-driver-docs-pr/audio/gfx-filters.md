---
title: GFX Filters
description: GFX Filters
ms.assetid: e1b5cb04-7793-4423-8162-3f70e3b9ac42
keywords:
- GFX filters WDK audio
- global effects WDK audio
- audio filters WDK audio , GPX
- filters WDK audio , GPX
- WDM audio drivers WDK , GPX filters
- audio drivers WDK , GPX filters
- GFX filters WDK audio , about GFX filters
- USB WDK audio
- audio proces
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# GFX Filters


## <span id="gfx_filters"></span><span id="GFX_FILTERS"></span>


The 32-bit versions of Windows Server 2003 and Windows XP provide support for global effects (GFX) filtering of an audio stream. These operating systems support GFX filters only for USB audio devices. Hardware vendors can choose to provide GFX filters to augment the capabilities of their USB audio devices.

A GFX filter can apply an audio-signal transform to the final audio mix that is rendered by an audio device. The effect is considered global because it affects all the streams that are combined to create the final mix. Examples of these system effects are equalization, bass enhancement, and speaker correction.

A GFX filter can also process the signal that is captured by an audio device. The GFX filter is inserted into the capture stream before any other processing of the audio signal.

A GFX filter is packaged as an [AVStream](https://msdn.microsoft.com/library/windows/hardware/ff554240) minidriver with an associated INF file. This type of GFX filter must not be confused with the COM-based audio processing objects that were developed for Windows Vista, called GFX sAPOs. For more information about GFX sAPOs, see [Exploring the Windows Vista Audio Engine](exploring-the-windows-vista-audio-engine.md).

For more information about INF files, see [Device Installation Files](https://msdn.microsoft.com/library/windows/hardware/ff541295).

A typical GFX filter implements a digital signal transformation that is designed for a specific audio hardware device (for example, to compensate for the response characteristics of a particular set of speakers). The manufacturer of the audio hardware typically provides the GFX driver. When you install a GFX driver, Windows enables the GFX filter and automatically configures it to begin processing the audio signal that is sent to the specified hardware.

Through the Windows multimedia control panel (Mmsys.cpl), you can do the following:

-   Enable or disable a GFX.

-   Select a GFX filter that is designed for the audio hardware in question. A GFX driver's INF file specifies the target hardware for the GFX.

The audio service uses no more than one GFX on each audio device and keeps track of GFX configurations for each user.

GFX filters can be designed for audio capture devices as well as for audio rendering devices. For example, the manufacturer of a microphone array might provide a GFX filter to process the input signals from the array.

Additionally, a GFX filter typically serves as a host-based (or non-accelerated) enhancement of hardware and is hardware-specific. For example, when a user plugs in USB speakers, a particular GFX filter might automatically load for those speakers. During this process, Windows restores the GFX filter configuration and settings that it saved when the speakers were used previously.

Be aware that GFX filters should not be used to implement virtual audio devices. For example, a GFX filter cannot be used to create a composite, four-channel audio device from two independent stereo audio devices.

**Note**  Any modifications that a vendor makes to an adapter driver to support GFX filters should be compatible with any earlier version of Windows that the driver needs to support.

 

Windows Server 2003 and Windows XP support GFX filters only in 32-bit versions of the operating system. GFX filters do not work in 64-bit systems. For information about digital audio signal processing in Windows Vista, see the [System Effects Audio Processing Objects](system-effects-audio-processing-objects.md) topic.

This section includes the following topics:

[Requirements for a GFX Filter Factory](requirements-for-a-gfx-filter-factory.md)

[Installing a Device-Specific GFX Filter](installing-a-device-specific-gfx-filter.md)

[GFX Data Format Requirements](gfx-data-format-requirements.md)

[Vendor's GFX User Interface](vendor-s-gfx-user-interface.md)

[Persistence of GFX Settings](persistence-of-gfx-settings.md)

[Target Device ID](target-device-id.md)

[DRM Requirements for GFX Drivers](drm-requirements-for-gfx-drivers.md)

 

 




