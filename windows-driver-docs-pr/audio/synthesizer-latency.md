---
Description: Synthesizer Latency
MS-HAID: 'audio.synthesizer\_latency'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Synthesizer Latency
---

# Synthesizer Latency


## <span id="synthesizer_latency"></span><span id="SYNTHESIZER_LATENCY"></span>


Another consideration in synthesizer timing is latency, which is the difference between the current time and the first time that a note can play. A MIDI message cannot be submitted to the synthesizer and rendered into the output buffer at the current sample time. Allowance should be made for data that has already been placed in the buffer but has not yet been streamed to the wave output device.

The wave sink therefore should implement a latency clock, which is an [**IReferenceClock**](wmformat.ireferenceclock) object (described in the Microsoft Windows SDK documentation). The latency clock's [**IReferenceClock::GetTime**](dshow.ireferenceclock_gettime) method retrieves the sample time up to which data has already been written to the buffer, and converts this to reference time relative to the master clock. The wave sink does conversions between reference and sample time with [**IDirectMusicSynthSink::SampleToRefTime**](audio.idirectmusicsynthsink_sampletoreftime) and [**IDirectMusicSynthSink::RefTimeToSample**](audio.idirectmusicsynthsink_reftimetosample), so in this case, the synth calls **IDirectMusicSynthSink::RefTimeToSample** to accomplish the conversion.

Latency time is all managed by the wave sink. Your implementation of the [**IDirectMusicSynthSink::GetLatencyClock**](audio.idirectmusicsynthsink_getlatencyclock) method should output a pointer to the latency clock, and this pointer must in turn be retrieved by [**IDirectMusicSynth::GetLatencyClock**](audio.idirectmusicsynth_getlatencyclock). The application uses the latency clock to determine the earliest point in time at which a MIDI message can be queued to play when it is passed to the synthesizer by calling the [**IDirectMusicSynth::PlayBuffer**](audio.idirectmusicsynth_playbuffer) method.

An example of the latency of a MIDI message is shown in the following figure.

![diagram illustrating latency of a midi message](images/dmclock.png)

In the preceding figure, the latency clock points to the first place in the PCM buffer loop where a note can be played. Note that the master clock is at 22 time units, which is the point where sound is currently playing from, but the space between 22 and 30 time units has already been filled with wave data and can no longer be written to. Therefore, the first place where a new time-stamped MIDI event can be scheduled to play is at time 30. Thus, the latency clock reads 30 time units.

Messages can be scheduled to play at, or any time after, this latency time. Therefore, messages that are to be rendered immediately are stamped with the latency time (not the current time) before being placed in the synthesizer's input buffer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Synthesizer%20Latency%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


