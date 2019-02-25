---
title: KSNODETYPE\_NOISE\_SUPPRESS
description: KSNODETYPE\_NOISE\_SUPPRESS
ms.assetid: 416504e2-38eb-4cfd-ae20-6f1f44a82abd
keywords: ["KSNODETYPE_NOISE_SUPPRESS Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_NOISE_SUPPRESS
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_NOISE\_SUPPRESS


## <span id="ddk_ksnodetype_noise_suppress_ks"></span><span id="DDK_KSNODETYPE_NOISE_SUPPRESS_KS"></span>


The KSNODETYPE\_NOISE\_SUPPRESS node represents a noise-suppression (NS) control. An NS node has connections for one input stream and one output stream. Both streams have the same format.

When a filter containing an NS node is created or the node is reset, the node is initially configured to operate in pass-through mode.

An NS node can be incorporated into an AEC (acoustic echo cancellation) filter to support full-duplex DirectSound applications. For more information, see [DirectSound Capture Effects](https://msdn.microsoft.com/library/windows/hardware/ff536327).

A KSNODETYPE\_NOISE\_SUPPRESS node in an AEC filter should support the following properties in order to enable hardware acceleration:

[**KSPROPERTY\_AUDIO\_CPU\_RESOURCES**](ksproperty-audio-cpu-resources.md)

[**KSPROPERTY\_AUDIO\_ALGORITHM\_INSTANCE**](ksproperty-audio-algorithm-instance.md)

[**KSPROPERTY\_TOPOLOGYNODE\_ENABLE**](ksproperty-topologynode-enable.md)

[**KSPROPERTY\_TOPOLOGYNODE\_RESET**](ksproperty-topologynode-reset.md)

The KSPROPERTY\_TOPOLOGYNODE\_ENABLE property is used to both enable and disable the node. When disabled, the node operates in pass-through mode (that is, it allows the input stream to pass through to the output without modification).

 

 





