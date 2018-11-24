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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




