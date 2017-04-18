---
title: Policy for Mixing Audio Streams and Setting the Output Sample Rate
description: Policy for Mixing Audio Streams and Setting the Output Sample Rate
ms.assetid: b05875a8-ed6e-4e48-99ac-33fa22b7bc69
keywords: ["SRC WDK audio , output sample rate", "sample-rate conversion WDK audio , output sample rate", "output sample rate WDK audio", "connecting audio streams WDK", "KMixer system driver WDK audio , mixing policy", "mixing policy WDK audio", "input stream rate WDK audio"]
---

# Policy for Mixing Audio Streams and Setting the Output Sample Rate


## <span id="ddk_policy_for_mixing_audio_streams_and_setting_the_output_sample_rate"></span><span id="DDK_POLICY_FOR_MIXING_AUDIO_STREAMS_AND_SETTING_THE_OUTPUT_SAMPLE_RATE"></span>


This topic describes the algorithm that the KMixer system driver uses to generate an output mix that preserves as much of the audio quality in the input streams as it can without requiring any more processing for sample-rate conversion (SRC) and mixing than is necessary. The following three aspects of the algorithm are discussed:

-   Connecting the First Audio Stream

-   Connecting Additional Audio Streams

-   Handling Special Cases

### <span id="connecting_the_first_audio_stream"></span><span id="CONNECTING_THE_FIRST_AUDIO_STREAM"></span>Connecting the First Audio Stream

-   When the [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver) initializes the KMixer driver for an audio device, it assigns a sample rate corresponding to the higher of 44.1 kHz and the highest rate available on the audio device. (In Microsoft Windows XP SP1, Windows Server 2003, and later, the highest sample rate that KMixer supports is 200 kHz. In Windows 98/Me, Windows 2000, and Windows XP, KMixer's highest sample rate is 100 kHz.) Note that the miniport driver's request handler returns the sample rates available on the device (see [Pin Data-Range and Intersection Properties](pin-data-range-and-intersection-properties.md)).

-   When a client requests connection of an audio stream to a device, KMixer queries the device to determine whether it supports the incoming rate. If the device supports the incoming rate, KMixer passes the incoming stream to the device without SRC. Otherwise, KMixer maintains the current output rate, and does the following:
    -   If the device supports the current output rate, KMixer uses SRC to convert the input rate to the current output rate.
    -   If the device does not support the current output rate, KMixer maintains the current rate and fails the client's request to connect the audio stream to the device.

### <span id="connecting_additional_audio_streams"></span><span id="CONNECTING_ADDITIONAL_AUDIO_STREAMS"></span>Connecting Additional Audio Streams

Following connection of the first input stream, KMixer applies a different policy to the creation of connections by clients to any additional input streams. The following table describes the KMixer policy on rate conversion and mixing for these additional streams. The table lists the tests in the order in which KMixer performs them.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Rate Test</th>
<th align="left">Rate Conversion and Mixing Policy</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>New incoming rate is equal to the current output rate.</p></td>
<td align="left"><p>Perform mixing only.</p></td>
</tr>
<tr class="even">
<td align="left"><p>New incoming rate is equal to the rate of another input stream.</p></td>
<td align="left"><p>Mix the new input stream with the other input stream at the same rate to take advantage of the existing SRC from input to output.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>New incoming rate is lower than the current maximum input rate.</p></td>
<td align="left"><p>Do SRC to the current output rate and mix.</p></td>
</tr>
<tr class="even">
<td align="left"><p>New incoming rate is higher that the current maximum input rate.</p></td>
<td align="left"><p>If the hardware supports the new input rate:</p>
<ul>
<li><p>Change the current maximum output rate and the hardware rate to the new incoming rate.</p></li>
<li><p>Do SRC on all other streams to the new maximum output rate and mix them with the new stream. (When converting to the new maximum output rate, KMixer mixes together any input streams that happen to share the same sample rate before doing SRC on those streams.)</p></li>
</ul>
<p>If the hardware does not support the new input rate, maintain the current output rate and do SRC on the new incoming stream to the current maximum input rate.</p></td>
</tr>
</tbody>
</table>

 

### <span id="handling_special_cases"></span><span id="HANDLING_SPECIAL_CASES"></span>Handling Special Cases

-   KMixer does not adjust its output rate when a client makes an **IDirectSoundBuffer::SetFrequency** call on a DirectSound buffer. Instead, KMixer adjusts the output rate when the buffer is first played.

-   The Sound Blaster emulator ([SBEmul system driver](kernel-mode-wdm-audio-components.md#sbemul_system_driver)) makes dynamic adjustments to its sample rate. KMixer maintains an output rate greater than or equal to that of the Sound Blaster emulator.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Policy%20for%20Mixing%20Audio%20Streams%20and%20Setting%20the%20Output%20Sample%20Rate%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


