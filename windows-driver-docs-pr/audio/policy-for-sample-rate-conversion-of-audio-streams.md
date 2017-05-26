---
title: Policy for Sample Rate Conversion of Audio Streams
description: Policy for Sample Rate Conversion of Audio Streams
ms.assetid: 5a54e1fb-abf6-4ab1-808d-0233e3e3a478
keywords:
- SRC WDK audio , policy
- sample-rate conversion WDK audio , policy
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Policy%20for%20Sample%20Rate%20Conversion%20of%20Audio%20Streams%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


