---
title: KSNODETYPE\_PROLOGIC\_ENCODER
description: KSNODETYPE\_PROLOGIC\_ENCODER
ms.assetid: cca6fe1d-20f8-4112-956b-a1b33b48a4ff
keywords: ["KSNODETYPE_PROLOGIC_ENCODER Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_PROLOGIC_ENCODER
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_PROLOGIC\_ENCODER


## <span id="ddk_ksnodetype_prologic_encoder_ks"></span><span id="DDK_KSNODETYPE_PROLOGIC_ENCODER_KS"></span>


The KSNODETYPE\_PROLOGIC\_ENCODER node represents a Dolby Surround Pro Logic encoder. The node accepts a four-channel input stream with channels for left, right, center, and back speakers. The node encodes the input stream as a surround-encoded stereo output stream.

The functionality of the KSNODETYPE\_PROLOGIC\_ENCODER node is complementary to the [**KSNODETYPE\_PROLOGIC\_DECODER**](ksnodetype-prologic-decoder.md) node, which takes a surround-encoded stereo input stream and decodes it into a four-channel stream with channels for left, right, center, and back speakers.

In Microsoft Windows XP and later, the [KMixer system driver](https://msdn.microsoft.com/library/windows/hardware/ff537039#kmixer-system-driver) has a KSNODETYPE\_PROLOGIC\_ENCODER node.

A KSNODETYPE\_PROLOGIC\_ENCODER node should support the [**KSPROPERTY\_AUDIO\_SURROUND\_ENCODE**](ksproperty-audio-surround-encode.md) property, which is used to enable and disable the node.

 

 





