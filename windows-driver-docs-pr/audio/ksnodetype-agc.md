---
title: KSNODETYPE\_AGC
description: KSNODETYPE\_AGC
ms.assetid: 54d6bb6a-9c15-4020-bc6e-92b24878e1fd
keywords: ["KSNODETYPE_AGC Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_AGC
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_AGC


## <span id="ddk_ksnodetype_agc_ks"></span><span id="DDK_KSNODETYPE_AGC_KS"></span>


The KSNODETYPE\_AGC node represents an automatic gain control (AGC). An AGC node has one input stream and one output stream, and each of the two streams has the same data format. The node automatically adjusts the amount of attenuation or gain applied to the input stream to achieve maximum dynamic range without clipping the signal.

A KSNODETYPE\_AGC node should support the following property:

[**KSPROPERTY\_AUDIO\_AGC**](ksproperty-audio-agc.md)

A KSNODETYPE\_AGC node can also support the following optional properties:

[**KSPROPERTY\_TOPOLOGYNODE\_ENABLE**](ksproperty-topologynode-enable.md)

[**KSPROPERTY\_TOPOLOGYNODE\_RESET**](ksproperty-topologynode-reset.md)

The KSPROPERTY\_TOPOLOGYNODE\_ENABLE property is used to both enable and disable the node. When disabled, the node operates in pass-through mode (that is, it allows the input stream to pass through to the output without modification).

 

 





