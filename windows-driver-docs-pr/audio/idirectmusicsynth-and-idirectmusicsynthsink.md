---
title: IDirectMusicSynth and IDirectMusicSynthSink
description: IDirectMusicSynth and IDirectMusicSynthSink
keywords:
- IDirectMusicSynth interface
- IDirectMusicSynthSink interface
- custom rendering in user mode WDK audio , interfaces
- user-mode synths WDK audio , interfaces
- custom wave sinks WDK audio
- wave sinks WDK audio , user-mode
- latency WDK audio , synthesizers
- master clocks WDK audio , synthesizers
- clocks WDK audio , synthesizers
- synthesizers WDK audio , interfaces
- custom synths WDK audio , interfaces
- DirectMusic custom rendering WDK audio , synthesizers
ms.date: 04/20/2017
---

# IDirectMusicSynth and IDirectMusicSynthSink

As described in [Synthesizers and Wave Sinks](synthesizers-and-wave-sinks.md), you can implement a custom software synthesizer or wave sink that runs in user mode and communicates with DirectMusic. The synthesizer object must have an IDirectMusicSynth interface. The wave sink object must have an IDirectMusicSynthSink interface.

DirectMusic communicates with a software synthesizer through its **IDirectMusicSynth** interface. DirectMusic supports this interface in DirectX 6.1 and later. **IDirectMusicSynth** supports the methods shown in the following table, which organizes the methods into functional groups.

| Group                    | Method Names                                                                                                                                                        |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activation               | IDirectMusicSynth::Activate                                                                                                                                         |
| Channels                 | IDirectMusicSynth::GetChannelPriority, IDirectMusicSynth::SetChannelPriority                                                                                        |
| Instruments              | IDirectMusicSynth::Download,  IDirectMusicSynth::Unload                                                                                                             |
| Information              | IDirectMusicSynth::GetAppend, IDirectMusicSynth::GetFormat, IDirectMusicSynth::GetLatencyClock, IDirectMusicSynth::GetPortCaps , IDirectMusicSynth::GetRunningStats |
| Playback                 | IDirectMusicSynth::PlayBuffer, IDirectMusicSynth::Render                                                                                                            |
| Ports                    | IDirectMusicSynth::Open, IDirectMusicSynth::Close, IDirectMusicSynth::SetNumChannelGroups                                                                           |
| Miscellaneous parameters | IDirectMusicSynth::SetMasterClock, IDirectMusicSynth::SetSynthSink                                                                                                  |

Most applications do not need to call the methods in the **IDirectMusicSynth** interface directly; the DirectMusic port typically manages the synthesizer. However, your application can interface directly to the synthesizer during development and testing.

The synthesizer is not complete without a connection to a wave sink, which is represented as an object with an **IDirectMusicSynthSink** interface. The wave sink connects the synthesizer's audio output stream to an audio rendering module such as DirectSound, DirectShow, or the Windows Multimedia **waveOut** API.

By default, DirectMusic uses its internal **IDirectMusicSynthSink** implementation to handle the wave data that the software synthesizer generates. This wave sink feeds the data to DirectSound.

Before the synthesizer can be activated, a wave sink must first be created and connected to the synthesizer via a call to **IDirectMusicSynth::SetSynthSink**. This should be the very first call after creating the synthesizer because many of the timing-related calls, including **IDirectMusicSynth::GetLatencyClock** and **IDirectMusicSynth::SetMasterClock**, are actually passed through to equivalent calls on **IDirectMusicSynthSink**.

Only DirectX 6.1 and DirectX 7 support the implementation of a custom user-mode wave sink with an **IDirectMusicSynthSink** interface. **IDirectMusicSynthSink** supports the methods shown in the following table, which organizes the methods into functional groups.

|Group|Method Names|
|---- |----------- |
|Initialization|IDirectMusicSynthSink::Activate, IDirectMusicSynthSink::GetDesiredBufferSize
IDirectMusicSynthSink::Init, IDirectMusicSynthSink::SetDirectSound|
|Timing|IDirectMusicSynthSink::GetLatencyClock, IDirectMusicSynthSink::RefTimeToSample
IDirectMusicSynthSink::SampleToRefTime, IDirectMusicSynthSink::SetMasterClock|

In DirectX 8 and later, DirectMusic always uses its internal wave sink with a user-mode synthesizer. These later versions of DirectMusic do not support custom implementations of **IDirectMusicSynthSink**.

In DirectX 6.1 and DirectX 7, however, you are free to implement your own **IDirectMusicSynthSink** object and use it to manage the synthesizer's audio output stream in any way you like. For example, you might feed the wave data into DirectShow or the **waveOut** API. If you create a wave stream object, it must have an **IDirectMusicSynthSink** interface to plug into the **IDirectMusicSynth** object.

In addition to managing the wave stream, the wave sink is responsible for controlling the timing for the synthesizer. The wave sink receives the master clock by a call to **IDirectMusicSynth::SetMasterClock**, which passes the master time source on with an identical call to **IDirectMusicSynthSink::SetMasterClock**. Because the master clock is not generated from the same crystal as the wave stream, the wave sink must keep them synchronized by compensating for clock drift.

Additionally, so that the synthesizer can keep track of time appropriately, it provides two calls to convert from master clock time to sample time and back:

- **IDirectMusicSynthSink::RefTimeToSample**

- **IDirectMusicSynthSink::SampleToRefTime**

The wave sink generates the latency clock because it actually manages the times at which samples get written by calls to **IDirectMusicSynth::Render**. When DirectMusic calls **IDirectMusicSynth::GetLatencyClock** on the DirectMusic port, it simply turns around and calls **IDirectMusicSynthSink::GetLatencyClock**.

When a software synthesizer is first opened, DirectMusic gives the synthesizer a DMUS\_PORTPARAMS structure (described in the Microsoft Windows SDK documentation) that specifies the sample rate and number of channels for the audio output stream. The synthesizer then converts these into a standard [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) structure that it passes to the wave sink when the wave sink calls the **IDirectMusicSynth::GetFormat** method.

For additional information, see the descriptions of the **IDirectMusic** and **IDirectMusicPort** interfaces in the Windows SDK documentation.
