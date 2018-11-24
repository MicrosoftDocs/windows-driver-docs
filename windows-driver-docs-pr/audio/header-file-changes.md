---
title: Header File Changes
description: Header File Changes
ms.assetid: 9212aa8d-bb11-4ade-a70c-274a7ffe83ef
keywords:
- data formats WDK audio
- formats WDK audio , data
- audio data formats WDK
- formats WDK audio , multichannel
- multichannel formats WDK audio
- home-theater systems WDK audio
- speakers WDK audio , home-threater systems
- audio drivers WDK , home-theater systems
- WDM audio drivers WDK , home-theater systems
- 7.1 home theater speakers WDK audio
- 7.1 wide configuration speakers WDK audio
- wide configuration speakers WDK audio
- 5.1 surround sound speakers WDK audio
- surround sound speakers WDK audio
- header files WDK audio
- Ksmedia.h
- Dsound.h
- channel masks WDK audio
- positions WDK audio
- WDM audio data formats WDK
- data formats WDK audio , header files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Header File Changes


The Windows Driver Kit (WDK) contains two header files that define the speaker configurations that are supported by the Windows multimedia control panel:

-   Ksmedia.h defines the channel masks for the [**KSAUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537083) structure that is used by the [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537250) property request.

-   Dsound.h defines a list of speaker-configuration identifiers that can be submitted to the **IDirectSound::SetSpeakerConfig** method. For more information about this method, see the Windows SDK documentation.

In Windows Server 2003, Windows XP with SP1, Windows 2000, and Windows Me/98, Ksmedia.h defines the channel masks that are shown in the following table for 5.1- and 7.1-channel streams.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter name</th>
<th align="left">Channel mask</th>
<th align="left">Speaker positions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>KSAUDIO_SPEAKER_5POINT1</p></td>
<td align="left"><p>0x3F</p></td>
<td align="left"><p>FL, FR, FC, LFE, BL, BR</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSAUDIO_SPEAKER_7POINT1</p></td>
<td align="left"><p>0xFF</p></td>
<td align="left"><p>FL, FR, FC, LFE, BL, BR, FLC, FRC</p></td>
</tr>
</tbody>
</table>

 

The two channel masks in the preceding table represent the 5.1 speaker configuration and the 7.1 speaker configuration. To identify the same two speaker configurations, Dsound.h defines the following speaker-configuration IDs:

```cpp
  #define DSSPEAKER_5POINT1      0x00000006
  #define DSSPEAKER_7POINT1      0x00000007
```

In Windows XP with SP2 and later versions of Windows, Ksmedia.h defines the channel masks shown in the following table for 5.1- and 7.1-channel streams.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter name</th>
<th align="left">Channel mask</th>
<th align="left">Speaker positions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>KSAUDIO_SPEAKER_5POINT1</p></td>
<td align="left"><p>0x3F</p></td>
<td align="left"><p>FL, FR, FC, LFE, BL, BR</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSAUDIO_SPEAKER_7POINT1_SURROUND</p></td>
<td align="left"><p>0x63F</p></td>
<td align="left"><p>FL, FR, FC, LFE, BL, BR, SL, SR</p></td>
</tr>
</tbody>
</table>

 

By comparing the two preceding tables, the following points are apparent:

-   The meaning of the channel mask 0x3F in the first table has not changed in the second table, even though in Windows SP2 and later versions of Windows, KSAUDIO\_SPEAKER\_5POINT1 is interpreted to use SL and SR speakers instead of BL and BR.

-   A new channel mask that has the value 0x63F is supported. This channel mask represents the 7.1 home theater speaker configuration.

-   **Note**   In Windows Vista and later versions of Windows, the KSAUDIO\_SPEAKER\_7POINT1 speaker configuration is no longer supported. As a result, it is not an available option in Control Panel.

     

To represent the same set of speaker configurations, Dsound.h defines the following speaker-configuration IDs:

```cpp
  #define DSSPEAKER_5POINT1             0x00000006
  #define DSSPEAKER_7POINT1             0x00000007
  #define DSSPEAKER_7POINT1_SURROUND    0x00000008
  #define DSSPEAKER_7POINT1_WIDE        DSSPEAKER_7POINT1
```

DSSPEAKER\_7POINT1\_SURROUND represents the new 7.1 home theater speaker configuration in Control Panel. DSSPEAKER\_7POINT1 and DSSPEAKER\_7POINT1\_WIDE are both names for the same 7.1 wide configuration speakers configuration.

For more information about speaker configuration for DirectSound, see [DirectSound Speaker-Configuration Settings](directsound-speaker-configuration-settings.md).

 

 




