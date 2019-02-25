---
title: KSNODETYPE\_VOLUME
description: KSNODETYPE\_VOLUME
ms.assetid: 4776ea69-6492-428e-97ce-dd8842f22c16
keywords: ["KSNODETYPE_VOLUME Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_VOLUME
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_VOLUME


## <span id="ddk_ksnodetype_volume_ks"></span><span id="DDK_KSNODETYPE_VOLUME_KS"></span>


The KSNODETYPE\_VOLUME node represents a volume (gain or attenuation) control. The volume control has one input stream and one output stream; each of the two streams has the same data format. It can apply attenuation (reduction in volume) or gain (increase in volume) to the stream. In addition, it can optionally support inverting the signal.

For information about multichannel volume nodes, see [Exposing Multichannel Nodes](https://msdn.microsoft.com/library/windows/hardware/ff536380).

A KSNODETYPE\_VOLUME node should support the following required property:

[**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](ksproperty-audio-volumelevel.md)

 

 





