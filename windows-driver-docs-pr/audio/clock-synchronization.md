---
title: Clock Synchronization
description: Clock Synchronization
ms.assetid: dc0071b0-a22c-4bb5-90ea-a69e5dcdba6f
keywords:
- synthesizers WDK audio , clock synchronization
- clocks WDK audio , synchronization
- latency WDK audio , clocks
- time WDK audio
- reference clocks WDK audio
- sample clocks WDK audio
- wave sinks WDK audio , clock synchronization
- offset time WDK audio
- master clocks WDK audio , synchronization
- phase-locked loops WDK audio
- synchronization WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Clock Synchronization


## <span id="clock_synchronization"></span><span id="CLOCK_SYNCHRONIZATION"></span>


A critical task for the wave sink to do is to resolve time drift between the reference-clock and sample-clock crystals. It does this with the software equivalent of a phase-locked loop.

The wave sink keeps track of what sample number in the buffer it can write to next. So even though it knows that it is on, for example, sample 20, the wave sink still needs to check the master clock to get a reference time. It has a thread that wakes up approximately every 20 milliseconds and asks the master clock for the current time. The master clock might report back that the current time (in milliseconds) is 420, for example.

The wave sink also maintains a latency clock, which shows the offset between the current time according to the master clock and the sample time. It uses this information to calculate the expected master clock time and compares this with the actual master clock reading to see if the two clocks have drifted apart.

The wave sink uses a phase-locked loop to adjust the sample time. When checking for drift, the wave sink does not adjust by the whole amount, because the readings contain some jitter. Instead, it moves the sample clock by some fraction of the distance toward the master clock. In this way, the wave sink smoothes out jitter errors while staying roughly in sync. It also takes this time and converts it to a latency clock time that is relative to the master clock. This is important because the application might need to know where the synthesizer is rendering at any point.

The latency clock tells the application the earliest time at which a new note can be scheduled to play. The latency clock time is the master clock time plus an offset that represents the synthesizer's latency. This latency represents the minimum delay from the time that the application submits a new note to be played to the time that the synthesizer actually plays the note. At any instant, the application can schedule a note to be played at or later than--but no earlier than--the current latency clock time.

For example, if the master clock is currently at time 420 and the application has a note that it wants to play as soon as possible, the latency clock tells it the earliest time that the note can be played. If the software synthesizer has a latency of 100 milliseconds, the next time it can play a note is at time 520.

Suppose an event is marked to play at time 520 in reference time. The synthesizer does its work by rendering notes down into samples and performing all its calculations in sample time. Therefore, it needs to know what a reference time of 520 converts to in sample time. In user mode, the wave sink provides two functions that the synth uses:

[**IDirectMusicSynthSink::SampleToRefTime**](https://msdn.microsoft.com/library/windows/hardware/ff536526)

[**IDirectMusicSynthSink::RefTimeToSample**](https://msdn.microsoft.com/library/windows/hardware/ff536525)

To do the conversion in this case, the synth calls **IDirectMusicSynthSink::RefTimeToSample** on the wave sink.

The wave sink then gives back a sample time (for example, 600). The note in question gets rendered at sample time 600. Then, when the synth [**IDirectMusicSynth::Render**](https://msdn.microsoft.com/library/windows/hardware/ff536541) method gets called by the wave sink to render the next portion of the stream (for example, from sample time 600 to 800), the note is rendered into the buffer at sample time 600.

**Note**   The sample time is kept as a 64-bit number to avoid rollover. (A DWORD value rolls over in 27 hours.)

 

To summarize, the synth does all its internal math in sample time and the wave sink does the conversion to sample time from reference time and vice versa. The wave sink also manages synchronization with the master clock and provides latency information. Hiding this functionality in the wave sink makes writing the synth easier.

 

 




