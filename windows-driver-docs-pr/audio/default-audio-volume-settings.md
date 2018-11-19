---
title: Default Audio Volume Settings
description: Default Audio Volume Settings
ms.assetid: 5d694aa2-5a47-44c5-92d5-ec8c4885820f
keywords:
- audio adapters WDK , volume settings
- adapter drivers WDK audio , volume settings
- Port Class audio adapters WDK , volume settings
- default volume settings
- audio volume settings WDK
- master volume slider WDK audio
- volume sliders WDK audio
- sound level settings WDK audio
- master-volume settings WDK audio
- default master-volume settings
- full-volume sliders WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Default Audio Volume Settings


## <span id="default_audio_volume_settings"></span><span id="DEFAULT_AUDIO_VOLUME_SETTINGS"></span>


The SndVol program (see [SysTray and SndVol32](systray-and-sndvol32.md)) displays a set of volume sliders. The sliders indicate the volume-level settings for the various audio devices and applications such as speakers and system sounds. There is an endpoint volume for each audio output and input, and an application volume for each application. The audio driver has control only over its own endpoint volumes, via KSPROPERTY\_AUDIO\_VOLUMELEVEL. If the driver does not explicitly initialize these volume settings at the time that it is installed, the operating system chooses its own default values for these settings. The defaults that the operating system chooses are not the same across all Windows releases, and vendors might need to take these differences into account to ensure that the volume levels are set neither too high nor too low immediately following driver installation.

As a general rule, if the audio adapter drives a set of analog speakers that have their own physical volume control, the INF file should not set the default volume level too low. Otherwise, a user might try to compensate by increasing the volume on the speakers instead of increasing the master volume on the sound card. The result of amplifying a low signal level is loss of audio quality.

If the audio adapter does not have a hardware amplifier, see [Software Volume Control Support](software-volume-control-support.md) for information about the software support provided.

**Note**  If there is a hardware amplifier, then the driver sets the range and the default level via the [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff537309) kernel streaming property. If there is not a hardware amplifier, Windows will create a software volume control APO.
If there is a physical volume knob on an active set of speakers, it should appear to Windows as a HID control. This will function similarly to the volume up and volume down buttons on a keyboard; Windows will see the volume knob turn and will program the volume control correspondingly (whether it is a hardware or software volume.)

 

Ideally, if a set of active speakers ships in the same box with the audio adapter card, the factory should adjust the volume knob on the speakers to the position that works best with the adapter's default volume setting. If the audio adapter does not have a physical volume control knob, see the [Software Volume Control Support](https://msdn.microsoft.com/library/windows/hardware/ff539263) topic for information about the software support provided by Windows.

**Note**  If the audio hardware exposes a hardware volume control (like a volume knob), then the driver sets the range and the default level via the [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff537309) Kernel Streaming property.

 

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
For information about the operational characteristics of the physical volume sliders that are represented by the software volume sliders in Windows applications, see [Audio-Tapered Volume Controls](https://msdn.microsoft.com/library/windows/desktop/dd370798.aspx).

## <span id="related_topics"></span>Related topics
[Customizing Default Audio Volume Settings](customizing-default-audio-volume-settings.md)  



