---
title: KSNODETYPE\_AUDIO\_ENGINE
description: The KSNODETYPE\_AUDIO\_ENGINE audio endpoint is a new endpoint that is available with Windows 8 and later versions of Windows.
ms.assetid: C1A7E136-655A-4024-A280-F252F1AE1282
keywords: ["KSNODETYPE_AUDIO_ENGINE Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_AUDIO_ENGINE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_AUDIO\_ENGINE


The KSNODETYPE\_AUDIO\_ENGINE audio endpoint is a new endpoint that is available with Windows 8 and later versions of Windows. The KSNODETYPE\_AUDIO\_ENGINE audio endpoint is contained within a Wave kernel streaming (KS) audio filter, and it allows an audio driver to expose the capabilities of the hardware audio engine.

The KSNODETYPE\_AUDIO\_ENGINE audio endpoint is a required endpoint and its introduction made it necessary to develop a new Wave data sink pin factory to which the new endpoint directly connects.

The KSNODETYPE\_AUDIO\_ENGINE audio endpoint must support the [**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md) enumerated values in addition to the following KS properties:

[**KSPROPERTY\_AUDIO\_MUTE**](ksproperty-audio-mute.md)

[**KSPROPERTY\_AUDIO\_PEAKMETER**](ksproperty-audio-peakmeter.md)

[**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](ksproperty-audio-volumelevel.md)

[KSPROPSETID\_AudioEngine](kspropsetid-audioengine.md)

 

 





