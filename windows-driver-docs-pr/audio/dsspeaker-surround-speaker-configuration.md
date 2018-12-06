---
title: DSSPEAKER_SURROUND Speaker Configuration
description: DSSPEAKER_SURROUND Speaker Configuration
ms.assetid: de8f861b-f190-4915-b3f0-95d39965b612
keywords:
- DSSPEAKER_SURROUND speaker configuration WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DSSPEAKER\_SURROUND Speaker Configuration


## <span id="dsspeaker_surround_speaker_configuration"></span><span id="DSSPEAKER_SURROUND_SPEAKER_CONFIGURATION"></span>


**Note**  This information applies to Windows XP and earlier operating systems. Starting with Windows Vista, **IDirectSound::GetSpeakerConfig** and **IDirectSound::SetSpeakerConfig** have been deprecated.

 

An application program can change the DirectSound speaker configuration to surround mode by calling the **IDirectSound::SetSpeakerConfig** method with the speaker-configuration parameter set to DSSPEAKER\_SURROUND. This specifies a four-channel PCM format in which the channels are mapped to left, right, center, and back speakers.

Once it takes effect, the DSSPEAKER\_SURROUND speaker-configuration setting is global and affects the audio device as a whole. All audio applications that subsequently run are subject to the new setting until DirectSound changes the setting again.

DirectSound uses the following algorithm to configure the audio system for surround mode:

1.  DirectSound first asks the driver to go into the surround speaker mode by sending a [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537250) set-property request to the driver's DAC node (or 3D node if it has no DAC node). (See [**KSNODETYPE\_DAC**](https://msdn.microsoft.com/library/windows/hardware/ff537158) and [**KSNODETYPE\_3D\_EFFECTS**](https://msdn.microsoft.com/library/windows/hardware/ff537148).) The [**KSAUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537083) structure that accompanies this property request specifies the KSAUDIO\_SPEAKER\_SURROUND speaker configuration. If the request succeeds, the audio device routes the four channels to four analog outputs that are connected directly to left, right, center, and back speakers.

2.  If that fails, DirectSound asks the driver to configure the device in stereo speaker mode and to enable its [**KSNODETYPE\_PROLOGIC\_ENCODER**](https://msdn.microsoft.com/library/windows/hardware/ff537187) node, if it has one. If this succeeds, the device converts the four-channel stream from the application to a surround-encoded stereo signal that it outputs in either digital or analog form. (The hardware should do the encoding after mixing the streams that flow into the device's various mixer pins.) The user can connect the device's stereo outputs to an external decoder that converts the encoded signal into four channels that are output to left, right, center, and back speakers.

3.  If that fails, DirectSound enables the KSNODETYPE\_PROLOGIC\_ENCODER node in KMixer. (The device is already in stereo mode from the previous step.) Again, the stereo signal that is output by the device can be fed to an external decoder.

If this algorithm succeeds, the application can create and play four-channel PCM buffers. In cases 1 and 2 above, the hardware buffers that the device reads from use four channels, but in case 3 the hardware buffers use a stereo format. The application can write directly to the hardware buffers in cases 1 and 2, but in case 3 it should write to a software buffer and allow KMixer to convert the application's four-channel stream to the surround-encoded stereo format needed for the hardware buffer.

In case (3) above, the application should avoid using hardware buffers for any of its output streams. Note that KMixer mixes all its input streams before encoding the mix to produce the surround stereo stream. However, any stream that enters a hardware mixer pin is mixed in hardware with the encoded stereo from KMixer, which degrades the quality of the surround audio when it is decoded. The application can prevent this by using only software buffers.

A stereo stream that has been surround-encoded by a KSNODETYPE\_PROLOGIC\_ENCODER node can be decoded into four channels (left, right, center, and back) by a [**KSNODETYPE\_PROLOGIC\_DECODER**](https://msdn.microsoft.com/library/windows/hardware/ff537185) node.

 

 




