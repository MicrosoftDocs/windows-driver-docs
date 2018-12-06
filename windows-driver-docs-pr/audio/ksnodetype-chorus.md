---
title: KSNODETYPE\_CHORUS
description: KSNODETYPE\_CHORUS
ms.assetid: fa7c4f4a-163d-4d16-a6ba-fa11adeb9ffb
keywords: ["KSNODETYPE_CHORUS Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_CHORUS
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_CHORUS


## <span id="ddk_ksnodetype_chorus_ks"></span><span id="DDK_KSNODETYPE_CHORUS_KS"></span>


The KSNODETYPE\_CHORUS node represents a chorus effects processor, which adds a chorus effect to the output stream. The chorus node has one input stream and one output stream, and these two streams share the same data format.

A KSNODETYPE\_CHORUS node should support the following required properties:

[**KSPROPERTY\_AUDIO\_CHORUS\_LEVEL**](ksproperty-audio-chorus-level.md)

[**KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH**](ksproperty-audio-chorus-modulation-depth.md)

[**KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_RATE**](ksproperty-audio-chorus-modulation-rate.md)

 

 





