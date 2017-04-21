---
title: Synthesizer Timing
description: Synthesizer Timing
ms.assetid: 38aca8b7-f895-4b16-aaac-5a13973cf976
keywords:
- synthesizers WDK audio , timing
- time WDK audio
- reference clocks WDK audio
- sample clocks WDK audio
- clocks WDK audio , synthesizers
- user-mode synths WDK audio , synthesizer timing
- custom synths WDK audio , synthesizer timing
- DirectMusic custom rendering WDK audio , synthesizer timing
- custom rendering in user mode WDK audio , synthesizer timing
- DirectMusic WDK audio , synthesizers
- timers WDK audio
- clocks WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Synthesizer Timing


## <span id="synthesizer_timing"></span><span id="SYNTHESIZER_TIMING"></span>


The synthesizer works with two different systems of time:

-   Reference time

-   Sample time

Reference time is the absolute time (in master-clock units) at which a sequence of messages is to be played. In user-mode implementations, it is passed to the [**IDirectMusicSynth::PlayBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536540) method when MIDI messages are fed to the synthesizer. The synthesizer, wave sink, and the rest of DirectMusic should all work under the same master clock, which is attached to the synthesizer by your implementation of the [**IDirectMusicSynth::SetMasterClock**](https://msdn.microsoft.com/library/windows/hardware/ff536543) method and to the wave sink by [**IDirectMusicSynthSink::SetMasterClock**](https://msdn.microsoft.com/library/windows/hardware/ff536528).

Sample time is used to measure offsets into the synthesizer's output buffer. This buffer is filled with wave samples, so sample time is relative to the sampling rate. For example, at a sampling rate of 22.1 kHz, each second of time is equivalent to 22,100 samples or 44,200 bytes (in the case of a 16-bit mono format).

Because the playback of the wave sample buffer is likely to be controlled by a different timing crystal than the master clock, reference time and sample time tend to drift apart. The wave sink keeps them in step by implementing a phase-locked loop. This clock synchronization is described in [Clock Synchronization](clock-synchronization.md).

This section also includes:

[Synthesizer Latency](synthesizer-latency.md)

[Time-Stamped Events](time-stamped-events.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Synthesizer%20Timing%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


