---
title: Translating Speaker-Configuration Requests
description: Translating Speaker-Configuration Requests
ms.assetid: be3dce30-7395-4332-ba62-de9a718b62f5
keywords:
- translating speaker-configuration requests WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Translating Speaker-Configuration Requests


## <span id="translating_speaker_configuration_requests"></span><span id="TRANSLATING_SPEAKER_CONFIGURATION_REQUESTS"></span>


**Note**  This information applies to Windows XP and earlier operating systems. Starting with Windows Vista, **IDirectSound::GetSpeakerConfig** and **IDirectSound::SetSpeakerConfig** have been deprecated.

 

When an application calls **IDirectSound::SetSpeakerConfig** (see Microsoft Windows SDK documentation) to change the speaker configuration, DirectSound translates the specified DSSPEAKER\_*Xxx* speaker-configuration parameter to the equivalent KSAUDIO\_*Xxx* channel-configuration mask. It sends a [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537250) set-property request containing this mask to the filter that represents the DirectSound device.

In the following table, each DSSPEAKER\_*Xxx* parameter on the left is paired with the equivalent KSAUDIO\_*Xxx* channel-configuration mask on the right.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DSSPEAKER Parameter</th>
<th align="left">KSAUDIO Channel-Configuration Mask</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DSSPEAKER_DIRECTOUT</p></td>
<td align="left"><p>KSAUDIO_SPEAKER_DIRECTOUT</p></td>
</tr>
<tr class="even">
<td align="left"><p>DSSPEAKER_HEADPHONE</p></td>
<td align="left"><p>KSAUDIO_SPEAKER_STEREO</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DSSPEAKER_MONO</p></td>
<td align="left"><p>KSAUDIO_SPEAKER_MONO</p></td>
</tr>
<tr class="even">
<td align="left"><p>DSSPEAKER_STEREO</p></td>
<td align="left"><p>KSAUDIO_SPEAKER_STEREO</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DSSPEAKER_QUAD</p></td>
<td align="left"><p>KSAUDIO_SPEAKER_QUAD</p></td>
</tr>
<tr class="even">
<td align="left"><p>DSSPEAKER_SURROUND</p></td>
<td align="left"><p>KSAUDIO_SPEAKER_SURROUND</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DSSPEAKER_5POINT1</p></td>
<td align="left"><p>KSAUDIO_SPEAKER_5POINT1</p></td>
</tr>
<tr class="even">
<td align="left"><p>DSSPEAKER_7POINT1</p></td>
<td align="left"><p>KSAUDIO_SPEAKER_7POINT1</p></td>
</tr>
</tbody>
</table>

 

In the preceding table, DirectSound specifies both its headphone and stereo speaker configurations with the same channel mask, KSAUDIO\_SPEAKER\_STEREO. To distinguish between these two configurations, DirectSound sends the filter a second set-property request, which specifies a speaker geometry (see [**KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY**](https://msdn.microsoft.com/library/windows/hardware/ff537305)). To indicate headphones, DirectSound passes the value KSAUDIO\_STEREO\_SPEAKER\_GEOMETRY\_HEADPHONE with the speaker-geometry request.

In the case of stereo speakers, however, the caller to **SetSpeakerConfig** can specify one of several possible DSSPEAKER\_*Xxx* stereo-speaker geometries. These appear in the left column of the following table, and the equivalent KSAUDIO\_*Xxx* parameters appear on the right.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DSSPEAKER Stereo-Speaker Geometry</th>
<th align="left">KSAUDIO Stereo-Speaker Geometry</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DSSPEAKER_GEOMETRY_WIDE</p></td>
<td align="left"><p>KSAUDIO_STEREO_SPEAKER_GEOMETRY_WIDE</p></td>
</tr>
<tr class="even">
<td align="left"><p>DSSPEAKER_GEOMETRY_NARROW</p></td>
<td align="left"><p>KSAUDIO_STEREO_SPEAKER_GEOMETRY_NARROW</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DSSPEAKER_GEOMETRY_MIN</p></td>
<td align="left"><p>KSAUDIO_STEREO_SPEAKER_GEOMETRY_MIN</p></td>
</tr>
<tr class="even">
<td align="left"><p>DSSPEAKER_GEOMETRY_MAX</p></td>
<td align="left"><p>KSAUDIO_STEREO_SPEAKER_GEOMETRY_MAX</p></td>
</tr>
</tbody>
</table>

 

If the caller does not explicitly specify one of the geometries in the left column above, DirectSound assumes DSSPEAKER\_GEOMETRY\_WIDE by default.

 

 




