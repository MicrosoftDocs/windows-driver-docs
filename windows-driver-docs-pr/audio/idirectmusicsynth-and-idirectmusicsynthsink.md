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
ms.localizationpriority: medium
---

# IDirectMusicSynth and IDirectMusicSynthSink


## <span id="idirectmusicsynth_and_idirectmusicsynthsink"></span><span id="IDIRECTMUSICSYNTH_AND_IDIRECTMUSICSYNTHSINK"></span>


As described in [Synthesizers and Wave Sinks](synthesizers-and-wave-sinks.md), you can implement a custom software synthesizer or wave sink that runs in user mode and communicates with DirectMusic. The synthesizer object must have an [IDirectMusicSynth](/windows/win32/api/dmusics/nn-dmusics-idirectmusicsynth) interface. The wave sink object must have an [IDirectMusicSynthSink](/windows/win32/api/dmusics/nn-dmusics-idirectmusicsynthsink) interface.

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
<td align="left"><p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-activate" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Activate&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-activate)"><strong>IDirectMusicSynth::Activate</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Channels</p></td>
<td align="left"><p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getchannelpriority" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetChannelPriority&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getchannelpriority)"><strong>IDirectMusicSynth::GetChannelPriority</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-setchannelpriority" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::SetChannelPriority&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-setchannelpriority)"><strong>IDirectMusicSynth::SetChannelPriority</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Instruments</p></td>
<td align="left"><p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-download" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Download&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-download)"><strong>IDirectMusicSynth::Download</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-unload" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Unload&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-unload)"><strong>IDirectMusicSynth::Unload</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Information</p></td>
<td align="left"><p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getappend" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetAppend&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getappend)"><strong>IDirectMusicSynth::GetAppend</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getformat" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetFormat&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getformat)"><strong>IDirectMusicSynth::GetFormat</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getlatencyclock" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetLatencyClock&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getlatencyclock)"><strong>IDirectMusicSynth::GetLatencyClock</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getportcaps" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetPortCaps&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getportcaps)"><strong>IDirectMusicSynth::GetPortCaps</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getrunningstats" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::GetRunningStats&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-getrunningstats)"><strong>IDirectMusicSynth::GetRunningStats</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Playback</p></td>
<td align="left"><p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-playbuffer" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::PlayBuffer&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-playbuffer)"><strong>IDirectMusicSynth::PlayBuffer</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-render" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Render&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-render)"><strong>IDirectMusicSynth::Render</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Ports</p></td>
<td align="left"><p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-open" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Open&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-open)"><strong>IDirectMusicSynth::Open</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-close" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::Close&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-close)"><strong>IDirectMusicSynth::Close</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-setnumchannelgroups" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::SetNumChannelGroups&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-setnumchannelgroups)"><strong>IDirectMusicSynth::SetNumChannelGroups</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Miscellaneous parameters</p></td>
<td align="left"><p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-setmasterclock" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::SetMasterClock&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-setmasterclock)"><strong>IDirectMusicSynth::SetMasterClock</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-setsynthsink" data-raw-source="[&lt;strong&gt;IDirectMusicSynth::SetSynthSink&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynth-setsynthsink)"><strong>IDirectMusicSynth::SetSynthSink</strong></a></p></td>
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
<td align="left"><p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-activate" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::Activate&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-activate)"><strong>IDirectMusicSynthSink::Activate</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-getdesiredbuffersize" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::GetDesiredBufferSize&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-getdesiredbuffersize)"><strong>IDirectMusicSynthSink::GetDesiredBufferSize</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-init" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::Init&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-init)"><strong>IDirectMusicSynthSink::Init</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-setdirectsound" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::SetDirectSound&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-setdirectsound)"><strong>IDirectMusicSynthSink::SetDirectSound</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Timing</p></td>
<td align="left"><p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-getlatencyclock" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::GetLatencyClock&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-getlatencyclock)"><strong>IDirectMusicSynthSink::GetLatencyClock</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-reftimetosample" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::RefTimeToSample&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-reftimetosample)"><strong>IDirectMusicSynthSink::RefTimeToSample</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-sampletoreftime" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::SampleToRefTime&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-sampletoreftime)"><strong>IDirectMusicSynthSink::SampleToRefTime</strong></a></p>
<p><a href="/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-setmasterclock" data-raw-source="[&lt;strong&gt;IDirectMusicSynthSink::SetMasterClock&lt;/strong&gt;](/windows/win32/api/dmusics/nf-dmusics-idirectmusicsynthsink-setmasterclock)"><strong>IDirectMusicSynthSink::SetMasterClock</strong></a></p></td>
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

When a software synthesizer is first opened, DirectMusic gives the synthesizer a DMUS\_PORTPARAMS structure (described in the Microsoft Windows SDK documentation) that specifies the sample rate and number of channels for the audio output stream. The synthesizer then converts these into a standard [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) structure that it passes to the wave sink when the wave sink calls the **IDirectMusicSynth::GetFormat** method.

For additional information, see the descriptions of the **IDirectMusic** and **IDirectMusicPort** interfaces in the Windows SDK documentation.

