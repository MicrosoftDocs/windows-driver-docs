---
title: KSNODETYPE\_EQUALIZER
description: KSNODETYPE\_EQUALIZER
keywords: ["KSNODETYPE_EQUALIZER Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSNODETYPE_EQUALIZER
api_type:
- NA
ms.date: 03/06/2023
---


# KSNODETYPE\_EQUALIZER


## <span id="ddk_ksnodetype_equalizer_ks"></span><span id="DDK_KSNODETYPE_EQUALIZER_KS"></span>


The KSNODETYPE\_EQUALIZER node represents an equalizer with multiple frequency bands. By adjusting the level that the equalization table assigns to each of the frequency bands, an EQ node can control the amount of each frequency band that appears in the node's output stream.

An EQ node has one input stream and one output stream, and the two streams share a common data format.

A KSNODETYPE\_EQUALIZER node should support the following required properties:

[**KSPROPERTY\_AUDIO\_EQ\_LEVEL**](ksproperty-audio-eq-level.md)

[**KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS**](ksproperty-audio-num-eq-bands.md)

[**KSPROPERTY\_AUDIO\_EQ\_BANDS**](ksproperty-audio-eq-bands.md)

 

 





