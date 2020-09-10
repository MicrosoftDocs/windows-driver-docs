---
title: KSPROPERTY\_INTERLEAVEDAUDIO_FORMATINFORMATION 
description: The KSPROPERTY\_INTERLEAVEDAUDIO_FORMATINFORMATION property provides  additional information about the interleaving of loopback audio and capture audio.
keywords: ["KSPROPERTY_INTERLEAVEDAUDIO_FORMATINFORMATION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_INTERLEAVEDAUDIO_FORMATINFORMATION 
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 07/11/2019
ms.localizationpriority: medium
---

# KSPROPERTY\_INTERLEAVEDAUDIO_FORMATINFORMATION

The **KSPROPERTY\_INTERLEAVEDAUDIO_FORMATINFORMATION** property provides additional information about the interleaving of loopback audio and capture audio.

## Usage Summary Table

 |Get|Set|Target|Property descriptor type|Property value type|
|--- |--- |--- |--- |--- |
|Yes|No|Pin|[KS_PIN](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)|[INTERLEAVED_AUDIO_FORMAT_INFORMATION](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_interleaved_audio_format_information)|

### Return Value

 For the get, **KSPROPERTY\_INTERLEAVEDAUDIO_FORMATINFORMATION** returns an [INTERLEAVED_AUDIO_FORMAT_INFORMATION](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_interleaved_audio_format_information) structure which contains additional information about the interleaving of loopback audio and capture audio in the audio stream.

Starting in Windows 10 19H1, setting the KSPROPERTY\_INTERLEAVEDAUDIO_FORMATINFORMATION property key is a requirement for systems that support the Hardware Keyword Spotter (HW KWS) that combine microphone and loopback audio into a single stream, in order to use an AEC APO on the keyword burst output. For more information, see [Voice Activation](voice-activation.md).

## Remarks

This property is intended only for the Hardware Keyword Spotter pin and provides a way to include loopback audio interleaved with the microphone audio. This is done by interleaving the Hardware Keyword Spotter pin audio and loopback audio together into a single PCM audio stream and then communicating, via this property, the channels containing loopback vs. microphone audio.

A sample APO is available that makes use of this property. It is on GitHub as part of the sysvad sample driver and is called *KWSApo*. The sample APO simply strips out the loopback audio, providing only the primary microphone audio upstream.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 10 Version 19H1|
|Header|Ksmedia.h|

## See also

[KSPROPSETID\_INTERLEAVEDAUDIO](kspropsetid-interleavedaudio.md)

[KS_PIN](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[INTERLEAVED_AUDIO_FORMAT_INFORMATION](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_interleaved_audio_format_information)