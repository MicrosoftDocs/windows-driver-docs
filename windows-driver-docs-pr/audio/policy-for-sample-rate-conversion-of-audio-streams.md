---
title: Policy for Sample Rate Conversion of Audio Streams
description: Policy for Sample Rate Conversion of Audio Streams
ms.assetid: 5a54e1fb-abf6-4ab1-808d-0233e3e3a478
keywords:
- SRC WDK audio , policy
- sample-rate conversion WDK audio , policy
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Policy for Sample Rate Conversion of Audio Streams


## <span id="policy_for_sample_rate_conversion_of_audio_streams"></span><span id="POLICY_FOR_SAMPLE_RATE_CONVERSION_OF_AUDIO_STREAMS"></span>


This section describes the policy that the KMixer system driver follows for sample-rate conversion (SRC).

KMixer does SRC on audio streams only if it must do so to match the sample rate of more than one stream. Most applications that use more than one audio stream use the same sample rate for each stream. However, KMixer uses the following client-based policy to match sampling rates:

-   **DirectSound clients**

    For rendering streams, the Windows multimedia control panel (Mmsys.cpl) gives a user some control over which type of SRC the KMixer driver uses with DirectSound. The slider shown in the Advanced Audio Properties dialog (see [DirectSound Hardware-Acceleration and SRC Sliders](directsound-hardware-acceleration-and-src-sliders.md)) assigns the settings **Good** through **Best** to linear interpolation, multipoint interpolation, and high-end multipoint interpolation, respectively. Linear interpolation is the default for the DirectSound versions that ship with Microsoft Windows 98/Me and Windows 2000. In Windows XP and later, the default is high-end multipoint interpolation.

    For DirectSound capture streams, KMixer always uses high-end multipoint interpolation.

-   **All other audio stream clients**

    The KMixer driver always uses high-end multipoint interpolation for render and capture streams that are associated with the Windows Multimedia functions (which include the waveOut API), Redbook CD, and the Sound Blaster emulator and software synthesizer.

The following table categorizes types of Windows audio applications and the system component that each type of application uses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Audio Application</th>
<th align="left">System Component</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows Sound Recorder</p></td>
<td align="left"><p>Windows Multimedia (Winmm.sys)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Media Player</p></td>
<td align="left"><p>DirectSound (Dsound.dll)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DirectX titles, including most games</p></td>
<td align="left"><p>DirectSound</p></td>
</tr>
<tr class="even">
<td align="left"><p>Most high-end wave editors</p></td>
<td align="left"><p>Windows Multimedia</p></td>
</tr>
</tbody>
</table>

 

Note that in Windows 98/Me, the Windows Multimedia functions are implemented in Mmsystem.dll. In Windows 2000 and later, the Windows Multimedia functions are implemented in Winmm.sys, and calls from 16-bit applications to Mmsystem.dll thunk to 32-bit calls to Winmm.sys. For more information about thunking calls from 16-bit code to 32-bit functions, see the Microsoft Windows SDK documentation.

 

 




