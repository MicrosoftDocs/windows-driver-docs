---
title: DSSPEAKER_DIRECTOUT Speaker Configuration
description: DSSPEAKER_DIRECTOUT Speaker Configuration
ms.assetid: a4198fb7-157f-40e3-8cca-5a9e392087d2
keywords:
- DSSPEAKER_DIRECTOUT speaker configuration WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DSSPEAKER\_DIRECTOUT Speaker Configuration


## <span id="dsspeaker_directout_speaker_configuration"></span><span id="DSSPEAKER_DIRECTOUT_SPEAKER_CONFIGURATION"></span>


**Note**  This information applies to Windows XP and earlier operating systems. Starting with Windows Vista, **IDirectSound::GetSpeakerConfig** and **IDirectSound::SetSpeakerConfig** have been deprecated.

 

An application program can change the DirectSound speaker configuration to direct-out mode by calling the **IDirectSound::SetSpeakerConfig** method with the speaker-configuration parameter set to DSSPEAKER\_DIRECTOUT (see Microsoft Windows SDK documentation). This specifies a speakerless configuration in which the channels in the playback stream from the application are output directly to the audio adapter without being interpreted as speaker positions. However, the input stream can still be modified by sample-rate conversion, attenuation, filtering, and other types of processing that require no assumptions about the assignment of speakers to channels.

Once it takes effect, the DSSPEAKER\_DIRECTOUT speaker-configuration setting is global and affects the audio device as a whole. All audio applications that subsequently run are subject to the new setting until DirectSound changes the setting again.

In direct-out mode, the audio device renders the first channel to the first output connector on the device, the second channel to the second output on the device, and so on. This allows an audio authoring application to output multichannel data directly to a device such as an external mixer or an audio storage device (hard disk, ADAT, and so on). For example, the channels in a 48-channel stream might be assigned as shown in the following table.

Channel Number
Content
0

Vocal

1

Drums

2

Guitar

3

Bass

...

47

Piano

 

For this kind of raw audio data, speaker positions are meaningless, and assigning speaker positions to the input or output streams might cause unwanted side effects. For example, a component such as KMixer might intervene inappropriately by applying speaker-specific effects such as 3D virtualization or Dolby Surround Pro Logic encoding to the stream. Note that the number of raw-data channels is not limited by the number of bits in the channel mask.

Even a device that is not designed specifically for audio editing should typically accept a [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537250) set-property request to change its speaker configuration to KSAUDIO\_SPEAKER\_DIRECTOUT. In general, a device should avoid failing the request unless it can somehow verify that its outputs are connected to speakers and cannot be used externally for any other purpose (for example, as inputs to an external mixer).

An application that uses direct-out mode is typically written for a specific hardware device. This allows the application to know in advance which direct-out data formats the device supports, including the number of channels and how the data in those channels should be interpreted. This knowledge is necessary because when an application calls **IDirectSound::GetSpeakerConfig** on a device that is configured in direct-out mode, the device merely confirms that it is in this mode; it provides no additional information regarding the number of channels in the stream formats that it supports in direct-out mode. (This information might be obtained, however, by sending a [**KSPROPERTY\_AUDIO\_MIX\_LEVEL\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff537291) get-property request to the supermixer node on the device's mixer pin; see [DirectSound Node-Ordering Requirements](directsound-node-ordering-requirements.md).)

When specifying the wave format for a direct-out stream, an application should set the **dwChannelMask** member of the [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) structure to the value KSAUDIO\_SPEAKER\_DIRECTOUT, which is zero. A channel mask of zero indicates that no speaker positions are defined. As always, the number of channels in the stream is specified in the **Format.nChannels** member.

Hardware vendors have the option of supporting DirectSound hardware acceleration when their devices are configured in direct-out mode. A DirectSound application can play back a direct-out stream through one of the device's mixing pins, if one is available. Once all the available hardware pin instances have been exhausted, any new streams pass through KMixer instead.

When mixing streams for a device that is configured in direct-out mode, KMixer applies a one-to-one mapping between the channels of the input streams from the applications and the channels of the mix stream that it outputs to the device. This means that if the application generates several direct-out streams that have the same number of channels, for example, each channel N of the output mix is simply the sum of channels N of all the streams that enter KMixer.

When mixing several direct-out streams that differ in the number of channels they contain, KMixer's mixing algorithm is slightly more complex. In this case, each channel N of the mix is the sum of channels N of all input streams that have a channel N. For example, if KMixer mixes quad and stereo input streams to form a quad output mix, channels zero and one of the output mix are the sums of channels zero and one, respectively, of the input stereo and quad streams. The stereo input stream contributes nothing, however, to channels two and three of the mix, which are taken solely from the last two channels of the quad input stream.

An application that attempts to do either of the following is risking unpredictable behavior:

-   Play a stream that is not in direct-out format through a device that is configured in direct-out mode.

-   Play a direct-out stream through a device that is not configured in direct-out mode.

When faced with one of these cases, KMixer avoids simply failing the attempt to open the stream. Instead, it tries to handle the apparent incompatibility by using the one-to-one mapping algorithm that is described above. The user may or may not be satisfied with the result. Other audio components cannot be expected to handle these cases in the same way as KMixer. For example, the driver for a device that is configured in direct-out mode should fail an attempt to open a hardware buffer for an output stream that is not in direct-out format, and vice versa.

An audio authoring application might need to let the user listen to the data that it has mixed into the first several channels of its output stream but ignore the raw data that is still contained in the remaining channels of the stream. KMixer's behavior makes this straightforward. For example, if a 24-channel playback stream contains a stereo mix in channels 0 and 1 and raw data in channels 2 through 23, the application does the following:

-   Configures the target audio device (this is not necessarily the device that the application uses to edit the stream) in stereo mode by calling **SetSpeakerConfig** with DSSPEAKER\_STEREO.

-   Changes **dwChannelMask** in the playback stream's [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) structure to KSAUDIO\_SPEAKER\_STEREO but leaves **Format.nChannels** set to 24, which is the total number of channels in the stream.

KMixer mixes only the stereo channels of the playback stream, which are described in the channel mask, and discards the remaining 22 channels, which contain raw data. Remember that any change made to the DirectSound speaker-configuration setting is unlikely to take effect until the current DirectSound object is destroyed and another is created (see [Applying Speaker-Configuration Settings](applying-speaker-configuration-settings.md)).

 

 




