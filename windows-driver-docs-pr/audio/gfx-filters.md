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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20GFX%20Filters%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


