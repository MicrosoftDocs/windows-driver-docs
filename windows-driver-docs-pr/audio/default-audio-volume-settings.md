---
Description: Default Audio Volume Settings
MS-HAID: 'audio.default\_audio\_volume\_settings'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Default Audio Volume Settings
---

# Default Audio Volume Settings


## <span id="default_audio_volume_settings"></span><span id="DEFAULT_AUDIO_VOLUME_SETTINGS"></span>


The SndVol program (see [SysTray and SndVol32](systray-and-sndvol32.md)) displays a set of volume sliders. The sliders indicate the volume-level settings for the various audio devices and applications such such as speakers and system sounds. There is an endpoint volume for each audio output and input, and an application volume for each application. The audio driver has control only over its own endpoint volumes, via KSPROPERTY\_AUDIO\_VOLUMELEVEL. If the driver does not explicitly initialize these volume settings at the time that it is installed, the operating system chooses its own default values for these settings. The defaults that the operating system chooses are not the same across all Windows releases, and vendors might need to take these differences into account to ensure that the volume levels are set neither too high nor too low immediately following driver installation.

As a general rule, if the audio adapter drives a set of analog speakers that have their own physical volume control, the INF file should not set the default volume level too low. Otherwise, a user might try to compensate by increasing the volume on the speakers instead of increasing the master volume on the sound card. The result of amplifying a low signal level is loss of audio quality.

If the audio adapter does not have a hardware amplifier, see [Software Volume Control Support](software-volume-control-support.md) for information about the software support provided.

**Note**  If there is a hardware amplifier, then the driver sets the range and the default level via the [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](audio.ksproperty_audio_volumelevel) kernel streaming property. If there is not a hardware amplifier, Windows will create a software volume control APO.
If there is a physical volume knob on an active set of speakers, it should appear to Windows as a HID control. This will function similarly to the volume up and volume down buttons on a keyboard; Windows will see the volume knob turn and will program the volume control correspondingly (whether it is a hardware or software volume.)

 

Ideally, if a set of active speakers ships in the same box with the audio adapter card, the factory should adjust the volume knob on the speakers to the position that works best with the adapter's default volume setting. If the audio adapter does not have a physical volume control knob, see the [Software Volume Control Support](audio.windows_vista_software_volume_control_support) topic for information about the software support provided by Windows.

**Note**  If the audio hardware exposes a hardware volume control (like a volume knob), then the driver sets the range and the default level via the [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](audio.ksproperty_audio_volumelevel) Kernel Streaming property.

 

The following table shows the volume ranges and default volume levels for audio in the different versions of Windows.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Windows version</th>
<th align="left">Microphone default values</th>
<th align="left">Non-microphone* default values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Windows Vista SP1</td>
<td align="left"><p>Default level: 0.0db</p>
<p>Volume Range : -192.0 dB ~ +12.0dB</p></td>
<td align="left"><p>Default level: 0.0db</p>
<p>Volume Range : -192.0 dB ~ 0dB</p></td>
</tr>
<tr class="even">
<td align="left">Windows 7</td>
<td align="left"><p>Default level: +30.0dB</p>
<p>Volume Range : -192 dB ~ +30.0 dB</p></td>
<td align="left"><p>Default level: 0 dB</p>
<p>Volume Range : -192 dB ~ 0 dB</p></td>
</tr>
<tr class="odd">
<td align="left">Windows 8</td>
<td align="left"><p>Default level: 0.0 dB</p>
<p>Volume Range: -96 dB ~ +30 dB</p></td>
<td align="left"><p>Default level: 0.0 dB</p>
<p>Volume Range: -96 dB ~ 0 dB</p></td>
</tr>
</tbody>
</table>

 

\*The term non-microphone describes all playback devices and recording devices other than microphones.
For information about the operational characteristics of the physical volume sliders that are represented by the software volume sliders in Windows applications, see [Audio-Tapered Volume Controls](http://msdn.microsoft.com/en-us/library/windows/desktop/dd370798.aspx).

## <span id="related_topics"></span>Related topics
[Customizing Default Audio Volume Settings](customizing-default-audio-volume-settings.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Default%20Audio%20Volume%20Settings%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


