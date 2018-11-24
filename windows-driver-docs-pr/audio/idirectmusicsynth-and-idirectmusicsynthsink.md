---
title: IDirectMusicSynth and IDirectMusicSynthSink
description: IDirectMusicSynth and IDirectMusicSynthSink
ms.assetid: ce9a353b-9e4b-402b-92bb-948200e3c2ef
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
ms.localizationpriority: medium
---

# IDirectMusicSynth and IDirectMusicSynthSink


## <span id="idirectmusicsynth_and_idirectmusicsynthsink"></span><span id="IDIRECTMUSICSYNTH_AND_IDIRECTMUSICSYNTHSINK"></span>


As described in [Synthesizers and Wave Sinks](synthesizers-and-wave-sinks.md), you can implement a custom software synthesizer or wave sink that runs in user mode and communicates with DirectMusic. The synthesizer object must have an [IDirectMusicSynth](https://msdn.microsoft.com/library/windows/hardware/ff536519) interface. The wave sink object must have an [IDirectMusicSynthSink](https://msdn.microsoft.com/library/windows/hardware/ff536520) interface.

DirectMusic communicates with a software synthesizer through its **IDirectMusicSynth** interface. DirectMusic supports this interface in DirectX 6.1 and later. **IDirectMusicSynth** supports the methods shown in the following table, which organizes the methods into functional groups.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Group</th>
<th align="left">Method Names</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Activation</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536529" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Activate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536529)"><strong>IDirectMusicSynth::Activate</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Channels</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536534" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetChannelPriority&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536534)"><strong>IDirectMusicSynth::GetChannelPriority</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536542" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::SetChannelPriority&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536542)"><strong>IDirectMusicSynth::SetChannelPriority</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Instruments</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536532" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Download&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536532)"><strong>IDirectMusicSynth::Download</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536546" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Unload&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536546)"><strong>IDirectMusicSynth::Unload</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Information</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536533" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetAppend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536533)"><strong>IDirectMusicSynth::GetAppend</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536535" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetFormat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536535)"><strong>IDirectMusicSynth::GetFormat</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536536" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetLatencyClock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536536)"><strong>IDirectMusicSynth::GetLatencyClock</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536537" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetPortCaps&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536537)"><strong>IDirectMusicSynth::GetPortCaps</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536538" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetRunningStats&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536538)"><strong>IDirectMusicSynth::GetRunningStats</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Playback</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536540" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::PlayBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536540)"><strong>IDirectMusicSynth::PlayBuffer</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536541" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Render&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536541)"><strong>IDirectMusicSynth::Render</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Ports</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536539" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Open&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536539)"><strong>IDirectMusicSynth::Open</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536531" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Close&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536531)"><strong>IDirectMusicSynth::Close</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536544" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::SetNumChannelGroups&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536544)"><strong>IDirectMusicSynth::SetNumChannelGroups</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Miscellaneous parameters</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536543" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::SetMasterClock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536543)"><strong>IDirectMusicSynth::SetMasterClock</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536545" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::SetSynthSink&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536545)"><strong>IDirectMusicSynth::SetSynthSink</strong></a></p></td>
</tr>
</tbody>
</table>

 

Most applications do not need to call the methods in the **IDirectMusicSynth** interface directly; the DirectMusic port typically manages the synthesizer. However, your application can interface directly to the synthesizer during development and testing.

The synthesizer is not complete without a connection to a wave sink, which is represented as an object with an **IDirectMusicSynthSink** interface. The wave sink connects the synthesizer's audio output stream to an audio rendering module such as DirectSound, DirectShow, or the Windows Multimedia **waveOut** API.

By default, DirectMusic uses its internal **IDirectMusicSynthSink** implementation to handle the wave data that the software synthesizer generates. This wave sink feeds the data to DirectSound.

Before the synthesizer can be activated, a wave sink must first be created and connected to the synthesizer via a call to **IDirectMusicSynth::SetSynthSink**. This should be the very first call after creating the synthesizer because many of the timing-related calls, including **IDirectMusicSynth::GetLatencyClock** and **IDirectMusicSynth::SetMasterClock**, are actually passed through to equivalent calls on **IDirectMusicSynthSink**.

Only DirectX 6.1 and DirectX 7 support the implementation of a custom user-mode wave sink with an **IDirectMusicSynthSink** interface. **IDirectMusicSynthSink** supports the methods shown in the following table, which organizes the methods into functional groups.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Group</th>
<th align="left">Method Names</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Initialization</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536521" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::Activate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536521)"><strong>IDirectMusicSynthSink::Activate</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536522" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::GetDesiredBufferSize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536522)"><strong>IDirectMusicSynthSink::GetDesiredBufferSize</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536524" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::Init&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536524)"><strong>IDirectMusicSynthSink::Init</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536527" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::SetDirectSound&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536527)"><strong>IDirectMusicSynthSink::SetDirectSound</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Timing</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536523" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::GetLatencyClock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536523)"><strong>IDirectMusicSynthSink::GetLatencyClock</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536525" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::RefTimeToSample&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536525)"><strong>IDirectMusicSynthSink::RefTimeToSample</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536526" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::SampleToRefTime&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536526)"><strong>IDirectMusicSynthSink::SampleToRefTime</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536528" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::SetMasterClock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536528)"><strong>IDirectMusicSynthSink::SetMasterClock</strong></a></p></td>
</tr>
</tbody>
</table>

 

In DirectX 8 and later, DirectMusic always uses its internal wave sink with a user-mode synthesizer. These later versions of DirectMusic do not support custom implementations of **IDirectMusicSynthSink**.

In DirectX 6.1 and DirectX 7, however, you are free to implement your own **IDirectMusicSynthSink** object and use it to manage the synthesizer's audio output stream in any way you like. For example, you might feed the wave data into DirectShow or the **waveOut** API. If you create a wave stream object, it must have an **IDirectMusicSynthSink** interface to plug into the **IDirectMusicSynth** object.

In addition to managing the wave stream, the wave sink is responsible for controlling the timing for the synthesizer. The wave sink receives the master clock by a call to **IDirectMusicSynth::SetMasterClock**, which passes the master time source on with an identical call to **IDirectMusicSynthSink::SetMasterClock**. Because the master clock is not generated from the same crystal as the wave stream, the wave sink must keep them synchronized by compensating for clock drift.

Additionally, so that the synthesizer can keep track of time appropriately, it provides two calls to convert from master clock time to sample time and back:

-   **IDirectMusicSynthSink::RefTimeToSample**

-   **IDirectMusicSynthSink::SampleToRefTime**

The wave sink generates the latency clock because it actually manages the times at which samples get written by calls to **IDirectMusicSynth::Render**. When DirectMusic calls **IDirectMusicSynth::GetLatencyClock** on the DirectMusic port, it simply turns around and calls **IDirectMusicSynthSink::GetLatencyClock**.

When a software synthesizer is first opened, DirectMusic gives the synthesizer a DMUS\_PORTPARAMS structure (described in the Microsoft Windows SDK documentation) that specifies the sample rate and number of channels for the audio output stream. The synthesizer then converts these into a standard [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) structure that it passes to the wave sink when the wave sink calls the **IDirectMusicSynth::GetFormat** method.

For additional information, see the descriptions of the **IDirectMusic** and **IDirectMusicPort** interfaces in the Windows SDK documentation.

 

 




