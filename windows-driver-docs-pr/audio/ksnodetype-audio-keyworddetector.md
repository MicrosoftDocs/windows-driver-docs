---
title: KSNODETYPE\_AUDIO\_KEYWORDDETECTOR
description: The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR audio endpoint is a new endpoint that is available with Windows 10 and later versions of Windows. The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR allows an audio capture driver to support a detector.
keywords: ["KSNODETYPE_AUDIO_KEYWORDDETECTOR Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSNODETYPE_AUDIO_KEYWORDDETECTOR
api_type:
- NA
ms.date: 03/06/2023
---


# KSNODETYPE\_AUDIO\_KEYWORDDETECTOR


The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR audio endpoint is a new endpoint that is available with Windows 10 and later versions of Windows. The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR allows an audio capture driver to support a detector.

This filter cannot be shared with other capture devices. The filter has a KS pin factory that has pin category KSNODETYPE\_AUDIO\_KEYWORDDETECTOR. There cannot be more than one pin factory having this KS pin category in a given KS filter instance.

The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR audio endpoint must support the following KS properties:

[**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md)

[**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md)

[**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md)

[**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md)

## <span id="see_also"></span>See also


[KSPROPSETID\_SoundDetector](kspropsetid-sounddetector.md)

 

 






