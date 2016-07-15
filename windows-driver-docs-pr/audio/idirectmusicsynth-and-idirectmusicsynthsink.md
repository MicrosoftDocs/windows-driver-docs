---
Description: IDirectMusicSynth and IDirectMusicSynthSink
MS-HAID: 'audio.idirectmusicsynth\_and\_idirectmusicsynthsink'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: IDirectMusicSynth and IDirectMusicSynthSink
---

# IDirectMusicSynth and IDirectMusicSynthSink


## <span id="idirectmusicsynth_and_idirectmusicsynthsink"></span><span id="IDIRECTMUSICSYNTH_AND_IDIRECTMUSICSYNTHSINK"></span>


As described in [Synthesizers and Wave Sinks](synthesizers-and-wave-sinks.md), you can implement a custom software synthesizer or wave sink that runs in user mode and communicates with DirectMusic. The synthesizer object must have an [IDirectMusicSynth](audio.idirectmusicsynth) interface. The wave sink object must have an [IDirectMusicSynthSink](audio.idirectmusicsynthsink) interface.

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
<td align="left"><p>[<strong>IDirectMusicSynth::Activate</strong>](audio.idirectmusicsynth_activate)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Channels</p></td>
<td align="left"><p>[<strong>IDirectMusicSynth::GetChannelPriority</strong>](audio.idirectmusicsynth_getchannelpriority)</p>
<p>[<strong>IDirectMusicSynth::SetChannelPriority</strong>](audio.idirectmusicsynth_setchannelpriority)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Instruments</p></td>
<td align="left"><p>[<strong>IDirectMusicSynth::Download</strong>](audio.idirectmusicsynth_download)</p>
<p>[<strong>IDirectMusicSynth::Unload</strong>](audio.idirectmusicsynth_unload)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Information</p></td>
<td align="left"><p>[<strong>IDirectMusicSynth::GetAppend</strong>](audio.idirectmusicsynth_getappend)</p>
<p>[<strong>IDirectMusicSynth::GetFormat</strong>](audio.idirectmusicsynth_getformat)</p>
<p>[<strong>IDirectMusicSynth::GetLatencyClock</strong>](audio.idirectmusicsynth_getlatencyclock)</p>
<p>[<strong>IDirectMusicSynth::GetPortCaps</strong>](audio.idirectmusicsynth_getportcaps)</p>
<p>[<strong>IDirectMusicSynth::GetRunningStats</strong>](audio.idirectmusicsynth_getrunningstats)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Playback</p></td>
<td align="left"><p>[<strong>IDirectMusicSynth::PlayBuffer</strong>](audio.idirectmusicsynth_playbuffer)</p>
<p>[<strong>IDirectMusicSynth::Render</strong>](audio.idirectmusicsynth_render)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Ports</p></td>
<td align="left"><p>[<strong>IDirectMusicSynth::Open</strong>](audio.idirectmusicsynth_open)</p>
<p>[<strong>IDirectMusicSynth::Close</strong>](audio.idirectmusicsynth_close)</p>
<p>[<strong>IDirectMusicSynth::SetNumChannelGroups</strong>](audio.idirectmusicsynth_setnumchannelgroups)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Miscellaneous parameters</p></td>
<td align="left"><p>[<strong>IDirectMusicSynth::SetMasterClock</strong>](audio.idirectmusicsynth_setmasterclock)</p>
<p>[<strong>IDirectMusicSynth::SetSynthSink</strong>](audio.idirectmusicsynth_setsynthsink)</p></td>
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
<td align="left"><p>[<strong>IDirectMusicSynthSink::Activate</strong>](audio.idirectmusicsynthsink_activate)</p>
<p>[<strong>IDirectMusicSynthSink::GetDesiredBufferSize</strong>](audio.idirectmusicsynthsink_getdesiredbuffersize)</p>
<p>[<strong>IDirectMusicSynthSink::Init</strong>](audio.idirectmusicsynthsink_init)</p>
<p>[<strong>IDirectMusicSynthSink::SetDirectSound</strong>](audio.idirectmusicsynthsink_setdirectsound)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Timing</p></td>
<td align="left"><p>[<strong>IDirectMusicSynthSink::GetLatencyClock</strong>](audio.idirectmusicsynthsink_getlatencyclock)</p>
<p>[<strong>IDirectMusicSynthSink::RefTimeToSample</strong>](audio.idirectmusicsynthsink_reftimetosample)</p>
<p>[<strong>IDirectMusicSynthSink::SampleToRefTime</strong>](audio.idirectmusicsynthsink_sampletoreftime)</p>
<p>[<strong>IDirectMusicSynthSink::SetMasterClock</strong>](audio.idirectmusicsynthsink_setmasterclock)</p></td>
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

When a software synthesizer is first opened, DirectMusic gives the synthesizer a DMUS\_PORTPARAMS structure (described in the Microsoft Windows SDK documentation) that specifies the sample rate and number of channels for the audio output stream. The synthesizer then converts these into a standard [**WAVEFORMATEX**](audio.waveformatex) structure that it passes to the wave sink when the wave sink calls the **IDirectMusicSynth::GetFormat** method.

For additional information, see the descriptions of the **IDirectMusic** and **IDirectMusicPort** interfaces in the Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20IDirectMusicSynth%20and%20IDirectMusicSynthSink%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


