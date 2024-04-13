---
title: KSNODETYPE\_TONE
description: KSNODETYPE\_TONE
keywords: ["KSNODETYPE_TONE Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSNODETYPE_TONE
api_type:
- NA
ms.date: 03/06/2023
---


# KSNODETYPE\_TONE


## <span id="ddk_ksnodetype_tone_ks"></span><span id="DDK_KSNODETYPE_TONE_KS"></span>


The KSNODETYPE\_TONE node represents a tone control. The tone control has one input stream and one output stream; the two streams have the same data format. It can attenuate the amount of bass, treble, or mid-frequencies of the output stream. In addition, it can optionally support a bass boost or gain.

A KSNODETYPE\_TONE node should support at least one of the following properties:

[**KSPROPERTY\_AUDIO\_BASS**](ksproperty-audio-bass.md)

[**KSPROPERTY\_AUDIO\_MID**](ksproperty-audio-mid.md)

[**KSPROPERTY\_AUDIO\_TREBLE**](ksproperty-audio-treble.md)

[**KSPROPERTY\_AUDIO\_BASS\_BOOST**](ksproperty-audio-bass-boost.md)

 

 





