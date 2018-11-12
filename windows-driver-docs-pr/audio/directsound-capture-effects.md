---
title: DirectSound Capture Effects
description: DirectSound Capture Effects
ms.assetid: 5dcadcea-0b6a-447d-828d-a7f256f97088
keywords:
- DirectSound WDK audio , capture effects
- acoustic echo cancellation WDK audio
- noise suppression WDK audio
- AEC WDK audio
- capture effects WDK audio
- full-duplex applications WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectSound Capture Effects


## <span id="directsound_capture_effects"></span><span id="DIRECTSOUND_CAPTURE_EFFECTS"></span>


DirectSound 8 adds some new features for enabling and controlling third-party effects during audio capture. This and later versions of DirectSound support the following two capture effects:

-   Acoustic echo cancellation (AEC)

-   Noise suppression (NS)

In a full-duplex audio application such as telephone conferencing, echoes of the render stream being output through the speakers are picked up in the microphone that generates the capture stream. After characterizing the sound reflections in the room or other physical environment, the full-duplex system uses AEC to monitor the render stream to cancel out the echoes that it adds to the capture stream. The system can further improve the quality of the capture stream by using NS to detect noise spikes and remove them from the stream.

A full-duplex DirectSound application can use the **IDirectSoundCaptureFXAec** and **IDirectSoundCaptureFXNoiseSuppress** interfaces to control the AEC and NS effects. The **IDirectSoundCaptureBuffer::GetObjectInPath** method retrieves pointers to objects with these interfaces. The **DirectSoundFullDuplexCreate** function creates the **IDirectSoundCaptureBuffer** object, and the parameters that the caller passes to this function include an array of DSCEFFECTDESC structures. The array specifies the effects that are to be enabled in the capture buffer. The **guidDSCFXClass** member of each structure in the array contains a GUID that specifies an effect: AEC or NS. The DirectSound name for each GUID is shown in the following table, along with the KS name for the same GUID value. For details, see the DirectX 8.0 SDK documentation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DirectSound GUID Name</th>
<th align="left">KS GUID Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>GUID_DSCFX_CLASS_AEC</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537150" data-raw-source="[&lt;strong&gt;KSNODETYPE_ACOUSTIC_ECHO_CANCEL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537150)"><strong>KSNODETYPE_ACOUSTIC_ECHO_CANCEL</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>GUID_DSCFX_CLASS_NS</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537182" data-raw-source="[&lt;strong&gt;KSNODETYPE_NOISE_SUPPRESS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537182)"><strong>KSNODETYPE_NOISE_SUPPRESS</strong></a></p></td>
</tr>
</tbody>
</table>

 

In Microsoft Windows XP and later, you can expose your audio device's hardware-accelerated capture effects to DirectSound applications. In addition, the AEC system filter (Aec.sys) provides software emulation of AEC and NS effects.

These topics are discussed in the remainder of this section:

[Exposing Hardware-Accelerated Capture Effects](exposing-hardware-accelerated-capture-effects.md)

[AEC System Filter](aec-system-filter.md)

 

 




