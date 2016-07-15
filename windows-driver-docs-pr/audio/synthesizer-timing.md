---
Description: Synthesizer Timing
MS-HAID: 'audio.synthesizer\_timing'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Synthesizer Timing
---

# Synthesizer Timing


## <span id="synthesizer_timing"></span><span id="SYNTHESIZER_TIMING"></span>


The synthesizer works with two different systems of time:

-   Reference time

-   Sample time

Reference time is the absolute time (in master-clock units) at which a sequence of messages is to be played. In user-mode implementations, it is passed to the [**IDirectMusicSynth::PlayBuffer**](audio.idirectmusicsynth_playbuffer) method when MIDI messages are fed to the synthesizer. The synthesizer, wave sink, and the rest of DirectMusic should all work under the same master clock, which is attached to the synthesizer by your implementation of the [**IDirectMusicSynth::SetMasterClock**](audio.idirectmusicsynth_setmasterclock) method and to the wave sink by [**IDirectMusicSynthSink::SetMasterClock**](audio.idirectmusicsynthsink_setmasterclock).

Sample time is used to measure offsets into the synthesizer's output buffer. This buffer is filled with wave samples, so sample time is relative to the sampling rate. For example, at a sampling rate of 22.1 kHz, each second of time is equivalent to 22,100 samples or 44,200 bytes (in the case of a 16-bit mono format).

Because the playback of the wave sample buffer is likely to be controlled by a different timing crystal than the master clock, reference time and sample time tend to drift apart. The wave sink keeps them in step by implementing a phase-locked loop. This clock synchronization is described in [Clock Synchronization](clock-synchronization.md).

This section also includes:

[Synthesizer Latency](synthesizer-latency.md)

[Time-Stamped Events](time-stamped-events.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Synthesizer%20Timing%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


