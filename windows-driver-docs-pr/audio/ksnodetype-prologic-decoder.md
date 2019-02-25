---
title: KSNODETYPE\_PROLOGIC\_DECODER
description: KSNODETYPE\_PROLOGIC\_DECODER
ms.assetid: 905ff503-1aff-4490-bd6f-f6bec8e7c3d6
keywords: ["KSNODETYPE_PROLOGIC_DECODER Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_PROLOGIC_DECODER
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_PROLOGIC\_DECODER


## <span id="ddk_ksnodetype_prologic_decoder_ks"></span><span id="DDK_KSNODETYPE_PROLOGIC_DECODER_KS"></span>


The KSNODETYPE\_PROLOGIC\_DECODER node represents a Dolby Surround Pro Logic decoder. The decoder control has one stereo input stream and one output stream with one to four channels. In the four-channel output format, the channels are mapped to left, right, center, and back speaker. In the three-channel output format, the channels are mapped to left, right, and back speakers.

The functionality of the KSNODETYPE\_PROLOGIC\_DECODER node is complementary to the [**KSNODETYPE\_PROLOGIC\_ENCODER**](ksnodetype-prologic-encoder.md) node, which converts a four-channel input stream to a surround-encoded stereo output stream.

A KSNODETYPE\_PROLOGIC\_DECODER node should support the following required properties:

[**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](ksproperty-audio-channel-config.md)

[**KSPROPERTY\_TOPOLOGYNODE\_ENABLE**](ksproperty-topologynode-enable.md)

[**KSPROPERTY\_TOPOLOGYNODE\_RESET**](ksproperty-topologynode-reset.md)

The KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG property sets and gets the channel configuration of the node's output stream.

 

 





