---
title: KSNODETYPE\_REVERB
description: KSNODETYPE\_REVERB
keywords: ["KSNODETYPE_REVERB Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSNODETYPE_REVERB
api_type:
- NA
ms.date: 03/06/2023
---


# KSNODETYPE\_REVERB


## <span id="ddk_ksnodetype_reverb_ks"></span><span id="DDK_KSNODETYPE_REVERB_KS"></span>


The KSNODETYPE\_REVERB node represents a reverberation (or "reverb") control. The reverb node has one input stream and one output stream, and the input and output streams have the same data format. The node adds reverberation to the output stream.

A KSNODETYPE\_REVERB node should support the following required properties:

[**KSPROPERTY\_AUDIO\_REVERB\_LEVEL**](ksproperty-audio-reverb-level.md)

[**KSPROPERTY\_AUDIO\_REVERB\_TIME**](ksproperty-audio-reverb-time.md)

 

 





