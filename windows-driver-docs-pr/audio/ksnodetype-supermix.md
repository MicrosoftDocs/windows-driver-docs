---
title: KSNODETYPE\_SUPERMIX
description: KSNODETYPE\_SUPERMIX
keywords: ["KSNODETYPE_SUPERMIX Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSNODETYPE_SUPERMIX
api_type:
- NA
ms.date: 03/06/2023
---


# KSNODETYPE\_SUPERMIX


## <span id="ddk_ksnodetype_supermix_ks"></span><span id="DDK_KSNODETYPE_SUPERMIX_KS"></span>


The KSNODETYPE\_SUPERMIX node represents a supermixer. A supermixer has one input stream with *m* channels and one output stream with *n* channels. For each output channel, the supermixer specifies a mix level for each of the input channels that adds to the mix in the output channel. The *m*-channel input stream is upmixed or down-mixed to *n* channels.

A KSNODETYPE\_SUPERMIX node should support the following required properties:

[**KSPROPERTY\_AUDIO\_MIX\_LEVEL\_TABLE**](ksproperty-audio-mix-level-table.md)

[**KSPROPERTY\_AUDIO\_MIX\_LEVEL\_CAPS**](ksproperty-audio-mix-level-caps.md)

 

 





