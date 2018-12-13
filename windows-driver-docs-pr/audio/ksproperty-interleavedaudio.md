---
title: KSPROPERTY\_INTERLEAVEDAUDIO
description: The KSPROPERTY\_INTERLEAVEDAUDIO property provides  additional information about the interleaving of loopback audio and capture audio.
keywords: ["KSPROPERTY_INTERLEAVEDAUDIO Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_INTERLEAVEDAUDIO
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 12/12/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_INTERLEAVEDAUDIO

The **KSPROPERTY\_INTERLEAVEDAUDIO** property provides additional information about the interleaving of loopback audio and capture audio.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

 |Get|Set|Target|Property descriptor type|Property value type|
|--- |--- |--- |--- |--- |
|Yes|No|Pin|[KSPROPERTY](https://msdn.microsoft.com/library/windows/hardware/ff564262)|[INTERLEAVED_AUDIO_FORMAT_INFORMATION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-interleaved-audio-format-information)|

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

 For the get, **KSPROPERTY\_INTERLEAVEDAUDIO** returns an [INTERLEAVED_AUDIO_FORMAT_INFORMATION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-interleaved-audio-format-information) structure which contains additional information about the interleaving of loopback audio and capture audio in the audio stream. 

Remarks
-------

This property is intended only for the Hardware Keyword Spotter pin and provides a way to include loopback audio interleaved with the microphone audio. This is done by interleaving the Hardware Keyword Spotter pin audio and loopback audio together into a single PCM audio stream and then communicating, via this property, the channels containing loopback vs. microphone audio.

A sample APO is available that makes use of this property. It is on GitHub as part of the sysvad sample driver and is called *KWSApo*. The sample APO simply strips out the loopback audio, providing only the primary microphone audio upstream.


Requirements
------------

|||
|--- |--- |
|Minimum supported client|Windows 10 Version 19H1|
|Header|Ksmedia.h|

## <span id="see_also"></span>See also

[KSPROPSETID\_INTERLEAVEDAUDIO](kspropsetid-interleavedaudio.md)

[KSPROPERTY](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 






