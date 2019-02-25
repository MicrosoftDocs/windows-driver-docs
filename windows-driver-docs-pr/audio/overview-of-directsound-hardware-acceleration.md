---
title: Overview of DirectSound Hardware Acceleration
description: Overview of DirectSound Hardware Acceleration
ms.assetid: 1f18f88a-2dd6-4b7a-b083-f43ab58571b3
keywords:
- hardware acceleration WDK DirectSound , about DirectSound hardware acceleration
ms.date: 10/27/2017
ms.localizationpriority: medium
---

# Overview of DirectSound Hardware Acceleration


## <span id="overview_of_directsound_hardware_acceleration"></span><span id="OVERVIEW_OF_DIRECTSOUND_HARDWARE_ACCELERATION"></span>


A number of audio adapters offer DirectSound hardware acceleration, which is the ability to perform hardware mixing for one or more DirectSound streams. Hardware mixing improves performance by offloading audio mixing operations from the CPU and performing them at hardware speeds. In addition to mixing, the hardware performs related operations such as sample-rate conversion (SRC), attenuation, and, optionally, 3D processing that would otherwise need to be performed in software.

All WaveCyclic or WavePci rendering devices present one or more hardware pins for mixing audio streams. In the case of a single-stream device, the [KMixer system driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver) is always instantiated on the one available hardware rendering pin.

Devices with DirectSound hardware acceleration provide more than one hardware mixing pin. Each additional pin can be used to mix a DirectSound stream. DirectSound streams that feed into hardware mixer pins bypass KMixer and avoid the latency of software mixing in KMixer. DirectSound makes use of all of an audio device's available hardware-accelerated mixer pins as long as those pins have a topology that conforms to the [DirectSound node-ordering requirements](directsound-node-ordering-requirements.md). DirectSound also requires that the pins support the DirectSound data format specified by KSDATAFORMAT\_SPECIFIER\_DSOUND (see [DirectSound Stream Data Format](directsound-stream-data-format.md)).

The [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver) always reserves one hardware pin for KMixer so that after the other (unreserved) hardware pins have all been allocated, any additional streams can be mixed by KMixer and fed into the reserved hardware pin.

The figure in [Rendering Wave Content Using DirectSound Software and Hardware Buffers](rendering-wave-content-using-directsound-software-and-hardware-buffers.md) illustrates these concepts.

If an audio device provides a sufficient number of hardware mixing pins, all of a DirectSound application's output streams can be hardware-accelerated. If not, the DirectSound application has a couple of options:

-   It can statically allocate the available hardware mixing pins to the streams that require the lowest latencies.

-   It can dynamically allocate the available hardware mixing pins to the streams as they are needed by treating the pins as a pool of shared resources.

For more information, see the discussion of voice management in the Microsoft Windows SDK documentation.

DirectSound can use two types of hardware mixer pins: 2D and 3D. A 2D pin performs SRC, attenuation, and mixing, but not 3D positioning. DirectSound can use a 2D pin to do 3D positioning by performing the necessary attenuation and frequency calculations in software and applying the results to the appropriate nodes on the 2D pin. In contrast, a 3D pin contains a 3D node that is able to calculate its own 3D effects directly from the 3D-buffer and 3D-listener properties instead of relying on DirectSound to do this. For a list of the properties of a 3D node, see [**KSNODETYPE\_3D\_EFFECTS**](https://msdn.microsoft.com/library/windows/hardware/ff537148). For more information about 2D and 3D pins, see [Supporting 2D DirectSound Acceleration in WDM Audio](supporting-2d-directsound-acceleration-in-wdm-audio.md) and [Supporting 3D DirectSound Acceleration in WDM Audio](supporting-3d-directsound-acceleration-in-wdm-audio.md).

 




