---
Description: DirectSound Capture Effects
MS-HAID: 'audio.directsound\_capture\_effects'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: DirectSound Capture Effects
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
<td align="left"><p>[<strong>KSNODETYPE_ACOUSTIC_ECHO_CANCEL</strong>](audio.ksnodetype_acoustic_echo_cancel)</p></td>
</tr>
<tr class="even">
<td align="left"><p>GUID_DSCFX_CLASS_NS</p></td>
<td align="left"><p>[<strong>KSNODETYPE_NOISE_SUPPRESS</strong>](audio.ksnodetype_noise_suppress)</p></td>
</tr>
</tbody>
</table>

 

In Microsoft Windows XP and later, you can expose your audio device's hardware-accelerated capture effects to DirectSound applications. In addition, the AEC system filter (Aec.sys) provides software emulation of AEC and NS effects.

These topics are discussed in the remainder of this section:

[Exposing Hardware-Accelerated Capture Effects](exposing-hardware-accelerated-capture-effects.md)

[AEC System Filter](aec-system-filter.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DirectSound%20Capture%20Effects%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



